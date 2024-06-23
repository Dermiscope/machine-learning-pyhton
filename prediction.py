import os
import numpy as np
from PIL import Image, UnidentifiedImageError
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tensorflow as tf
import requests
from io import BytesIO
from collections import Counter, defaultdict
from storage import upload_to_gcs

def getPrediction(detection_id, image_url):
    # Memuat model object detection
    model = tf.saved_model.load("./saved_model_v2/saved_model")

    # Memuat gambar dari URL
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        image = Image.open(BytesIO(response.content))
    except (requests.RequestException, UnidentifiedImageError) as e:
        return {"error": f"Error loading image: {e}"}

    image_np = np.array(image)

    # Menjalankan deteksi
    input_tensor = tf.convert_to_tensor(image_np)
    input_tensor = input_tensor[tf.newaxis,...]
    detections = model(input_tensor)

    # Ekstrak data deteksi
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # Deteksi dalam bentuk dictionary
    detection_classes = detections['detection_classes'].astype(np.int64)
    detection_boxes = detections['detection_boxes']
    detection_scores = detections['detection_scores']

    class_names = {
        1: 'Bekas Jerawat',
        2: 'Blackhead',
        3: 'Nodule',
        4: 'Papules',
        5: 'Pori-Pori',
        6: 'Pustule',
        7: 'Whitehead'
    }

    # Menghitung frekuensi kemunculan setiap kelas dan rata-rata threshold
    class_counter = Counter(detection_classes[detection_scores >= 0.3])
    class_scores = defaultdict(list)

    for cls, score in zip(detection_classes, detection_scores):
        if score >= 0.2:
            class_scores[cls].append(score)

    class_avg_scores = {cls: np.mean(scores) for cls, scores in class_scores.items()}

    # Menyusun hasil deteksi dalam format yang diminta
    detection_results = []
    for class_id, count in class_counter.items():
        detection_results.append({
            "name": class_names.get(class_id, 'Unknown'),
            "accuration": round(class_avg_scores[class_id], 2),
            "count": count
        })

    # Menambahkan bounding boxes ke gambar
    fig, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(image)

    for i in range(num_detections):
        if detection_scores[i] >= 0.3:  # Threshold untuk menampilkan deteksi
            box = detection_boxes[i]
            y_min, x_min, y_max, x_max = box
            (left, right, top, bottom) = (x_min * image_np.shape[1], x_max * image_np.shape[1], y_min * image_np.shape[0], y_max * image_np.shape[0])
            
            rect = patches.Rectangle((left, top), right - left, bottom - top, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            
            class_name = class_names.get(detection_classes[i], 'Unknown')
            ax.text(left, top, f'{class_name}: {detection_scores[i]:.2f}', bbox=dict(facecolor='yellow', alpha=0.5))

    # Construct output image path based on the original file name
    output_image_name = os.path.basename(image_url).split('?')[0]  # Remove query parameters if any
    output_image_path = f"predicted_{output_image_name}"
    plt.axis('off')  # Menghilangkan axis sebelum menyimpan
    plt.savefig(output_image_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    # Upload the image to Bucket Storage
    image_uploaded_public_url = ""
    try:
        image_uploaded_public_url += upload_to_gcs(detection_id, output_image_path)
    except Exception as ex:
        print(f"Failed to upload file: {ex}")

    # Delete the image after successful upload
    try:
        os.remove(output_image_path)
        print(f"Image {output_image_path} deleted successfully.")
    except OSError as e:
        return {"error": f"Error deleting image: {e}"}

    return {"publicUrl" : image_uploaded_public_url, "detection_results" : detection_results}
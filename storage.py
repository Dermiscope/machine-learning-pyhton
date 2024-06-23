import os
from google.cloud import storage
from dotenv import load_dotenv # type: ignore

# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mendapatkan jalur kredensial dari variabel lingkungan
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

# Mengatur variabel lingkungan untuk Google Cloud
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

def upload_to_gcs(detection_id, source_file_name):
    try:
        destination_blob_name = f"detections/{detection_id}/result/{os.path.basename(source_file_name)}"
        
        # Initialize a storage client
        storage_client = storage.Client()

        # Get the bucket
        bucket = storage_client.bucket("dermiscope")

        # Create a blob object from the bucket
        blob = bucket.blob(destination_blob_name)

        # Upload the file to GCS
        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
        return f"https://storage.cloud.google.com/dermiscope/detections/{detection_id}/result/{source_file_name}"

    except Exception as e:
        print(f"An error occurred: {e}")

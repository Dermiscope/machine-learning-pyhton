from flask import Flask, request, jsonify
from prediction import getPrediction
from rangking import process_data
from treatment import find_treatment_by_acne_type

app = Flask(__name__)

@app.route("/predictions", methods=["POST"])
def predictions():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        detection_id = data.get("id")
        image_urls = data.get("faces")

        if not image_urls or not isinstance(image_urls, list):
            return jsonify({"error": "No valid image URLs provided"}), 400

        faces_result = []
        results = []
        for image_url in image_urls:
            try:
                result = getPrediction(detection_id, image_url["publicUrl"])
                if "error" in result:
                    results.append({"image_url": image_url["publicUrl"], "error": result["error"]})
                else:
                    for detection in result["detection_results"]:
                        results.append(detection)
                    faces_result.append({"publicUrl": result["publicUrl"]})
            except Exception as e:
                print(e)
                results.append({"image_url": image_url["publicUrl"], "error": str(e)})

        best_prediction = process_data(results)
        treatment = find_treatment_by_acne_type(best_prediction["name"])['treatment']

        return jsonify({
            "type": best_prediction["name"],
            "accuration": round(best_prediction['accuration'] * 100, 2),
            "faces_result": faces_result,
            "treatment": treatment
        })

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

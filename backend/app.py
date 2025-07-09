from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Check for PIL/Pillow before proceeding
try:
    from PIL import Image
    print("PIL/Pillow is correctly installed.")
except ImportError:
    print("ERROR: PIL/Pillow is not properly installed. Installing now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow==9.5.0"])
    print("Pillow installation complete. Importing again...")
    from PIL import Image
    print("PIL/Pillow is now correctly installed.")

# Now import transformers
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load the garbage classification model from Hugging Face
try:
    print("Loading the garbage classification model...")
    classifier = pipeline("image-classification", model="yangy50/garbage-classification")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    print(f"Exception type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    
    # Try an alternative approach with more explicit imports if the main approach fails
    try:
        print("\nAttempting alternative model loading approach...")
        from transformers import AutoImageProcessor, AutoModelForImageClassification
        
        image_processor = AutoImageProcessor.from_pretrained("yangy50/garbage-classification")
        model = AutoModelForImageClassification.from_pretrained("yangy50/garbage-classification")
        classifier = pipeline("image-classification", model=model, image_processor=image_processor)
        print("Alternative model loading successful.")
    except Exception as alt_e:
        print(f"Alternative approach also failed: {str(alt_e)}")
        raise

@app.route('/api/classify', methods=['POST'])
def classify_garbage():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Save the uploaded file temporarily
        temp_path = os.path.join(os.getcwd(), "temp_image.jpg")
        file.save(temp_path)
        
        # Run the image through the model
        result = classifier(temp_path)
        
        # Clean up the temporary file
        os.remove(temp_path)
        
        # Return the classification results
        return jsonify({
            'success': True,
            'predictions': result
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        # Print version information
        import flask
        import werkzeug
        print(f"Running with Flask {flask.__version__} and Werkzeug {werkzeug.__version__}")
        print("Starting server on http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"Error starting server: {str(e)}")
        print(f"Exception type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

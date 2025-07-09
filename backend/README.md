# Garbage Classification API

This is a Flask-based API for classifying garbage images using a Hugging Face model.

## Setup

1. Create a Python virtual environment:
```
python -m venv venv
```

2. Activate the virtual environment:
```
# On Windows
venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

## Running the API

Start the server:
```
python app.py
```

The API will be available at http://localhost:5000

## API Endpoints

### POST /api/classify

Send a POST request with an image file to classify the type of garbage.

Example using curl:
```
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:5000/api/classify
```

Response format:
```json
{
  "success": true,
  "predictions": [
    {
      "label": "garbage_type",
      "score": 0.95
    },
    ...
  ]
}
```

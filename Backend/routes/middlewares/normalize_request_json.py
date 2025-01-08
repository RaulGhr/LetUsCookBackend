from flask import Flask, request

app = Flask(__name__)

@app.before_request
def normalize_request_json():
    if request.method == 'OPTIONS':
        return '', 200
    if request.is_json:
        original_get_json = request.get_json

        def get_normalized_json(*args, **kwargs):
            data = original_get_json(*args, **kwargs)
            if data:
                return {key.lower(): value for key, value in data.items()}
            return data

        request.get_json = get_normalized_json
from flask import Flask, render_template, request, send_file
import os
import torch
from PIL import Image
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = torch.hub.load('yolov5', 'yolov5s', source='local')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    filename = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Run detection
    results = model(filepath)
    results.render()  # Render results on the image

    # Save result
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], "out_" + filename)
    Image.fromarray(results.ims[0]).save(output_path)

    return render_template("index.html", result_image="uploads/out_" + filename)

if __name__ == '__main__':
    app.run(debug=True)

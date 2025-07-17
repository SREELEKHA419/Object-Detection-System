
#  Object Detection System using YOLOv5 🚗📦

A web-based real-time object detection application using **YOLOv5** and **Flask**. This system allows users to upload an image and detect multiple objects such as cars, people, animals, and more with high accuracy.

---

##  Project Structure

```

📁 OUTPUTS/             # Stores output images with detections
📁 static/              # Static files like CSS, JS, and uploaded images
📁 templates/           # HTML files (Jinja2 templating)
📁 yolov5/              # YOLOv5 model source (must be cloned manually)
📄 app.py               # Flask app runner
📄 detect.py            # YOLOv5 detection logic
📄 detect\_choice.py     # Handles model choice or variations
📄 cars.jpg             # Sample input image
📄 detected\_image.jpg   # Output image with detections
📄 yolov5s.pt           # Pre-trained YOLOv5 model weights

````

---

##  Setup Instructions

### Prerequisites
- Python 3.8+
- pip

###  Clone YOLOv5 Repository Manually
YOLOv5 needs to be cloned manually (cannot be uploaded directly).

```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
````

###  Install Other Required Packages

```bash
pip install flask opencv-python pillow torch torchvision
```

###  Run the Flask App

Make sure you're in the main project directory (where `app.py` is located):

```bash
python app.py
```

Now open your browser and visit:

```
http://127.0.0.1:5000/
```

---

##  Features

* Upload any image to detect objects.
* View output images with bounding boxes and labels.
* Uses pre-trained YOLOv5s model (`yolov5s.pt`).
* Clean and responsive frontend using Flask and HTML templates.

---

##  Model Details

* Model used: YOLOv5s
* File: `yolov5s.pt` (Pre-trained by Ultralytics)
* Classes supported: 80+ (COCO dataset)

Download pre-trained weights (if not included):
👉 [Download yolov5s.pt](https://github.com/ultralytics/yolov5/releases)

Save it in the project root as `yolov5s.pt`.

---

##  Tech Stack

* Python
* Flask
* OpenCV
* PyTorch
* YOLOv5
* HTML/CSS (Jinja2 templates)

---

##  Sample Output

![Sample](static/outputs/detected_image.jpg)

---

##  License

Open-source project under the MIT License.
Please cite Ultralytics for the YOLOv5 base repository.


## AUTHOR 

Sreelekha A S, B S Abdur Rahman Crescent Institute Of Science And Technology
Chennai

---

##  Acknowledgements

* [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)

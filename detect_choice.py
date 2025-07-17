import torch
import cv2
from PIL import Image
import os

# Load YOLOv5s model from local
model = torch.hub.load('./yolov5', 'yolov5s', source='local')
model.conf = 0.5  # Confidence threshold

def detect_image(image_path):
    if not os.path.exists(image_path):
        print("❌ Image not found.")
        return

    img = Image.open(image_path)
    results = model(img)
    results.print()

    results.render()
    result_img = Image.fromarray(results.ims[0])
    result_img.show()

    output_path = "detected_image.jpg"
    result_img.save(output_path)
    print(f"✅ Result saved as {output_path}")

def detect_video(video_source=0):
    cap = cv2.VideoCapture(video_source)
    if not cap.isOpened():
        print("❌ Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        results.render()
        frame = results.ims[0]
        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Detection ended.")

def main():
    print("\n🧠 Object Detection Menu")
    print("1. Detect image")
    print("2. Detect video or webcam")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        img_path = input("Enter full image path (e.g., image.jpg): ").strip().strip('"')
        detect_image(img_path)
    elif choice == '2':
        use_webcam = input("Use webcam? (y/n): ").lower()
        if use_webcam == 'y':
            detect_video(0)
        else:
            video_path = input("Enter full video path (e.g., video.mp4): ")
            detect_video(video_path)
    else:
        print("❌ Invalid choice.")

if __name__ == '__main__':
    main()

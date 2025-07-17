import torch
import cv2
from PIL import Image
import os

# Load the YOLOv5s model (from local)
model = torch.hub.load('./yolov5', 'yolov5s', source='local')
model.conf = 0.5  # Confidence threshold

def detect_image(image_path):
    if not os.path.exists(image_path):
        print("❌ Image not found.")
        return

    img = Image.open(image_path)
    results = model(img)
    results.print()

    results.render()  # draws results on the image
    result_img = Image.fromarray(results.ims[0])
    result_img.show()

    # Optionally save output
    output_path = "detected_image.jpg"
    result_img.save(output_path)
    print(f"✅ Saved result as: {output_path}")


def detect_video(video_source=0):
    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("❌ Could not open video source.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        results.render()
        frame = results.ims[0]

        cv2.imshow("YOLOv5 Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("✅ Video detection ended.")


def main():
    print("\n🧠 Object Detection System")
    print("1. Detect objects in an image")
    print("2. Detect objects in a video or webcam")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        img_path = input("Enter image file path (e.g., image.jpg): ")
        detect_image(img_path)
    elif choice == '2':
        use_webcam = input("Use webcam? (y/n): ").lower()
        if use_webcam == 'y':
            detect_video(0)  # 0 = default webcam
        else:
            video_path = input("Enter video file path (e.g., video.mp4): ")
            detect_video(video_path)
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()

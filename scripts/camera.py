import cv2
from scripts.model import detect_objects  # Import your model's detection function

scanning = False


def start_scan():
    global scanning
    scanning = True


def gen_frames():
    global scanning
    camera = cv2.VideoCapture(0)  # Use 0 for the default camera
    while True:
        success, frame = camera.read()  # Read the camera frame
        if not success:
            break
        else:
            if scanning:
                # Detect objects and draw bounding boxes
                frame = detect_objects(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()

from flask import Flask, Response, render_template
from scripts.camera import gen_frames
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('open_camera.html')

@app.route('/camera')
def camera():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/scan')
def scan():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
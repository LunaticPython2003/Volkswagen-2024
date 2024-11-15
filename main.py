from flask import Flask, render_template, Response, jsonify, request
from scripts.camera import gen_frames, start_scan

app = Flask(__name__)

scanning = False  # To control scanning globally


@app.route('/')
def index():
    return render_template('open_camera.html')


@app.route('/camera')
def camera():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/scan', methods=['GET'])
def scan():
    global scanning
    scanning = True
    start_scan()  # Enable scanning in the camera module
    return jsonify({"message": "Scanning started"})


@app.route('/click', methods=['POST'])
def click():
    data = request.json
    # Process the click event and return the clicked bounding box data
    return jsonify({"message": "Click received", "data": data})


if __name__ == '__main__':
    app.run(debug=True)

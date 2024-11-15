import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load your trained model
model = load_model('static/models/model.h5')


def detect_objects(frame):
    # Preprocess the frame for your model
    input_frame = cv2.resize(frame, (224, 224))  # Resize to your model's input size
    input_frame = np.expand_dims(input_frame, axis=0)  # Add batch dimension
    input_frame = input_frame / 255.0  # Normalize if required by your model

    # Perform inference
    predictions = model.predict(input_frame)[0]  # Assuming batch size of 1

    # Post-process the predictions to draw bounding boxes
    height, width, _ = frame.shape
    bounding_boxes = []  # Store bounding box data for frontend
    for i in range(0, len(predictions), 5):  # Assuming [x_min, y_min, x_max, y_max, confidence]
        try:
            x_min, y_min, x_max, y_max, confidence = predictions[i:i+5]
            if confidence > 0.5:  # Draw boxes with confidence > 50%
                start_point = (int(x_min * width), int(y_min * height))
                end_point = (int(x_max * width), int(y_max * height))
                color = (0, 255, 0)  # Green color
                thickness = 2
                frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

                # Append bounding box for frontend
                bounding_boxes.append([start_point, end_point])
        except ValueError:
            print(f"Unexpected prediction format at index {i}: {predictions[i:i+5]}")
            continue

    return frame

# ⚽ Football Match Video Analysis System

This project is an end-to-end **football analytics pipeline** that takes raw match footage as input and performs detailed player and ball analysis using computer vision and machine learning techniques. It produces visually enhanced and data-rich insights such as player speed, ball possession, and camera movement correction.

---

## 📌 Key Features

### 🎯 1. Ball Interpolation
- Fills in missing detections in ball trajectory using **data interpolation**.
- Ensures continuous tracking even if the ball is occluded.

### 🧠 2. Player-Ball Assignment
- Determines which player has possession of the ball at every frame.
- Uses **Euclidean distance** thresholding to associate the ball with nearby players.

### 🎥 3. Camera Movement Estimation
- Detects and accounts for moving camera by estimating frame-to-frame shift.
- Uses **Lucas-Kanade Optical Flow** to track feature point displacements.
- Removes camera bias to ensure accuracy in positional data.

### 📐 4. Perspective Transformation
- Maps pixel coordinates to real-world positions using **homography matrix**.
- Converts video data into actual on-field player locations (in meters).
- Based on OpenCV’s `cv2.getPerspectiveTransform`.

### 🏃 5. Speed & Distance Calculation
- Estimates real-time speed (in km/h) and cumulative distance covered (in meters) for each player.
- Based on **transformed positions** and **frame rate**.

---


## 🧪 Requirements

- Python 3.8+
- OpenCV
- NumPy
- pandas
- matplotlib
- scikit-learn
- torch (for PyTorch models, if used for detection)
- pickle (standard lib)

## 🚀 How to Run the Project

Follow these steps to successfully run the entire video analysis pipeline:

---

### Step 1: Train the Model (if not already trained)

Before running the analysis, you need to train the detection model (for detecting players, ball, etc.).

You can use any object detection model such as YOLO, Faster R-CNN, or a custom-trained model.

Once trained, save the model weights as a `.pt` file.

For example:
models/best.pt
models/last.pt

    
### Step 2: Put the input video in input_videos folder
python main.py

├── input_videos/input_video.mp4  

### Step 3: Run the Analysis Pipeline
python main.py

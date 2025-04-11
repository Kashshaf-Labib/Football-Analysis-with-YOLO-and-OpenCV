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

## 🛠️ Project Structure

project/ │ ├── src/ │ ├── interpolate.py │ ├── assign_player_ball.py │ ├── camera_motion.py │ ├── perspective_transform.py │ ├── speed_distance.py │ └── utils.py │ ├── stubs/ │ └── (optional cached camera motion results) │ ├── input_videos/ │ └── match.mp4 │ ├── output_videos/ │ └── annotated_output.mp4 │ ├── requirements.txt ├── README.md └── .gitignore

## 🧪 Requirements

- Python 3.8+
- OpenCV
- NumPy
- pandas
- matplotlib
- scikit-learn
- torch (for PyTorch models, if used for detection)
- pickle (standard lib)


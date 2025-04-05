import cv2

## reads video frame by frame and returns a list of frames
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(ouput_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*"XVID") ## codec/format of the video
    out = cv2.VideoWriter(
        output_video_path,
        fourcc,
        24, ##fps
        (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0]), ## width, height
    )
    for frame in ouput_video_frames:
        out.write(frame)
    out.release()

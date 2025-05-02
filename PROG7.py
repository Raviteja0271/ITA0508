import cv2

# Slow motion video (slow_factor > 1)
def slow_motion(input_video, output_video, slow_factor=2):
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get original fps
    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"XVID"), fps / slow_factor, 
                          (int(cap.get(3)), int(cap.get(4))))  # Adjust FPS for slow motion
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        # Write each frame multiple times to slow down the video
        for _ in range(slow_factor):
            out.write(frame)
    
    cap.release()
    out.release()
    print(f"Slow motion video saved as {output_video}")

# Fast motion video (fast_factor > 1)
def fast_motion(input_video, output_video, fast_factor=2):
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get original fps
    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*"XVID"), fps * fast_factor, 
                          (int(cap.get(3)), int(cap.get(4))))  # Adjust FPS for fast motion
    
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break
        # Skip frames to speed up the video
        if frame_count % fast_factor == 0:
            out.write(frame)
        frame_count += 1
    
    cap.release()
    out.release()
    print(f"Fast motion video saved as {output_video}")

# Input video path
input_video = "your_video.mp4"

# Create slow-motion video
slow_motion(input_video, "slow_motion_video.avi", slow_factor=2)

# Create fast-motion video
fast_motion(input_video, "fast_motion_video.avi", fast_factor=2)

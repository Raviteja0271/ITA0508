import cv2

cap = cv2.VideoCapture("your_video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

normal_delay = int(1000 / fps)
slow_delay = int(1000 / (fps / 0.5))
fast_delay = int(1000 / (fps * 2))

def play_video(delay, title):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(title, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyWindow(title)

play_video(normal_delay, "Normal Speed")
play_video(slow_delay, "Slow Motion")
play_video(fast_delay, "Fast Motion")

cap.release()
cv2.destroyAllWindows()

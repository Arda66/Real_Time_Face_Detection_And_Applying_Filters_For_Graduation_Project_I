import cv2

def Manual_Real_Time_Video_Enhancement(brigtness,contrast,saturation,zoom,sharpness,width=1280,height=720,framerate=30):  # We set Default as HD (1280x720)
    cap = cv2.VideoCapture(0)
    cap.set(3,width)
    cap.set(4,height)
    cap.set(5,framerate)
    cap.set(10,brigtness)
    cap.set(11,contrast)
    cap.set(12,saturation)
    cap.set(27,zoom)
    cap.set(20,sharpness)

    while True:
        ret, frame = cap.read()
        cv2.imshow("Video", frame)
        if cv2.waitKey(10) & 0xFF == ord('e'):
            break


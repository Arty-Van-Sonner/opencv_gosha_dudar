import cv2

cap = cv2.VideoCapture(0)
# cap.set(3, 500) w-size
# cap.set(4, 300) h-size

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
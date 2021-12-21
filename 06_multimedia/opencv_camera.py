import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    exit()

# ret, frame = cap.read()
# cv2.imshow('a', frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 13:
        break

# while True:
#     if cv2.waitKey() == 13:
#         break

cv2.imwrite('camera.jpg', frame)

cap.release()
cv2.destroyALLWindows()
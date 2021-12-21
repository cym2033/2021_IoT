import cv2

img = cv2.imread('avenger.jpg')

img2 = cv2.resize(img, (710, 496))

img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('Averger', img)
cv2.imshow('averger', img2)
cv2.imshow('averger_g', img3)
cv2.imshow('Averger_edge1', edge1)
cv2.imshow('Averger_edge2', edge2)
cv2.imshow('Averger_edge3', edge3)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('avenger_GRAY.jpg', img3)
cv2.destroyAllWindows()
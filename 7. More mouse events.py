import cv2
import numpy as np

# events =  [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    # Joining two points where we left clicked.
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 255), 5)
        cv2.imshow('Image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorImg = np.zeros((512, 512, 3), dtype=np.uint8)
        mycolorImg[:] = [blue, green, red]

        cv2.imshow('color', mycolorImg)

# img = np.zeros([512, 512, 3], dtype=np.uint8)
img = cv2.imread('images/lena.jpg')

# Window name should be same everywhere
cv2.imshow('Image', img)
points = []

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
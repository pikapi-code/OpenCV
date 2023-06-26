import cv2
import numpy as np

# events =  [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        s = str(x) + ', ' + str(y)
        cv2.putText(img, s, (x, y), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        s = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, s, (x, y), font, 0.5, (255, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
        

# img = np.zeros([512, 512, 3], dtype=np.uint8)
img = cv2.imread('images/lena.jpg')

# Window name should be same everywhere
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
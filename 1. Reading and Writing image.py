import cv2

img = cv2.imread('images/lena.jpg', -1)

cv2.imshow("Image", img)

# Setting value as 0, window will have to be manually closed
k = cv2.waitKey(0) or 0

if k == 27: # 27 is the escape key
    cv2.destroyAllWindows()
elif k == ord('s'): # If s is pressed
    cv2.imwrite('images/LenaUpdate.jpg', img)
    cv2.destroyAllWindows()
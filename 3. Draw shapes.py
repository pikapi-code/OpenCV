import cv2
import numpy as np

# Creating image using numpy
# Parameters Height, weight and 3
img = np.zeros([512, 512, 3], dtype=np.uint8)

#img = cv2.imread('images/lena.jpg', 1)

# First argument is the image, then start position
# then the end point, then the color, and finally the thickness
img = cv2.line(img, (0,1), (255, 255), (255, 255, 0), 5)
img = cv2.arrowedLine(img, (0,255), (255, 255), (255, 0, 0), 5)

# 2nd argument is the top left coordinate, 
# 3rd argument is the bottom right coordinate
# 4th argument is the color
# 5th argument is the thickness, if -1 then it fills the rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (255, 0, 0), 10)

# 2nd argument is the centre, 
# 3rd argument is the radius
# 4th argument is the color
# 5th argument is the thickness, if -1 then it fills the rectangle
img = cv2.circle(img, (447,63), 63, (0, 255, 0), -1)

# 2nd argument is the text, 3rd argument is the coordinate
# 4th argument is the font, 5th argument is the font size
# 6th argument is the color, 7th argument is the thickness
# 8th argument is the line type
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
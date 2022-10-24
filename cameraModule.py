import os
from turtle import pos
import cv2

posterImgPath = "C:/Users/prana/Desktop/Python/c104/assets/poster.jpg"

posterImg = cv2.imread(posterImgPath)

rocket = posterImg[120:360, 400:500]
posterImg[0:240, 500:600] = rocket

text_to_show = "Hello"
cv2.putText(posterImg, text_to_show, (200, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 0, 255))

# gray_image = cv2.cvtColor(posterImg, cv2.COLOR_RGB2GRAY)
# cv2.imshow("Poster Gray", gray_image)



cv2.imshow("Poster", posterImg)
cv2.waitKey(0)

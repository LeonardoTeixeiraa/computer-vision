import cv2
import numpy as np

image = cv2.imread('cubo.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([98,109,20])
upper_blue = np.array([112,255,255])
img_final = cv2.inRange(hsv_image, lower_blue, upper_blue)
cv2.imwrite("imagem.jpg", img_final)
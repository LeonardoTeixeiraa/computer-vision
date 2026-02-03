import cv2
import numpy as np

mascara = np.zeros((296,295), dtype="uint8")
cv2.circle(mascara, (100,100), 50, (255,255,255), -1)
cv2.imwrite("mascara-circular.png", mascara)
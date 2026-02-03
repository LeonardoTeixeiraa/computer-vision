import cv2
import numpy as np

mascara = np.zeros((200,200), dtype="uint8")
cv2.rectangle(mascara, (50,50), (150,150), (255,255,255), -1)
cv2.imwrite("mascara-retangular.png", mascara)
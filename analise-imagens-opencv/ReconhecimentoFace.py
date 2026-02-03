#Algoritmo para reconhecimento de faces
import cv2

loadFaceAlgorithm = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
loadEyeAlgorithm = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
#carrega a imagem 1
img = cv2.imread('img/imagem1.jpeg')

#Transforma a imagem para a escala de cinza
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = loadFaceAlgorithm.detectMultiScale(grayImg, scaleFactor=1.016) 

print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(img, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey()
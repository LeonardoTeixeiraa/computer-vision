#Algoritmo para reconhecimento de olhos
import cv2

loadFaceAlgorithm = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
loadEyeAlgorithm = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

#carrega a imagem 1
img = cv2.imread('img/imagem5.jpg')
#Transforma a imagem para a escala de cinza
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = loadFaceAlgorithm.detectMultiScale(grayImg, scaleFactor = 1.3, minNeighbors = 4) 

for(x, y, l, a) in faces:
   faceRead = cv2.rectangle(img, (x, y), (x + l, y + a), (0, 255, 0), 2)
   faceArea = faceRead[y:y + a, x:x + l]
   eyeToGrayScale = cv2.cvtColor(faceArea, cv2.COLOR_BGR2GRAY)
   detectedEye = loadEyeAlgorithm.detectMultiScale(
    eyeToGrayScale,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(20, 20)
)

   for(ox, oy, ol, oa) in detectedEye:
      if oy < a / 2: #metade superior da face
        cv2.rectangle(faceArea, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

cv2.imshow("Detecta face e olhos", img)
cv2.waitKey()
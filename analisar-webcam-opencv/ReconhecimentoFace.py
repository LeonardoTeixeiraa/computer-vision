#Algoritmo que irá reconhecer uma face a partir da camera do computador
import cv2 

#Habilita a camera do computador
webcam = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not webcam.isOpened():
    print("Erro ao acessar a câmera")
    exit()

classificadorVideoFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
loadEyeAlgorithm = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

while True:
    camera, frame = webcam.read()

    #Validação para evitar crash gráfico caso frame venha como none
    if not camera:
        break

    grayScaleImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificadorVideoFace.detectMultiScale(grayScaleImg)

    for(x, y, l, a) in detecta:
        faceRead = cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 0), 2 )
        faceArea = faceRead[y:y + a, x:x + l]
        faceAreaToGrayScale = cv2.cvtColor(faceArea, cv2.COLOR_BGR2GRAY)
        detectedEye = loadEyeAlgorithm.detectMultiScale(faceAreaToGrayScale,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(20, 20))
        
        for(ox, oy, ol, oa) in detectedEye:
            if oy < a / 2: #metade superior da face
                cv2.rectangle(faceArea, (ox, oy), (ox + ol, oy + oa), (255, 0, 255), 2)

    cv2.imshow("Video camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
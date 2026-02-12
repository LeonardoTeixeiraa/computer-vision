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
        
        contador = str(detecta.shape[0])

        cv2.putText(frame, contador, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.putText(frame, "Quantidade de Face: " + contador, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Video camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
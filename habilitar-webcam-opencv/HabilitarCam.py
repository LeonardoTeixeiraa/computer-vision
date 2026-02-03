#Algoritmo que irá reconhecer uma face a partir da camera do computador
import cv2 

#Habilita a camera do computador
webcam = cv2.VideoCapture(0)

while True:
    camera, frame = webcam.read()

    cv2.imshow("Imagem camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
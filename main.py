import cv2
from test import *
from AlunosFace import *
import os
alunos = "./alunosFace/"

path = "/home/jvvitor307/miniconda3/envs/TrabalhoIA/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml"
clf = cv2.CascadeClassifier(path)
cap = cv2.VideoCapture(0)
while not cv2.waitKey(20) & 0xFF == ord('q'):
    ret, frame = cap.read()
    gray = EscalaCinza(frame)
    faces = DetectarRosto(gray)
    recorte = cortarImagem(faces, frame)
    try:
        salvarImagem("saida.png", recorte)
    except Exception as e:
        print("Nenhum rosto detectado")
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0))

    cv2.imshow('frame', frame)
    for aluno in os.listdir(alunos):
        caminho = alunos+aluno
        try:
            result = verificacao("saida.png", caminho)
            print(f"{aluno[:-4]}:{result}")
        except Exception as e:
            print("Nehnhum rosto detectado")

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)












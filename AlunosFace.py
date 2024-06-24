import cv2
from test import *
import os


pastaAlunos = "./alunos/"
alunosFace = "./alunosFace/"
lenalunos = len(os.listdir(pastaAlunos))
alunos = os.listdir(pastaAlunos)

path = "/home/jvvitor307/miniconda3/envs/TrabalhoIA/share/opencv4/haarcascades/haarcascade_frontalface_alt2.xml"
clf = cv2.CascadeClassifier(path)

def EscalaCinza(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

def DetectarRosto(framecinza):
    faces = clf.detectMultiScale(framecinza)
    return faces
def cortarImagem(faces, frame):
    for x, y, w, h in faces:
        recorte = frame[y:(y + w), x:(x + h), :]
        return recorte
def salvarImagem(caminhoParaSalvar, imagem):
    cv2.imwrite(caminhoParaSalvar, imagem)

# for i in range(0, lenalunos):
#     frame = cv2.imread(pastaAlunos + alunos[i])
#     gray = EscalaCinza(frame)
#     faces = DetectarRosto(gray)
#     recorte = cortarImagem(faces, frame)
#     salvarImagem(alunosFace + alunos[i], recorte)
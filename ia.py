import face_recognition as fr
from datetime import datetime

alunospresentes = []
frequencia = {"Dia": [], "Alunos": []}

#Carrega a imagem do arquivo
def carregarImagem(nome):
    return fr.load_image_file(nome)

#Localiza a face na imagem
def localizarFace(img, i):
    return fr.face_locations(img)[i]

#Carrega o encoding da face
def carregarEncoding(img,i):
    return fr.face_encodings(img)[i]

#Quantidade de faces na imagem
def qtdFaces(img):
    return len(fr.face_locations(img))

#Compara duas faces
def compararFaces(encode1, encode2):
    return fr.compare_faces([encode1], encode2)

#Função para verificar a presença do aluno
def presenca(alunos, caminhoPasta):
    for i in range(len(alunos['nome'])):
        aluno = carregarEncoding(carregarImagem(alunos['foto'][i]), 0)
        for j in range(qtdFaces(carregarImagem(caminhoPasta))):
            encodingAlunoSala = carregarEncoding(carregarImagem(caminhoPasta), j)
            if compararFaces(aluno, encodingAlunoSala)[0]:
                print(compararFaces(aluno, encodingAlunoSala))
                alunospresentes.append(alunos['nome'][i])
                print(f"{alunos['nome'][i]} está presente.")
                break
    frequencia['Dia'].append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    frequencia['Alunos'].append(alunospresentes.copy())
    alunospresentes.clear()
    return frequencia


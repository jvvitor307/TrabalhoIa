from Alunos import *
from Camera import *
from ia import *
import cv2

alunos = CarregarAlunos_csv()

def sistema():
    print("Sistema de reconhecimento facial")
    print("1 - Cadastrar aluno")
    print("2 - Reconhecer aluno")
    print("3 - Sair")
    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        cadastrar_aluno(alunos)
        salvar_csv(alunos, "alunos")
        sistema()
    elif escolha == "2":
        foto = capturar_foto()
        if qtdFaces(carregarImagem(foto)) > 0:
            freq = presenca(alunos, foto)
            salvar_csv(freq, "frequencia")
            sistema()
    elif escolha == "3":
        print("saindo...")
    else:
        print("Opção inválida.")
        sistema()

sistema()

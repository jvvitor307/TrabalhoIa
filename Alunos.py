import tkinter as tk
import pandas as pd
from tkinter import filedialog
from PIL import Image
import os

# Dicionário de alunos


def cadastrar_aluno(aluno):
    nome = input('Digite o nome do aluno: ')
    caminho_foto = cadastrar_foto_aluno(nome)
    fotoV = foto_valida(caminho_foto)
    if fotoV:
        aluno['nome'].append(nome)
        aluno['foto'].append(caminho_foto)
        print("Aluno cadastrado com sucesso.")
    else:
        print("Aluno não cadastrado.")


def foto_valida(caminho_foto, cont=0):
    if caminho_foto:
        return True
    else:
        cont += 1
        if cont == 2:
            print("Você não conseguiu cadastrar a foto do aluno.")
            return False
        print("Foto inválida.")
        caminho_foto = cadastrar_foto_aluno()
        return foto_valida(caminho_foto, cont)


def cadastrar_foto_aluno(nomealuno):
    # Cria uma instância da janela Tkinter
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Abre o gerenciador de arquivos para selecionar a imagem
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione a foto do aluno",
        filetypes=[("Arquivos de imagem", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if caminho_arquivo:
        # Carrega a imagem selecionada
        imagem = Image.open(caminho_arquivo)

        # Cria o diretório 'fotos_alunos' se não existir
        diretorio_destino = "fotos_alunos"
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)

        # Salva a imagem no diretório desejado
        caminho_destino = os.path.join(diretorio_destino, f"{nomealuno}.jpg")
        imagem.save(caminho_destino)
        print(f"Foto do aluno cadastrada com sucesso: {caminho_destino}")
        return caminho_destino
    else:
        print("Nenhuma imagem foi selecionada.")
        return None


def salvar_csv(dicionario, nome_arquivo):
    print(dicionario)
    # Verifica se todas as listas têm o mesmo comprimento
    lengths = [len(v) for v in dicionario.values()]
    if len(set(lengths)) != 1:
        raise ValueError("Todas as listas no dicionário devem ter o mesmo comprimento.")

    # Exibir o dicionário para debug
    print("Dicionário recebido:", dicionario)

    # Cria o DataFrame a partir do dicionário
    df = pd.DataFrame.from_dict(dicionario)

    # Exibir o DataFrame para debug
    print("DataFrame criado:", df)

    # Salva o DataFrame em um arquivo CSV
    df.to_csv(f"{nome_arquivo}.csv", index=False, encoding='utf-8')
    print("Arquivo CSV criado com sucesso!")


def CarregarAlunos_csv():
    # Carrega o arquivo CSV
    try:
        df = pd.read_csv('alunos.csv')

        # Converte o DataFrame em um dicionário
        dicionario = df.to_dict(orient='list')
    except FileNotFoundError:
        print("Arquivo 'alunos.csv' não encontrado.")
        dicionario = {'nome': [], 'idade': [], 'foto': []}
    return dicionario


# Chama a função para cadastrar aluno e transformar o dicionário em CSV

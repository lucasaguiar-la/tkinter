from tkinter import *
# Função qualquer para ação de botão
index = 0
def click():
    global index
    index += 1
    print(f"Você apertou o botão {index} vezes!")

# Título e icone
janela = Tk()
janela.iconbitmap('favicon.ico')
janela.title('Aperte o botão...')


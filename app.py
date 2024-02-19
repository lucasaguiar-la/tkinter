from tkinter import *
# Função qualquer para ação de botão
index = 0
def click():
    global index
    index += 1
    if index == 1:
        print("Apertou 1 vez!")
    else:
        print(f"Apertou {index} vezes!")

# Título e icone
janela = Tk()
janela.iconbitmap('favicon.ico')
janela.title('Contador de cliques...')

# Dimensão da janela
largura = 500
altura = 300

# Resolução da tela
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Posição da janela baseado na resolução da tela
posx = largura_tela/2 - largura/2
posy = altura_tela/2 - altura/2

# Definir geometria da janela
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
#janela.geometry("500x300+1200+880")

# Janela não redimensionável
janela.resizable(0,0)

# Labels e textos
label_01 = Label (
    janela,
    text="Apenas clique...",
    font=("Arial", 20),
    width=100,
    height=2,
    padx=15,
    pady=10,
    anchor=W)
label_01.pack()
label_02 = Label (
    janela,
    text="...no...",
    font=("Arial", 20),
    width=100,
    height=2,
    anchor=CENTER)
label_02.pack()
label_03 = Label (
        janela,
        text="...botão!",
        font=("Arial", 20),
        width=100,
        height=2,
        padx=15,
        pady=10,
        anchor=E)
label_03.pack()

# Botão de ação
btn = Button(
    janela,
    text='Aperte aqui!',
    width=20,
    padx=10,
    pady=10,
    command=lambda: click()
)
btn.pack()

# Loop da janela
janela.mainloop()
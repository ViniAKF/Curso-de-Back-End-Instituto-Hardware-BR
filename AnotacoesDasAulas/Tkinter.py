"""
---------------------CUSTOM TKINTER--------------------------

Hoje vamos ver sobre a maneira de construir uma interface gráfica com o Python

16/05
"""

import customtkinter as ctk #arquivo com várias classes

#tema
ctk.set_appearance_mode("dark")

#cor padrão
ctk.set_default_color_theme("blue")

#cria janela
janela = ctk.CTk() #acessa o arquivo para poder pegar a classe -- inicializa ela vazia já que n sabemos a ordem
janela.title("Minha segunda interface")
janela.geometry("500x300")

#Colocando texto
texto = ctk.CTkLabel(
    janela,
    text="Olá Mundo",
    font=("Arial", 24)
)  

texto.pack(pady=20)

#colocando um campo para digitação
entrada = ctk.CTkEntry(
    janela,
    placeholder_text= "Digite o seu nome" #dicazinha que fica cinzinha atrás e sai quando digita
)

entrada.pack(pady=20)

def mostrar_nome():
    nome = entrada.get()
    print(nome)

#colocando um botão
botao = ctk.CTkButton(
     janela,
     text= "clique para mostrar o nome",
     command=mostrar_nome
 )

botao.pack(pady=20)

#executar
janela.mainloop()

print("Olá interface")




#Utilizando frames
janela2 =ctk.CTk()
janela2.geometry("600x400")

frame_topo = ctk.CTkFrame(janela2)
frame_topo.pack(fill="x", pady=10)

frame_conteudo = ctk.CTkFrame(janela2)
frame_conteudo.pack(expand =True, fill="both", padx=10, pady=10) #pad é o quanto deixa de distancia de borda

label1 = ctk.CTkLabel(frame_topo, text="MENU")
label1.pack(pady=10)

label2 = ctk.CTkLabel(frame_conteudo, text="CONTEUDO")
label2.pack(pady=20)

janela2.mainloop()  



#Utilzando grid
janela4 = ctk.CTk()
janela4.geometry("400x300")

label_nome = ctk.CTkLabel(janela4, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

entrada_nome = ctk.CTkEntry(janela4)
entrada_nome.grid(row=0, column=1)

label_idade = ctk.CTkLabel(janela4, text="Idade")
label_idade.grid(row=1, column=0, padx=10, pady=10)

entrada_idade = ctk.CTkEntry(janela4)
entrada_idade.grid(row=1, column=1)

janela4.mainloop()



#utilizando checkbox
janela3 = ctk.CTk()
janela3.geometry("400x250")

#vairável que vai controlar o estado do checkbox
variavel = ctk.BooleanVar()

checkbox = ctk.CTkCheckBox(
    janela3,
    text="Aceito os termos",
    variable=variavel
)

def verificar():
    #.get em uma variável boobleana retorna true se marcado e falso se desmarcado
    if variavel.get():
        print("Checkbox marcado")
    else:
        print("checkbox desmarcado") 


checkbox.pack(pady=20)

#botão para testar
btn = ctk.CTkButton(janela3, text="Verificar", command=verificar)
btn.pack(pady = 5)

janela3.mainloop()

#para jogar instale a biblioteca turtle
# para instalar a biblioteca digite: pip install PythonTurtle

import turtle
import random

t=turtle.Turtle()
s=turtle.Screen()

#velocidade de criação do #
t.speed(10)#2° mais rapido possivel

#cor do #
t.shape("blank")

#titulo da pagina
turtle.title("Jogo da velha")

#criando o #
turtle.bgcolor("#f7e9de")
t.pencolor("#3f0013")

t.goto(0,0)
t.forward(150)
t.backward(300) 
t.forward(100)
t.right(90)
t.backward(100)
t.forward(300)
t.backward(100)
t.left(90)
t.backward(100)
t.forward(300)
t.backward(100)
t.left(90)
t.backward(100)
t.forward(300)
t.penup()

#titulo explicativo
t.goto(0,250)
t.write("JOGO DA VELHA", align="center", font=("Times New Roman",20, "normal"))
t.goto(0,230)
t.write("Escolha uma jogada de acordo com as seguintes posições:", align="center", font=("Times New Roman",10, "normal"))
t.goto(0,140)
t.write(" 1 | 2 | 3  \n _______ \n 4 | 5 | 6  \n _______ \n 7 | 8 | 9", align="center", font=("Arial",10, "normal"))

#JOGO

#matriz que servirá para acompanhar o andamento do jogo
matriz_jogo=[[0,0,0],
             [0,0,0],
             [0,0,0]]

#lista com as jogadas disponiveis
disponiveis=[1,2,3,4,5,6,7,8,9]


#função para imprimir a jogada de um player
def jogador_A():
    
    jogada=turtle.textinput("Vez do jogador X", "Qual sua jogada? digite um numero de 1 a 9")
    jogada=int(jogada)

    while 1>jogada or jogada>9:
        jogada=turtle.textinput("Número inválido", "Digite um numero de 1 a 9")
        jogada=int(jogada)

    if jogada not in disponiveis:
        jogada=turtle.textinput("Número repetido", "Digite outro numero de 1 a 9")
        jogada=int(jogada)

    if jogada<=3:
        matriz_jogo[0][jogada-1]=2
        if jogada==1:
            t.goto(-130,20)
            disponiveis.remove(jogada)
        elif jogada==2:
            t.goto(-30,20)
            disponiveis.remove(jogada)
        elif jogada==3:
            t.goto(70,20)
            disponiveis.remove(jogada)

    elif 4<=jogada<=6:
        matriz_jogo[1][jogada-4]=2
        if jogada==4:
            t.goto(-130,-80)
            disponiveis.remove(jogada)
        elif jogada==5:
            t.goto(-30,-80)
            disponiveis.remove(jogada)
        elif jogada==6:
            t.goto(70,-80)
            disponiveis.remove(jogada)

    elif 7<=jogada<=9:
        matriz_jogo[2][jogada-7]=2
        if jogada==7:
            t.goto(-130,-180)
            disponiveis.remove(jogada)
        elif jogada==8:
            t.goto(-30,-180)
            disponiveis.remove(jogada)
        elif jogada==9:
            t.goto(70,-180)
            disponiveis.remove(jogada)
    
    #desenhar o "X"
    t.pencolor("#ea785b")
    t.pensize(5)
    t.pendown()
    t.right(45)
    t.forward(84)
    t.penup()
    t.left(45)
    t.backward(60)
    t.left(45)
    t.pendown()
    t.forward(84)
    t.right(45)
    t.penup()
    t.goto(0,-50)

    
def jogador_B():
    
    jogada=turtle.textinput("Vez do jogador O", "Qual sua jogada? digite um numero de 1 a 9")
    jogada=int(jogada)

    while 1>jogada or jogada>9:
        jogada=turtle.textinput("Número inválido", "Digite um numero de 1 a 9")
        jogada=int(jogada)

    if jogada not in disponiveis:
        jogada=turtle.textinput("Número repetido", "Digite outro numero de 1 a 9")
        jogada=int(jogada)

    if jogada<=3:
        matriz_jogo[0][jogada-1]=1
        if jogada==1:
            t.goto(-100,20)
            disponiveis.remove(jogada)
        elif jogada==2:
            t.goto(0,20)
            disponiveis.remove(jogada)
        elif jogada==3:
            t.goto(100,20)
            disponiveis.remove(jogada)

    elif 4<=jogada<=6:
        matriz_jogo[1][jogada-4]=1
        if jogada==4:
            t.goto(-100,-80)
            disponiveis.remove(jogada)
        elif jogada==5:
            t.goto(0,-80)
            disponiveis.remove(jogada)
        elif jogada==6:
            t.goto(100,-80)
            disponiveis.remove(jogada)

    elif 7<=jogada<=9:
        matriz_jogo[2][jogada-7]=1
        if jogada==7:
            t.goto(-100,-180)
            disponiveis.remove(jogada)
        elif jogada==8:
            t.goto(0,-180)
            disponiveis.remove(jogada)
        elif jogada==9:
            t.goto(100,-180)
            disponiveis.remove(jogada)

    #desenhar a "O"
    t.pencolor("#a1a8be")
    t.speed(10)
    t.pensize(5)
    t.pendown()
    t.right(90)
    t.circle(30)
    t.penup()
    t.left(90)
    
def verificarVitoria():
        vitoria=False
        #linha fechada    
        if matriz_jogo[0][0]==matriz_jogo[0][1] and matriz_jogo[0][0]==matriz_jogo[0][2] and matriz_jogo[0][0]!=0:
            vitoria=True
        elif matriz_jogo[1][0]==matriz_jogo[1][1] and matriz_jogo[1][0]==matriz_jogo[1][2] and matriz_jogo[1][0]!=0:
            vitoria=True
        elif matriz_jogo[2][0]==matriz_jogo[2][1] and matriz_jogo[2][0]==matriz_jogo[2][2] and matriz_jogo[2][0]!=0:
            vitoria=True

        #coluna fechada
        elif matriz_jogo[0][0]==matriz_jogo[1][0] and matriz_jogo[0][0]==matriz_jogo[2][0] and matriz_jogo[0][0]!=0:
            vitoria=True
        elif matriz_jogo[0][1]==matriz_jogo[1][1] and matriz_jogo[0][1]==matriz_jogo[2][1] and matriz_jogo[0][1]!=0:
            vitoria=True
        elif matriz_jogo[0][2]==matriz_jogo[1][2] and matriz_jogo[0][2]==matriz_jogo[2][2] and matriz_jogo[0][2]!=0:
            vitoria=True
            
        #diagonal principal fechada
        elif matriz_jogo[0][0]==matriz_jogo[1][1] and matriz_jogo[0][0]==matriz_jogo[2][2] and matriz_jogo[0][0]!=0:
            vitoria=True
            
        #diagonal secundaria
        elif matriz_jogo[2][0]==matriz_jogo[1][1] and matriz_jogo[2][0]==matriz_jogo[0][2] and matriz_jogo[2][0]!=0:
            vitoria=True
        
        return vitoria

while True:
    jogador_A()
    
    #conferindo vitoria após jogada do jogador X
    vencedorA=verificarVitoria()
    if vencedorA==True:
        t.goto(0,105)
        t.write("JOGADOR X VENCEU", align="center", font=("Times New Roman",15, "normal"))
        break
    
    #Caso de dar empate
    if len(disponiveis)==0:
        t.goto(0,105)
        t.pencolor("#3f0013")
        t.write("DEU VELHA",align="center", font=("Times New Roman",15, "normal"))
        break

    jogador_B()    
    #conferindo vitoria após jogada do jogador O
    vencedorB=verificarVitoria()
    if vencedorB==True:
        t.goto(0,105)
        t.write("JOGADOR O VENCEU", align="center", font=("Times New Roman",15, "normal"))
        break
    

turtle.mainloop()

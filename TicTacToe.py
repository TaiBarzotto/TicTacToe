import turtle
import random


t=turtle.Turtle()
#velocidade de criação do #
t.speed(10)#2° mais rapido possivel

#cor do #
t.shape("blank")

#titulo da pagina
turtle.title("Jogo da velha")
#criando o #
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
t.write("JOGO DA VELHA", align="center", font=("Verdana",20, "normal"))
t.goto(0,230)
t.write("Escolha uma jogada de acordo com as seguintes posições:", align="center", font=("Verdana",10, "normal"))
t.goto(0,140)
t.write(" 1 | 2 | 3  \n ________ \n 4 | 5 | 6  \n ________ \n 7 | 8 | 9", align="center", font=("Verdana",10, "normal"))
#jogo em si

#matriz que servirá para acompanhar o andamento do jogo
matriz_jogo=[[0,0,0],
             [0,0,0],
             [0,0,0]]

#lista de jogadas disponiveis
disponiveis=[1,2,3,4,5,6,7,8,9]


#função para imprimir a jogada de um player
def jogador():
    
    jogada=turtle.textinput("Sua vez", "Qual sua jogada? digite um numero de 1 a 9")
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

    t.pencolor("red")
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

    
                


def maquina():

    idx=random.randint(0,(len(disponiveis)-1))
    place=disponiveis[idx]

    if place<=3:
        matriz_jogo[0][place-1]=1
        if place==1:
            t.goto(-100,20)
            disponiveis.remove(place)
        elif place==2:
            t.goto(0,20)
            disponiveis.remove(place)
        elif place==3:
            t.goto(100,20)
            disponiveis.remove(place)

    elif 4<=place<=6:
        matriz_jogo[1][place-4]=1
        if place==4:
            t.goto(-100,-80)
            disponiveis.remove(place)
        elif place==5:
            t.goto(0,-80)
            disponiveis.remove(place)
        elif place==6:
            t.goto(100,-80)
            disponiveis.remove(place)

    elif 7<=place<=9:
        matriz_jogo[2][place-7]=1
        if place==7:
            t.goto(-100,-180)
            disponiveis.remove(place)
        elif place==8:
            t.goto(0,-180)
            disponiveis.remove(place)
        elif place==9:
            t.goto(100,-180)
            disponiveis.remove(place)
    
    t.pencolor("blue")
    t.pensize(5)
    t.pendown()
    t.right(90)
    t.circle(30)
    t.penup()
    t.left(90)
    



while len(disponiveis)>0 or vitoria==False:
    vitoria=False 
    jogador()

    print(disponiveis)
    print(matriz_jogo)
    #conferindo vitoria
    if len(disponiveis)<=4: #checando a partir da terceira rodada, ja foram 3 jogadas do player e duas da maquina
        #linha fechada
        for i in range(3):
            for j in range(1):
                if matriz_jogo[i][j]==matriz_jogo[i][j+1] and matriz_jogo[i][j]==matriz_jogo[i][2+j]:
                    vitoria=True
        
        #coluna fechada
        for j in range(3):
            for i in range(1):
                if matriz_jogo[i][j]==matriz_jogo[i+1][j] and matriz_jogo[i][j]==matriz_jogo[i+2][j]:
                    vitoria=True
            
        #diagonal principal fechada
        i=0
        j=0
        if matriz_jogo[i][j]==matriz_jogo[i+1][j+1] and matriz_jogo[i][j]==matriz_jogo[i+2][j+2]:
            vitoria=True
            
        #diagonal secundaria
        i=0
        j=0
        if matriz_jogo[i+2][j]==matriz_jogo[i+1][j+1] and matriz_jogo[i+2][j]==matriz_jogo[i][j+2]:
            vitoria=True

    if vitoria==True:
        t.goto(-10,0)

        t.write("VOCÊ VENCEU", align="center", font=("Verdana",15, "normal"))

        break

    o=maquina()    
    #conferindo vitoria
    if len(disponiveis)<=4: #checando a partir da terceira rodada, ja foram 3 jogadas do player e duas da maquina
        #linha fechada
        for i in range(3):
            for j in range(1):
                if matriz_jogo[i][j]==matriz_jogo[i][j+1] and matriz_jogo[i][j]==matriz_jogo[i][2+j]:
                    vitoria=True
        
        #coluna fechada
        for j in range(3):
            for i in range(1):
                if matriz_jogo[i][j]==matriz_jogo[i+1][j] and matriz_jogo[i][j]==matriz_jogo[i+2][j]:
                    vitoria=True
            
        #diagonal principal fechada
        i=0
        j=0
        if matriz_jogo[i][j]==matriz_jogo[i+1][j+1] and matriz_jogo[i][j]==matriz_jogo[i+2][j+2]:
            vitoria=True
            
        #diagonal secundaria
        i=0
        j=0
        if matriz_jogo[i+2][j]==matriz_jogo[i+1][j+1] and matriz_jogo[i+2][j]==matriz_jogo[i][j+2]:
            vitoria=True

    if vitoria==True:
        t.goto(0,0)
        t.write("VOCÊ PERDEU",align="center", font=("Verdana",15, "normal"))
        break

turtle.mainloop()

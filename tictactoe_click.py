import turtle
import random

t=turtle.Screen()
#velocidade de criação do #
turtle.speed(10)#2° mais rapido possivel

#cor do #
#turtle.shape("blank")

#criando o #
turtle.forward(150)
turtle.backward(300) 
turtle.forward(100)
turtle.right(90)
turtle.backward(100)
turtle.forward(300)
turtle.backward(100)
turtle.left(90)
turtle.backward(100)
turtle.forward(300)
turtle.backward(100)
turtle.left(90)
turtle.backward(100)
turtle.forward(300)
turtle.penup()
#jogo em si

#matriz que servirá para acompanhar o andamento do jogo
matriz_jogo=[[0,0,0],
             [0,0,0],
             [0,0,0]]

#lista de jogadas disponiveis
disponiveis=[1,2,3,4,5,6,7,8,9]


  
# method to perform action 
  
  
# onclick action  



#função para imprimir a jogada de um player
def jogador(x,y):
    turtle.goto(x, y)
    turtle.write(str(x)+","+str(y)) 
    if y>0:
        if x<-50:
            turtle.goto(-130,20)
            matriz_jogo[0][0]=2
            disponiveis.remove(1)
        elif x>-50 and x<50:
            turtle.goto(-30,20)
            matriz_jogo[0][1]=2
            disponiveis.remove(2)
        elif x>50:
            turtle.goto(70,20)
            matriz_jogo[0][2]=2
            disponiveis.remove(3)

    elif y<0 and y>-100:
        if x<-50:
            turtle.goto(-130,-80)
            matriz_jogo[1][0]=2
            disponiveis.remove(4)
        elif x>-50 and x<50:
            turtle.goto(-30,-80)
            matriz_jogo[1][1]=2
            disponiveis.remove(5)
        elif x>50:
            turtle.goto(70,-80)
            matriz_jogo[1][2]=2
            disponiveis.remove(6)

    elif y<-100:
        if x<-50:
            turtle.goto(-130,-180)
            matriz_jogo[2][0]=2
            disponiveis.remove(7)
        elif x>-50 and x<50:
            turtle.goto(-30,-180)
            matriz_jogo[2][1]=2
            disponiveis.remove(8)
        elif x>50:
            turtle.goto(70,-180)
            matriz_jogo[2][2]=2
            disponiveis.remove(9)

    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(84)
    turtle.penup()
    turtle.left(45)
    turtle.backward(60)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(84)
    turtle.right(45)
    turtle.penup()
    turtle.goto(0,-50)


             
def maquina():

    idx=random.randint(0,(len(disponiveis)-1))
    place=disponiveis[idx]

    if place<=3:
        matriz_jogo[0][place-1]=1
        if place==1:
            turtle.goto(-100,20)
            disponiveis.remove(place)
        elif place==2:
            turtle.goto(0,20)
            disponiveis.remove(place)
        elif place==3:
            turtle.goto(100,20)
            disponiveis.remove(place)

    elif 4<=place<=6:
        matriz_jogo[1][place-4]=1
        if place==4:
            turtle.goto(-100,-80)
            disponiveis.remove(place)
        elif place==5:
            turtle.goto(0,-80)
            disponiveis.remove(place)
        elif place==6:
            turtle.goto(100,-80)
            disponiveis.remove(place)

    elif 7<=place<=9:
        matriz_jogo[2][place-7]=1
        if place==7:
            turtle.goto(-100,-180)
            disponiveis.remove(place)
        elif place==8:
            turtle.goto(0,-180)
            disponiveis.remove(place)
        elif place==9:
            turtle.goto(100,-180)
            disponiveis.remove(place)
    
    turtle.pencolor("blue")
    turtle.pensize(5)
    turtle.pendown()
    turtle.right(90)
    turtle.circle(30)
    turtle.penup()
    turtle.left(90)
    


t.onclick(jogador)

'''
while len(disponiveis)>0 or vitoria==False:
    vitoria=False 
   

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
        turtle.goto(-10,0)

        turtle.write("VOCÊ VENCEU", font=("Verdana",15, "normal"))

        break

    #o=maquina()    
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
        turtle.goto(0,0)
        turtle.write("VOCÊ PERDEU", font=("Verdana",15, "normal"))
        break
'''
turtle.mainloop()

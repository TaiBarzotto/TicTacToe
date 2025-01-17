import turtle

# Configuração inicial
t = turtle.Turtle()
s = turtle.Screen()
s.title("Jogo da Velha")
s.bgcolor("#f7e9de")
t.speed(1000)
t.penup()
t.hideturtle()

# Desenhar o tabuleiro
def desenhar_tabuleiro():
    t.pencolor("#3f0013")
    t.pensize(1)
    t.clear()  # Limpa a tela antes de desenhar o tabuleiro
    t.goto(0,0)
    t.setheading(0)
    t.pendown()
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

# Variáveis do jogo
matriz_jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogador_atual = "X"
game_active = True

# Função para desenhar X
def desenha_X(pos):
    global ocupado
    ocupado = True
    t.goto(pos)
    t.pendown()
    t.pencolor("#ea785b")
    t.pensize(5)
    t.setheading(45)
    t.forward(60)
    t.backward(120)
    t.forward(60)
    t.setheading(-45)
    t.forward(60)
    t.backward(120)
    t.penup()
    ocupado = False

# Função para desenhar O
def desenha_O(pos):
    global ocupado
    ocupado = True
    pos = pos[0] - 30, pos[1] - 30
    t.goto(pos)
    t.pendown()
    t.pencolor("#a1a8be")
    t.pensize(5)
    t.circle(43)
    t.penup()
    ocupado = False

# Função para verificar vitória
def verificar_vitoria():
    for i in range(3):
        if matriz_jogo[i][0] == matriz_jogo[i][1] == matriz_jogo[i][2] != 0:
            return True
        if matriz_jogo[0][i] == matriz_jogo[1][i] == matriz_jogo[2][i] != 0:
            return True
    if matriz_jogo[0][0] == matriz_jogo[1][1] == matriz_jogo[2][2] != 0:
        return True
    if matriz_jogo[0][2] == matriz_jogo[1][1] == matriz_jogo[2][0] != 0:
        return True
    return False

# Função para lidar com cliques
def clique(x, y):
    global jogador_atual, game_active

    if not game_active:
        print("BB")
        s.onscreenclick(restart_game)
        start_game()
        return

    pos = None
    jogada = None

    # Determinar a posição clicada
    if -150 < x < -50 and 0 < y < 100:  # Posição 1
        pos = [-100, 50]
        jogada = 1
    elif -50 < x < 50 and 0 < y < 100:  # Posição 2
        pos = [0, 50]
        jogada = 2
    elif 50 < x < 150 and 0 < y < 100:  # Posição 3
        pos = [100, 50]
        jogada = 3
    elif -150 < x < -50 and -100 < y < 0:  # Posição 4
        pos = [-100, -50]
        jogada = 4
    elif -50 < x < 50 and -100 < y < 0:  # Posição 5
        pos = [0, -50]
        jogada = 5
    elif 50 < x < 150 and -100 < y < 0:  # Posição 6
        pos = [100, -50]
        jogada = 6
    elif -150 < x < -50 and -200 < y < -100:  # Posição 7
        pos = [-100, -150]
        jogada = 7
    elif -50 < x < 50 and -200 < y < -100:  # Posição 8
        pos = [0, -150]
        jogada = 8
    elif 50 < x < 150 and -200 < y < -100:  # Posição 9
        pos = [100, -150]
        jogada = 9

    # Verificar se a jogada é válida
    if jogada in disponiveis:
        disponiveis.remove(jogada)
        if jogador_atual == "X":
            matriz_jogo[(jogada - 1) // 3][(jogada - 1) % 3] = 1
            desenha_X(pos)
            if verificar_vitoria():
                t.goto(0, 200)
                t.write("JOGADOR X VENCEU!", align="center", font=("Times New Roman", 15, "normal"))
                game_active = False
                return
            jogador_atual = "O"
        else:
            matriz_jogo[(jogada - 1) // 3][(jogada - 1) % 3] = 2
            desenha_O(pos)
            if verificar_vitoria():
                t.goto(0, 200)
                t.write("JOGADOR O VENCEU!", align="center", font=("Times New Roman", 15, "normal"))
                game_active = False
                return
            jogador_atual = "X"

    # Verificar empate
    if not disponiveis:
        t.goto(0, 200)
        t.write("DEU VELHA!", align="center", font=("Times New Roman", 15, "normal"))
        game_active = False
        return
    

def draw_buttons():
    t.setheading(0)
    # Draw Restart Button
    t.penup()
    t.pensize(0.5)
    t.color("white")
    t.goto(-125, -250)
    t.pendown()
    t.fillcolor("#a1a8be")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(-70, -280)
    t.pendown()
    t.write("Restart", align="center", font=("Arial", 16, "normal"))

    # Draw Quit Button
    t.penup()
    t.goto(25, -250)
    t.pendown()
    t.fillcolor("#ea785b")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(75, -280)
    t.pendown()
    t.write("Quit", align="center", font=("Arial", 16, "normal"))
    t.hideturtle()

def restart_game(x, y):
    global game_active

    if -150 < x < -50 and -290 < y < -250:
        global matriz_jogo, disponiveis, jogador_atual
        matriz_jogo = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Reinicia a matriz do jogo
        disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Reinicia as jogadas disponíveis
        jogador_atual = "X"  # Reinicia o jogador atual
        t.clear()  # Limpa a tela
        game_active = True
        t.goto(0,0)

        start_game()  # Desenha o tabuleiro novamente
       

    if 25 < x < 125 and -290 < y < -250:
        turtle.bye()   
    
def start_game():
    if game_active:
        desenhar_tabuleiro()
        s.onscreenclick(clique)
    else:
        t.penup()
        t.goto(0, 0)
        t.pendown()
        draw_buttons()
        s.onscreenclick(restart_game)

    t.hideturtle()

# Initialize the game
start_game()
turtle.done()

# Ian Lucca Soares Mesquita ---211045140

import pyxel
from random import   randrange

nome= input("digite seu nome : ")

#dificuldade=input("digite uma dificuldade desejada: ")

# Constantes
W_SCREEN = 180
H_SCREEN = 140
FPS = 30

## Variáveis ##

# Nave
x = 85
y = 100
v_nave = 1.5
wn=10
hn=10
# Meteoros
y_m = [-10,-25,-38,-50,-10]
x_m = [10, 30, 60, 120, 130]
N_METEORS = len(y_m)
v_meteoro = [1.75, 1.5 ,2, 1.5, 1.65]
r = 5

#embaralha a posição dos meteoros
for i in range(10, W_SCREEN-20):
    if i % 15 == 0:
        x_m.append(i)

# Condição do jogo
game_over = False
escrito=False

#Condição de vitória
victory=False
#shield = 300
#score
score = 0

#coloca no arquivo do leaderboard sua pontuação
def write_record(score,nome):
    global escrito
    if escrito:
        return
    linha=f"{score} , {nome} \n"
    with open ("record.txt", "a") as arquivo:
        arquivo.write(linha)
        escrito=True
        
def update():
    global x, y, x_m, y_m, score,v_meteoro,game_over,victory,escrito  #,dificuldade,shield

    #trava o jogo quando da game over ou victory e quando apertar espaço reinicia o jogo
    if game_over and pyxel.btn(pyxel.KEY_SPACE):
        # Reinicia o jogo
        y = 100
        x=85
        v_meteoro=[1.75, 1.5 ,2, 1.5, 1.65]
        game_over = False
        y_m = [-10,-25,-38,-50,-10]
        x_m = [10, 30, 60, 120, 130]
        score = 0
        escrito=False


    elif game_over:
        write_record(nome, score )   
        return

    if victory:
        return

    # Movimentação da nave
    if pyxel.btn(pyxel.KEY_W):
        y -= v_nave
    elif pyxel.btn(pyxel.KEY_S):
        y += v_nave
    if pyxel.btn(pyxel.KEY_A):
        x -= v_nave
    elif pyxel.btn(pyxel.KEY_D):
        
        x += v_nave

    # Movimentação dos meteoros
    for i in range(N_METEORS):
        y_m[i] += v_meteoro[i]

    #aumenta a dificuldade 
    if score % 10 == 0:      
        v_meteoro[i]+=0.15


#implementa o score
    for i in range (N_METEORS):      
        if y_m[i] > H_SCREEN:
            score+=1

#recicla os meteoros / volta eles
    for j in range(N_METEORS):
        if y_m[j] > H_SCREEN :
            x_m[j] = randrange(W_SCREEN)
            y_m[j] = -10

#verifica colisão
    for i in range(int(x), int(x + wn)):
        for j in range(int(y), int(y + wn)):
            if pyxel.pget(i,j)== pyxel.COLOR_GRAY:
                game_over=True

#Trava o jogo se a nave sair da tela
    if x==W_SCREEN+wn:
        game_over=True
    if x <0-wn:
        game_over=True
    if y >H_SCREEN+hn:
        game_over=True
    if y <0-hn:
        game_over=True

#Da a condição de vitória:
    if score==120:
        victory=True

###############################
    # if score == int(dificuldade):
    #   victory=True
################################
#   for t in range int(x), int(x+ws)
#       for p in range int(y),int(y+ws):
#         if pyxel.pget(t,p)==((pyxel.frame_count//5)%16):
#              shield-=0.25
######################################

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)

    # Nave
    pyxel.rect(x, y, wn, hn, pyxel.COLOR_WHITE)

    # Meteoros
    for i in range(len(y_m)):
        pyxel.circ(x_m[i], y_m[i], r, pyxel.COLOR_GRAY)

#desenha o score
    pyxel.text(140,5,f" score:{score}",pyxel.COLOR_WHITE)

#desenha a borda 
    pyxel.rectb(0,0,W_SCREEN,H_SCREEN,(pyxel.frame_count//5)%16)



#desenha game over
    if game_over:
        pyxel.rect(18, 27, 74, 15, (pyxel.frame_count // 5) % 16)
        pyxel.text(23, 31, f"GAME OVER! {nome}", pyxel.COLOR_BLACK)
        pyxel.text(22, 30, f"GAME OVER! {nome}", pyxel.COLOR_WHITE)
#desenha a Vitória
    if victory:
        pyxel.rect(18, 27, 70, 15, (pyxel.frame_count // 5) % 16)
        pyxel.text(23, 31, f"PaRaBeNS!! {nome}", pyxel.COLOR_BLACK)
        pyxel.text(22, 30, f"PaRaBeNS!! {nome}", pyxel.COLOR_WHITE)

pyxel.init(W_SCREEN, H_SCREEN,title="Meteor Evade",  fps=FPS)
pyxel.mouse(True)
pyxel.run(update, draw)
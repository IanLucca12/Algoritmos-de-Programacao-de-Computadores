import pyxel
from random import randint
pyxel.init(256, 256,fps = 30)
x= 100
y=100
s= 0
t = 0
z= 3
j = 3
p=0
def update():
    global z , t , x , y ,s, j, p
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


    if pyxel.btn(pyxel.KEY_W) and y - 3 > -1:
        y-=j
        
    if pyxel.btn(pyxel.KEY_S) and y + 3 < 257:
        y+=j
    if pyxel.btn(pyxel.KEY_D) and x + 3 <257:
        x+=j
    if pyxel.btn(pyxel.KEY_A) and x - 3 > -1:
        x-=j
    s += 1 
    if s == 30 :
        z = randint(0,1)
        s= 0
    if z == 0 :
        t = 5
        j =1
        
        p-=0.05
    else :
        t = 8
        j =3 
        p+=0.05

def draw():
    pyxel.cls(0)
    pyxel.rect(10, 10, 20, 20, t)
    pyxel.rect(x, y, 20, 20, t)
    pyxel.text (200, 200, "status: {:.1f}".format(p), pyxel.COLOR_WHITE) 

pyxel.run(update, draw)
import pyxel
x=20
y=10
p=0
time = 1
def update():
    global x,y,p
    if pyxel.btnp(pyxel.KEY_SPACE, 0,500):
        if p ==0 :
            y+=10
        p=30
    if p>0 :
        p-=1    
        
        
    
    
    if pyxel.btnp(pyxel.KEY_D):
        x+=10
def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    pyxel.rect(x, y, 12, 12, pyxel.COLOR_GREEN)
    

pyxel.init(120, 120,title="Meteor Evade",fps=30)
pyxel.mouse(True)
pyxel.run(update, draw)
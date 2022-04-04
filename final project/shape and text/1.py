import pygame as pg
from random import randint

pg.init()
win = pg.display.set_mode((800,500))
flag = True
rang = (randint(0,255),randint(0,255),randint(0,255))
shoaa = randint(10,100)
x_markaz = randint(100,700)
y_markaz = randint(100,400)
soraat1 = 1000
soraat2 = randint(1,50)
print(rang,shoaa,(x_markaz,y_markaz))
while flag:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
    x_markaz += soraat1
    y_markaz += soraat2
    if x_markaz < shoaa or x_markaz+shoaa > 800:
        soraat1 *= -1
    if y_markaz < shoaa or y_markaz+shoaa > 500:
        soraat2 *= -1
    win.fill((0,0,0))
    pg.draw.circle(win, rang, (x_markaz,y_markaz), shoaa)
    pg.display.update()
    pg.time.Clock().tick(30)
import pygame as pg
from random import randint

pg.init()
n = int(input())
win = pg.display.set_mode((800,500))
flag = True
rang = []
shoaa = []
x_markaz = []
y_markaz = []
soraat1 = []
soraat2 = []

for i in range(n):
    rang.append((randint(0,255),randint(0,255),randint(0,255)))
    shoaa.append(randint(10,100))
    x_markaz.append(randint(100,700))
    y_markaz.append(randint(100,400))
    soraat1.append(randint(1,50))
    soraat2.append(randint(1,50))

while flag:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
    for i in range(n):
        pg.draw.circle(win, rang[i], (x_markaz[i],y_markaz[i]), shoaa[i])
        x_markaz[i] += soraat1[i]
        y_markaz[i] += soraat2[i]
        if x_markaz[i] < shoaa[i] or x_markaz[i]+shoaa[i] > 800:
            soraat1[i] *= -1
        if y_markaz[i] < shoaa[i] or y_markaz[i]+shoaa[i] > 500:
            soraat2[i] *= -1
    pg.display.update()
    pg.time.Clock().tick(30)
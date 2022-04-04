import pygame as pg
from random import randint as r

pg.init()
win = pg.display.set_mode((1200,700))
flag = True
rang=[(r(0,255), r(0,255), r(0,255)),
    (r(0,255), r(0,255), r(0,255)),
    (r(0,255), r(0,255), r(0,255)),
    (r(0,255), r(0,255), r(0,255)),
    (r(0,255), r(0,255), r(0,255))]
shoaa = [r(10,50), r(10,50), r(10,50), r(10,50), r(10,50)]
x_markaz = [r(100,1100), r(100,1100), r(100,1100), r(100,1100), r(100,1100)]
y_markaz = [r(100,700), r(100,700), r(100,700), r(100,700), r(100,700)]
soraat1 = [r(5,15), r(5,30), r(5,30), r(5,30), r(5,30)]
soraat2 = [r(5,15), r(5,30), r(5,30), r(5,30), r(5,30)]

while flag:
    win.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            flag = False
    pg.draw.circle(win, rang[0], (x_markaz[0],y_markaz[0]), shoaa[0])
    pg.draw.circle(win, rang[1], (x_markaz[1],y_markaz[1]), shoaa[1])
    pg.draw.circle(win, rang[2], (x_markaz[2],y_markaz[2]), shoaa[2])
    pg.draw.circle(win, rang[3], (x_markaz[3],y_markaz[3]), shoaa[3])
    pg.draw.circle(win, rang[4], (x_markaz[4],y_markaz[4]), shoaa[4])
    x_markaz[0] += soraat1[0]
    y_markaz[0] += soraat2[0]
    x_markaz[1] += soraat1[1]
    y_markaz[1] += soraat2[1]
    x_markaz[2] += soraat1[2]
    y_markaz[2] += soraat2[2]
    x_markaz[3] += soraat1[3]
    y_markaz[3] += soraat2[3]
    x_markaz[4] += soraat1[4]
    y_markaz[4] += soraat2[4]
    if x_markaz[0] < shoaa[0] or x_markaz[0]+shoaa[0] > 1200:
        soraat1[0] *= -1
    if y_markaz[0] < shoaa[0] or y_markaz[0]+shoaa[0] > 700:
        soraat2[0] *= -1
    if x_markaz[1] < shoaa[1] or x_markaz[1]+shoaa[1] > 1200:
        soraat1[1] *= -1
    if y_markaz[1] < shoaa[1] or y_markaz[1]+shoaa[1] > 700:
        soraat2[1] *= -1
    if x_markaz[2] < shoaa[2] or x_markaz[2]+shoaa[2] > 1200:
        soraat1[2] *= -1
    if y_markaz[2] < shoaa[2] or y_markaz[2]+shoaa[2] > 700:
        soraat2[2] *= -1
    if x_markaz[3] < shoaa[3] or x_markaz[3]+shoaa[3] > 1200:
        soraat1[3] *= -1
    if y_markaz[3] < shoaa[3] or y_markaz[3]+shoaa[3] > 700:
        soraat2[3] *= -1
    if x_markaz[4] < shoaa[4] or x_markaz[4]+shoaa[4] > 1200:
        soraat1[4] *= -1
    if y_markaz[4] < shoaa[4] or y_markaz[4]+shoaa[4] > 700:
        soraat2[4] *= -1
    
    if ((y_markaz[0]-y_markaz[1])**2+(x_markaz[0]-x_markaz[1])**2)**0.5<shoaa[0]+shoaa[1]:
        soraat1[0],soraat1[1],soraat2[0],soraat2[1]=soraat1[1],soraat1[0],soraat2[1],soraat2[0]

    if ((y_markaz[0]-y_markaz[2])**2+(x_markaz[0]-x_markaz[2])**2)**0.5<shoaa[0]+shoaa[2]:
        soraat1[0],soraat1[2],soraat2[0],soraat2[2]=soraat1[2],soraat1[0],soraat2[2],soraat2[0]
    
    if ((y_markaz[0]-y_markaz[3])**2+(x_markaz[0]-x_markaz[3])**2)**0.5<shoaa[0]+shoaa[3]:
        soraat1[0],soraat1[3],soraat2[0],soraat2[3]=soraat1[3],soraat1[0],soraat2[3],soraat2[0]
    
    if ((y_markaz[0]-y_markaz[4])**2+(x_markaz[0]-x_markaz[4])**2)**0.5<shoaa[0]+shoaa[4]:
        soraat1[0],soraat1[4],soraat2[0],soraat2[4]=soraat1[4],soraat1[0],soraat2[4],soraat2[0]

    if ((y_markaz[2]-y_markaz[1])**2+(x_markaz[2]-x_markaz[1])**2)**0.5<shoaa[2]+shoaa[1]:
        soraat1[2],soraat1[1],soraat2[2],soraat2[1]=soraat1[1],soraat1[2],soraat2[1],soraat2[2]

    if ((y_markaz[1]-y_markaz[3])**2+(x_markaz[1]-x_markaz[3])**2)**0.5<shoaa[1]+shoaa[3]:
        soraat1[1],soraat1[3],soraat2[1],soraat2[3]=soraat1[3],soraat1[1],soraat2[3],soraat2[1]

    if ((y_markaz[1]-y_markaz[4])**2+(x_markaz[1]-x_markaz[4])**2)**0.5<shoaa[1]+shoaa[4]:
        soraat1[1],soraat1[4],soraat2[1],soraat2[4]=soraat1[4],soraat1[1],soraat2[4],soraat2[1]

    if ((y_markaz[2]-y_markaz[3])**2+(x_markaz[2]-x_markaz[3])**2)**0.5<shoaa[2]+shoaa[3]:
        soraat1[2],soraat1[3],soraat2[2],soraat2[3]=soraat1[3],soraat1[2],soraat2[3],soraat2[2]

    if ((y_markaz[2]-y_markaz[4])**2+(x_markaz[2]-x_markaz[4])**2)**0.5<shoaa[2]+shoaa[4]:
        soraat1[2],soraat1[4],soraat2[2],soraat2[4]=soraat1[4],soraat1[2],soraat2[4],soraat2[2]

    if ((y_markaz[3]-y_markaz[4])**2+(x_markaz[3]-x_markaz[4])**2)**0.5<shoaa[3]+shoaa[4]:
        soraat1[3],soraat1[4],soraat2[3],soraat2[4]=soraat1[4],soraat1[3],soraat2[4],soraat2[3]
        
    if x_markaz[0] < shoaa[0]:
        x_markaz[0] = shoaa[0]
    if x_markaz[0]+shoaa[0] > 1200:
        x_markaz[0] = 1200-shoaa[0]
    if y_markaz[0] < shoaa[0]:
        y_markaz[0] = shoaa[0]
    if y_markaz[0]+shoaa[0] > 700:
        y_markaz[0] = 700-shoaa[0]
    if x_markaz[1] < shoaa[1]:
        x_markaz[1] = shoaa[1]
    if x_markaz[1]+shoaa[1] > 1200:
        x_markaz[1] = 1200-shoaa[1]
    if y_markaz[1] < shoaa[1]:
        y_markaz[1] = shoaa[1]
    if y_markaz[1]+shoaa[1] > 700:
        y_markaz[1] = 700-shoaa[1]
    if x_markaz[2] < shoaa[2]:
        x_markaz[2] = shoaa[2]
    if x_markaz[2]+shoaa[2] > 1200:
        x_markaz[2] = 1200-shoaa[2]
    if y_markaz[2] < shoaa[2]:
        y_markaz[2] = shoaa[2]
    if y_markaz[2]+shoaa[2] > 700:
        y_markaz[2] = 700-shoaa[2]
    if x_markaz[3] < shoaa[3]:
        x_markaz[3] = shoaa[3]
    if x_markaz[3]+shoaa[3] > 1200:
        x_markaz[3] = 1200-shoaa[3]
    if y_markaz[3] < shoaa[3]:
        y_markaz[3] = shoaa[3]
    if y_markaz[3]+shoaa[3] > 700:
        y_markaz[3] = 700-shoaa[3]
    if x_markaz[4] < shoaa[4]:
        x_markaz[4] = shoaa[4]
    if x_markaz[4]+shoaa[4] > 1200:
        x_markaz[4] = 1200-shoaa[4]
    if y_markaz[4] < shoaa[4]:
        y_markaz[4] = shoaa[4]
    if y_markaz[4]+shoaa[4] > 700:
        y_markaz[4] = 700-shoaa[4]
    pg.display.update()
    pg.time.Clock().tick(30)

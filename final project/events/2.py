import pygame as pg
import time
pg.init()
win = pg.display.set_mode((800,600))
run = True

#متغيرها
background = pg.transform.scale(pg.image.load("background.PNG"),(800,600))
lst1 = ["bala","rast","paein","chap"]
lst2 = ["bala","rast","paein","chap"]
salamati1 = 1
salamati2 = 1
i = 0
j = 0
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
f7 = 0
f8 = 0
up = False
down = False
up2 = False
down2 = False
x = 650
y = 450
x2 = 0
y2 = 450
tir1 = [1,2,3,4]
tir2 = [1,2,3,4]
flag1 = False
#وايل اصلي
while run:
    win.blit(background,(0,0))
    win.blit(pg.transform.scale(pg.image.load(lst1[i]+".PNG"),(150,150)),(x,y))
    win.blit(pg.transform.scale(pg.image.load(lst1[j]+".PNG"),(150,150)),(x2,y2))
    win.blit(pg.transform.scale(pg.image.load("salamati1_"+str(salamati1)+".PNG"),(100,70)),(0,0))
    win.blit(pg.transform.scale(pg.image.load("salamati2_"+str(salamati2)+".PNG"),(100,70)),(700,0))

    if f1 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir1.PNG"),(50,50)),(x_tirha+50,y1_tir1))
        y1_tir1 -= 30
        if y1_tir1 < -30:
            f1 = 0
        if y2 < y1_tir1 < y2+150:
            salamati2 += 1
            y1_tir1 = -50
        
    if f2 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir2.PNG"),(50,50)),(x1_tir1,y_tirha+50))
        x1_tir1 += 30
        if x1_tir1 > 840:
            f2 = 0
        if x2 < x1_tir1 < x2+150:
            salamati2 += 1
            x1_tir1 = 850
    if f3 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir3.PNG"),(50,50)),(x_tirha+50,y2_tir1))
        y2_tir1 += 30
        if y2_tir1 > 540:
            f3 = 0
        if y2 < y2_tir1 < y2+150:
            salamati2 += 1
            y2_tir1 = 650
    if f4 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir4.PNG"),(50,50)),(x2_tir1,y_tirha+50))
        x2_tir1 -= 30
        if x2_tir1 < -30:
            f4 = 0
        if x2 < x2_tir1 < x2+150:
            salamati2 += 1
            x2_tir1 = -50
    if f5 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir1.PNG"),(50,50)),(x2_tirha+50,y1_tir2))
        y1_tir2 -= 30
        if y1_tir2 < -30:
            f5 = 0
        if y < y1_tir2 < y+150:
            salamati1 += 1
            y1_tir2 = -50
    if f6 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir2.PNG"),(50,50)),(x1_tir2,y2_tirha+50))
        x1_tir2 += 30
        if x1_tir2 > 840:
            f6 = 0
        if x < x1_tir2 < x+150:
            salamati1 += 1
            x1_tir2 = 850
    if f7 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir3.PNG"),(50,50)),(x2_tirha+50,y2_tir2))
        y2_tir2 += 30
        if y2_tir2 > 540:
            f7 = 0
        if y < y2_tir2 < y+150:
            salamati1 += 1
            y2_tir2 = 650
    if f8 == 1:
        win.blit(pg.transform.scale(pg.image.load("tir4.PNG"),(50,50)),(x2_tir2,y2_tirha+50))
        x2_tir2 -= 30
        if x2_tir2 < -30:
            f8 = 0
        if x < x2_tir2 < x+150:
            salamati1 += 1
            x2_tir2 = -50
    if salamati2 == 4:
        win.blit(pg.transform.scale(pg.image.load("gameover2.PNG"),(800,600)),(0,0))
        pg.display.update()
        time.sleep(4)
        run = False
    if salamati1 == 4:
        win.blit(pg.transform.scale(pg.image.load("gameover1.PNG"),(800,600)),(0,0))
        pg.display.update()
        time.sleep(4)
        run = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        #ايونت هاي تانک دوم
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                i += 1
                if i == 4:
                   i = 0
            if event.key == pg.K_LEFT:
                i -= 1
                if i == -1:
                    i = 3
            if event.key == pg.K_UP:
                up = True
            if event.key == pg.K_DOWN:
                down = True
            if event.key == pg.K_SPACE and i == 0:
                if f1 == 0:
                    y1_tir1 = y-50
                    x_tirha = x
                f1 = 1
            if event.key == pg.K_SPACE and i == 1:
                if f2 == 0:
                    x1_tir1 = x+140
                    y_tirha = y
                f2 = 1
            if event.key == pg.K_SPACE and i == 2:
                if f3 == 0:
                    y2_tir1 = y+140
                    x_tirha = x
                f3 = 1
            if event.key == pg.K_SPACE and i == 3:
                if f4 == 0:
                    x2_tir1 = x-50
                    y_tirha = y
                f4 = 1
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                up = False
            if event.key == pg.K_DOWN:
                down = False
            if event.key == pg.K_SPACE:
                bullet1 = False
        # ايونت هاي تانک اول
        if event.type == pg.MOUSEBUTTONDOWN and j == 0:
                if f5 == 0:
                    y1_tir2 = y2-80
                    x2_tirha = x2
                f5 = 1
        if event.type == pg.MOUSEBUTTONDOWN and j == 1:
                if f6 == 0:
                    x1_tir2 = x2+130
                    y2_tirha = y2
                f6 = 1
        if event.type == pg.MOUSEBUTTONDOWN and j == 2:
                if f7 == 0:
                    y2_tir2 = y2+130
                    x2_tirha = x2
                f7 = 1
        if event.type == pg.MOUSEBUTTONDOWN and j == 3:
                if f8 == 0:
                    x2_tir2 = x2-80
                    y2_tirha = y2
                f8 = 1
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                j += 1
                if j == 4:
                   j = 0
            if event.key == pg.K_a:
                j -= 1
                if j == -1:
                    j = 3
            if event.key == pg.K_w:
                up2 = True
            if event.key == pg.K_s:
                down2 = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                up2 = False
            if event.key == pg.K_s:
                down2 = False

    # حرکت تانک دوم
    if up:
        if lst1[i] == "rast":
            x += 10
        elif lst1[i] == "chap":
            x -= 10
        elif lst1[i] == "paein":
            y += 10
        else:
            y -= 10
    if down:
        if lst1[i] == "rast":
            x -= 10
        elif lst1[i] == "chap":
            x += 10
        elif lst1[i] == "paein":
            y -= 10
        else:
            y += 10
    #حرکت تانک اول
    if up2:
        if lst1[j] == "rast":
            x2 += 10
        elif lst1[j] == "chap":
            x2 -= 10
        elif lst1[j] == "paein":
            y2 += 10
        else:
            y2 -= 10
    if down2:
        if lst1[j] == "rast":
            x2 -= 10
        elif lst1[j] == "chap":
            x2 += 10
        elif lst1[j] == "paein":
            y2 -= 10
        else:
            y2 += 10
    pg.display.update()
    pg.time.Clock().tick(30)
pg.quit()

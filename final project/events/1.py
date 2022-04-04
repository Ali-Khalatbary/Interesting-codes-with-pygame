import pygame as pg
pg.init()
win = pg.display.set_mode((800,600))
run = True

#متغيرها
background = pg.transform.scale(pg.image.load("background.PNG"),(800,600))
lst1 = ["bala","rast","paein","chap"]
lst2 = ["bala","rast","paein","chap"]
i = 0
j = 0
up = False
down = False
up2 = False
down2 = False
x = 650
y = 450
x2 = 0
y2 = 450
#وايل اصلي
while run:
    win.blit(background,(0,0))
    win.blit(pg.transform.scale(pg.image.load(lst1[i]+".PNG"),(150,150)),(x,y))
    win.blit(pg.transform.scale(pg.image.load(lst1[j]+".PNG"),(150,150)),(x2,y2))
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
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                up = False
            if event.key == pg.K_DOWN:
                down = False
        #ايونت هاي تانک اول
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
    k = 1
pg.quit()

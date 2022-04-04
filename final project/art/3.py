import pygame as pg
import time as t
pg.init()
win = pg.display.set_mode((700,700))

q = 0
run = True

m1 = -100
m2 = 100
m3 = 0
m4 = 50

pg.mixer.init()
pg.mixer.music.load("music.mp3")
pg.mixer.music.set_volume(0.5)
pg.mixer.music.play(-1)

snd = pg.mixer.Sound("sound.wav")

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    snd.play()
    win.blit(pg.transform.scale(pg.image.load(str(q%10)+".jfif"),(700,700)),(0,0))
    q += 1
    pg.display.update()
    t.sleep(5)
    win.fill((0,0,0))
    if q%10 == 1:
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(100*(6-i),100*(6-i))),(0,0))
            pg.display.update()
            t.sleep(0.5)
            win.fill((0,0,0))
    if q%10 == 2:
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(100*(6-i),100*(6-i))),(100*(i+1),100*(i+1)))
            pg.display.update()
            t.sleep(0.5)
            win.fill((0,0,0))
    if q%10 == 3:
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,m1))
            win.blit(pg.transform.scale(pg.image.load(str((q)%10)+".jfif"),(700,700)),(0,700+m1))
            pg.display.update()
            m1 -= 100
            t.sleep(0.5)
    if q%10 == 4:
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(m2,0))
            win.blit(pg.transform.scale(pg.image.load(str((q)%10)+".jfif"),(700,700)),(m2-700,0))
            pg.display.update()
            m2 += 100
            t.sleep(0.5)
    if q%10 == 5:
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(100*(6-i),100*(6-i))),(50*(i+1),50*(i+1)))
            pg.display.update()
            t.sleep(0.5)
            win.fill((0,0,0))
        for i in range(7):
            win.blit(pg.transform.scale(pg.image.load(str((q)%10)+".jfif"),(100*i,100*i)),(50*(7-i),50*(7-i)))
            pg.display.update()
            t.sleep(0.5)
            win.fill((0,0,0))
    if q%10 == 6:
        win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,0))
        for i in range(7):
            pg.draw.line(win,(0,0,0),(m3+25,0),(m3+25,700),50)
            pg.display.update()
            t.sleep(0.5)
            m3 += 100
        for i in range(7):
            pg.draw.line(win,(255,255,255),(m4+25,0),(m4+25,700),50)
            pg.display.update()
            t.sleep(0.5)
            m4 += 100
    if q%10 == 7:
        m3 = 0
        m4 = 50
        win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,0))
        for i in range(7):
            pg.draw.line(win,(0,0,0),(0,m3+25),(700,m3+25),50)
            pg.display.update()
            t.sleep(0.5)
            m3 += 100
        for i in range(7):
            pg.draw.line(win,(255,255,255),(0,m4+25),(700,m4+25),50)
            pg.display.update()
            t.sleep(0.5)
            m4 += 100
    if q%10 == 8:
        win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,0))
        for i in range(71):
            for j in range(71):
                pg.draw.rect(win,(255,255,255),((j*10,i*10),(10,10)))
                pg.display.update()
                t.sleep(0.0025)
    if q%10 == 9:
        win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,0))
        for i in range(7):
            for j in range(7):
                pg.draw.circle(win,(255,255,255),(50*(2*i+1),50*(2*j+1)),50)
                pg.display.update()
                t.sleep(0.25)
    if q%10 == 0:
        win.blit(pg.transform.scale(pg.image.load(str((q-1)%10)+".jfif"),(700,700)),(0,0))
        pg.draw.line(win,(0,0,0),(350,0),(350,700),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(0,350),(700,350),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(0,0),(700,700),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(700,0),(0,700),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(700,175),(0,525),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(700,525),(0,175),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(175,0),(525,700),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.line(win,(0,0,0),(525,0),(175,700),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.circle(win,(0,0,0),(350,350),50)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.circle(win,(0,0,0),(350,350),150)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.circle(win,(0,0,0),(350,350),250)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.circle(win,(0,0,0),(350,350),350)
        t.sleep(0.5)
        pg.display.update()
        pg.draw.circle(win,(0,0,0),(350,350),450)
        t.sleep(0.5)
        pg.display.update()
    pg.time.Clock().tick(30)
pg.quit()

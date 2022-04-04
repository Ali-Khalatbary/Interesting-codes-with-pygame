import pygame as pg
import time as t
pg.init()
win = pg.display.set_mode((700,700))

q = 0
run = True

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
    t.sleep(10)
    pg.time.Clock().tick(30)

pg.quit()

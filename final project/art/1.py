import pygame as pg
import time as t
pg.init()
win = pg.display.set_mode((700,700))

q = 0
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    win.blit(pg.transform.scale(pg.image.load(str(q%10)+".jfif"),(700,700)),(0,0))
    q += 1
    pg.display.update()
    t.sleep(5)
    pg.time.Clock().tick(30)

pg.quit()

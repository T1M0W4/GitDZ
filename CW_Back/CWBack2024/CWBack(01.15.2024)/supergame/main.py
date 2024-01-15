import pygame as pg

pg.init()
pg.display.set_mode((1024, 768))

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
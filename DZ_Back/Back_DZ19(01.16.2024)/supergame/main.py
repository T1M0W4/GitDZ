import pygame as pg

pg.init()
pg.display.set_caption("Magic Mastery Boss")
icon = pg.image.load('resources/icons/robe.png')
pg.display.set_icon(icon)

screen = pg.display.set_mode((800, 600))

running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((77, 155, 161))
    pg.display.update()
pg.quit()   



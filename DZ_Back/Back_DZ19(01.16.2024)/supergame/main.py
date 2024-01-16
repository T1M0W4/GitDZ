import pygame as pg
import controls
import player

FPS = 50
pg.init()
clock = pg.time.Clock()
pg.display.set_caption("Magic Mastery Boss")
icon = pg.image.load('resources/icons/robe.png')
pg.display.set_icon(icon)
screen = pg.display.set_mode((1024, 768))
bg_color = "gray"
me = player.init((24, 34), (512-25, 384-25), "magenta")
bg = pg.image.load('resources/background/dunge.png')


running = True
while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    controls.check()        
    screen.blit(bg, (300, 300))
    player.update(me)
    screen.blit(me, player.my_position)
    pg.display.update()
    clock.tick(FPS)
    
pg.quit()   



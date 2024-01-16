import pygame as pg

my_size = (0,0)
my_position = (0,0)
my_color = "green"
my_sprite = None
my_frame = 0

def init(size, position, color):
    global my_size, my_position, my_color, my_sprite
    my_size = size
    my_position = position
    my_color = color
    my_sprite = pg.image.load('resources\GG_mage\mage-dark.png')
    me = pg.Surface((my_size))
    update(me)
    me.set_colorkey((0, 0, 0))
    return me

def update(me):
    me.fill((0, 0, 0))
    me.blit(my_sprite, (0, 0), (my_size[0]*my_frame, 0, my_size[0]*(my_frame+1), my_size[1]))

def next_frame():
    global my_frame
    my_frame += 1
    if my_frame > 11:
        my_frame = 0

def move(dx, dy):
    global my_position
    my_position = (my_position[0]+dx, my_position[1]+dy)
    next_frame()
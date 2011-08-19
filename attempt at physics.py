import pygame
from pygame.locals import *
from useful import Vec

class _globals():
    pass

class Box():
    def __init__(self):
        self.pos = Vec(200,200)
        self.vel = Vec(0,0)
        self.force = Vec(0,0)
        self.r = pygame.Rect(200,200,100,100)

    def update(self):
        self.vel += self.force + [0,grav]
        
        self.pos += self.vel
        if self.pos[1] > winy-100:
            #get out of the floor
            self.pos[1] -= (self.pos[1]+100-winy)*2
            self.vel[1] *= -0.4
            if abs(self.vel[1]) < 1:
                self.pos[1] = winy-100
                self.vel[1] = 0
                self.vel[0] *= friction
        if self.pos[0] < 0:
            #keep out of left wall
            self.pos[0] *= -1
            self.vel[0] *= -0.5
        elif self.pos[0] > 572:
            self.pos[0] -= 2*(self.pos[0]+100-winx)
            self.vel[0] *= -0.5
        self.r.topleft = self.pos.data
        print self.pos, self.vel
#---------------------------w---p
#-2(p-w)
    def draw(self):
        pygame.draw.rect(screen,(255,255,255),self.r,1)

#GLOBALS
g = _globals()
clock = pygame.time.Clock()
winx, winy = 672, 672
box = Box()
grav = 1
grabbed = 0
offset = [0,0]
friction = 0.95


#SETUP
pygame.init()
screen = pygame.display.set_mode((winx,winy))
pygame.display.set_caption("Physics simulator")


############################## - MAINLOOP - ##############################

_END = False
while True:
    p = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and box.r.collidepoint(pygame.mouse.get_pos()):
            grabbed = 1
            offset = [box.pos[0]-p[0],box.pos[1]-p[1]]
        if event.type == MOUSEBUTTONUP and grabbed:
            grabbed = 0
            box.vel = Vec(pygame.mouse.get_rel())
        if event.type == QUIT:
            _END = True
            break
    if _END:
        break

    #update shit
    box.update()
    if grabbed:
        box.r.topleft = (p[0]+offset[0],p[1]+offset[1])
        box.r.clamp_ip((0,0,winx,winy))
        box.pos = Vec(box.r.topleft)
        box.vel *= 0
    #draw shit
    screen.fill((0,0,0))
    box.draw()
    
    pygame.display.flip()
    #exec raw_input(">>> ")
    pygame.mouse.get_rel()   #get_rel only measures movement relative to last call
    clock.tick(40)

pygame.quit()

import random

from pygame.math import Vector2

import core


class Brique(object):
    def __init__(self,i,j,w,h):
        self.pos=Vector2(i,j)
        self.longeur=w
        self.hauteur=h
        self.offset=50
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def show(self):
        core.Draw.rect(self.color, (self.pos.x*self.longeur+self.pos.x,self.offset+self.pos.y*self.hauteur+self.pos.y,self.longeur,self.hauteur))

    def intersection(self, balle):

        DeltaX = balle.pos.x - max(self.pos.x*self.longeur+self.pos.x, min(balle.pos.x, self.pos.x*self.longeur+self.pos.x + self.longeur));
        DeltaY = balle.pos.y - max(self.offset+self.pos.y*self.hauteur+self.pos.y, min(balle.pos.y, self.offset+self.pos.y*self.hauteur+self.pos.y + self.hauteur));
        print((DeltaX * DeltaX + DeltaY * DeltaY) < (balle.r * balle.r))
        return (DeltaX * DeltaX + DeltaY * DeltaY) < (balle.r * balle.r)
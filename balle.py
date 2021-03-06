import random

from pygame.math import Vector2

import core


class Balle:
    def __init__(self,w=400,h=400):
        self.pos = Vector2(random.randint(0,w),random.randint(0,h))
        self.vel = Vector2(random.uniform(-1,1),random.uniform(0,10))
        self.acc = Vector2()
        self.maxVel = 4
        self.maxAcc=1
        self.r = 10
        self.color=(255,0,0)

    def applyForce(self,force):
        pass

    def intersection(self, objet):
        DeltaX = self.pos.x - max(objet.pos.x, min(self.pos.x, objet.pos.x + objet.longeur));
        DeltaY = self.pos.y - max(objet.pos.y, min(self.pos.y, objet.pos.y + objet.hauteur));
        return (DeltaX * DeltaX + DeltaY * DeltaY) < (self.r * self.r);

    def update(self,player):
        self.pos+=self.vel

        if self.intersection(player):
            self.vel.y *= -1







    def edge(self,sizes):
        if self.pos.x <=0:
            self.vel.x *= -1
            self.pos.x = 10
        if self.pos.x >= sizes[0]:
            self.vel.x *= -1
            self.pos.x = sizes[0] - 10
        if self.pos.y <= 0:
            self.vel.y *= -1
            self.pos.y = 10
        if self.pos.y >= sizes[1]:
            return True
        return False

    def show(self):
        core.Draw.circle(self.color,self.pos,self.r)

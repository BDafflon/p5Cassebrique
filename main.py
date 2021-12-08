import random
import pygame
from pygame.math import Vector2, Vector3
import core
from cassebrique.balle import Balle
from cassebrique.brique import Brique
from cassebrique.player import Player





def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [800, 600]
    core.memory("IA",False)
    core.memory("b",Balle())
    core.memory("GameOver", False)
    core.memory("Score", 0)

    core.memory('p',Player(800,600))

    core.memory('briques',[])
    core.memory('nbBriqueLargeur',10)
    core.memory('nbBriqueHauteur',5)
    for i in range(0,core.memory('nbBriqueLargeur')):
        for j in range(0,core.memory('nbBriqueHauteur')):
            core.memory('briques').append(Brique(i,j,(800-core.memory('nbBriqueLargeur'))/core.memory('nbBriqueLargeur'),(200-core.memory('nbBriqueHauteur'))/core.memory('nbBriqueHauteur')))




    print("Setup END-----------")




def run():
    #SCore
    myfont = pygame.font.SysFont('Comic Sans MS', 20)
    textsurface = myfont.render("Score :"+str(core.memory("Score")), False, (255, 0, 0))
    core.screen.blit(textsurface, (10,10))

    #Rerstart
    if core.getKeyPressList("r"):
        restart()
    if len(core.memory("briques"))==0:
        restart()

    #Si pas perdu
    if not core.memory("GameOver"):
        core.cleanScreen()

        #Update player
        if core.getMouseLeftClick():
            core.memory('p').update(core.getMouseLeftClick())

        if core.memory("IA"):
            core.memory('p').pos.x=core.memory('b').pos.x-core.memory('p').longeur/2

        #Update balle
        core.memory('b').update(core.memory('p'))

        if core.memory('b').edge(core.WINDOW_SIZE):
            core.memory("GameOver",True)



        #Affichage
        core.memory('b').show()
        core.memory('p').show()


        for i,brique in enumerate(core.memory("briques")):
            if brique.intersection(core.memory('b')):

                core.memory("briques").remove(brique)
                core.memory("Score", core.memory("Score") + 1)
                core.memory('b').vel.y*=-1

        for i, brique in enumerate(core.memory("briques")):
            brique.show()




    else: #Perdu
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render("Game Over", False, (255, 0, 0))
        core.screen.blit(textsurface, (core.WINDOW_SIZE[0]/2-250, core.WINDOW_SIZE[1]/2-50))

        textsurface = myfont.render("Score :"+str(core.memory("Score")), False, (255, 0, 0))
        core.screen.blit(textsurface, (core.WINDOW_SIZE[0] / 2 - 200, core.WINDOW_SIZE[1] / 2 +50))


def restart():
    core.memory("b", Balle())
    core.memory("GameOver", False)
    core.memory('p', Player(800, 600))
    core.memory('briques', [])
    core.memory('nbBriqueLargeur', 10)
    core.memory('nbBriqueHauteur', 5)
    for i in range(0, core.memory('nbBriqueLargeur')):
        for j in range(0, core.memory('nbBriqueHauteur')):
            core.memory('briques').append(
                Brique(i, j, (800 - core.memory('nbBriqueLargeur')) / core.memory('nbBriqueLargeur'),
                       (200 - core.memory('nbBriqueHauteur')) / core.memory('nbBriqueHauteur')))





core.main(setup, run)

import pygame
from pygame.locals import *
import random



ROUGE = (255, 0, 0)


# Taille de la fenêtre
LARGEUR_FENETRE = 500
HAUTEUR_FENETRE = 500




# Classe pour la raquette
class Raquette:
    def __init__(self, x, y,Lr=80,Hr=10):
        self.x = x
        self.y = y
        self.Lr = Lr
        self.Hr = Hr

    def dessine(self, surface):
        pygame.draw.rect(surface, ROUGE, (self.x, self.y,self.Lr,self.Hr ))

    def deplace(self, direction):
        if direction == "gauche" and self.x > 0:
            self.x -= 1
        elif direction == "droite" and self.x < LARGEUR_FENETRE - self.Lr:
            self.x += 1


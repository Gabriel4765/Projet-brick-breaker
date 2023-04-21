import pygame
from pygame.locals import *
import random

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)

# Taille de la fenêtre
LARGEUR_FENETRE = 500
HAUTEUR_FENETRE = 500


# Taille de la raquette
LARGEUR_RAQUETTE = 80
HAUTEUR_RAQUETTE = 10

# Classe pour la raquette
class Raquette:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dessine(self, surface):
        pygame.draw.rect(surface, ROUGE, (self.x, self.y, LARGEUR_RAQUETTE, HAUTEUR_RAQUETTE))

    def deplace(self, direction):
        if direction == "gauche" and self.x > 0:
            self.x -= 0.60
        elif direction == "droite" and self.x < LARGEUR_FENETRE - LARGEUR_RAQUETTE:
            self.x += 0.60
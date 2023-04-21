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

# Taille de la balle
RAYON_BALLE = 10

# Taille des briques
LARGEUR_BRIQUE = 50
HAUTEUR_BRIQUE = 20

class Brique:
    def __init__(self, x, y, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.visible = True

    def dessine(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.couleur, (self.x, self.y, LARGEUR_BRIQUE, HAUTEUR_BRIQUE))

    def est_en_collision_avec(self, balle):
        if not self.visible:
            return False

        if balle.x + RAYON_BALLE > self.x and balle.x - RAYON_BALLE < self.x + LARGEUR_BRIQUE:
            if balle.y + RAYON_BALLE > self.y and balle.y - RAYON_BALLE < self.y + HAUTEUR_BRIQUE:
                self.visible = False
                balle.vy = -balle.vy
                return True

        return False
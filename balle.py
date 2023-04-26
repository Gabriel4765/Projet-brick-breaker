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

# Taille de la balle
RAYON_BALLE = 10

# Taille de la raquette
LARGEUR_RAQUETTE = 80
HAUTEUR_RAQUETTE = 10

# Classe pour la balle
class Balle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def deplace(self):
        self.x += self.vx
        self.y += self.vy

    def dessine(self, surface):
        pygame.draw.circle(surface, JAUNE, (int(self.x), int(self.y)), RAYON_BALLE)

    def rebondit_sur_murs(self):
        if self.x < RAYON_BALLE or self.x > LARGEUR_FENETRE - RAYON_BALLE:
            self.vx = -self.vx

        if self.y < RAYON_BALLE:
            self.vy = -self.vy

    def rebondit_sur_raquette(self, raquette):
        if raquette.x < self.x < raquette.x + LARGEUR_RAQUETTE:
            if (raquette.y < self.y - RAYON_BALLE < raquette.y + HAUTEUR_RAQUETTE):
                self.vy = -self.vy

        # Collision sur le coin
        elif raquette.y < self.y < raquette.y + HAUTEUR_RAQUETTE:
            if (raquette.x < self.x + RAYON_BALLE < raquette.x + LARGEUR_RAQUETTE) or (raquette.x < self.x - RAYON_BALLE < raquette.x + LARGEUR_RAQUETTE):
                self.vx = -self.vx
                self.vy = -self.vy



    def est_sortie(self):
        return self.y > HAUTEUR_FENETRE

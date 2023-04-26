import pygame
from pygame.locals import *
import random
from balle import Balle

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
        pygame.draw.rect(surface, self.couleur, (self.x, self.y, LARGEUR_BRIQUE, HAUTEUR_BRIQUE))

    def est_en_collision_avec(self, balle):
        #collision verticale
        if balle.x  > self.x and balle.x < self.x + LARGEUR_BRIQUE:
            if self.y < (balle.y + RAYON_BALLE) < (self.y + HAUTEUR_BRIQUE) or (self.y + HAUTEUR_BRIQUE) > (balle.y - RAYON_BALLE) > self.y :
                balle.vy = -balle.vy
                return True
        #collision horizontale
        if balle.y  > self.y and balle.y < self.y + HAUTEUR_BRIQUE:
            if self.x < (balle.x + RAYON_BALLE) < (self.x + LARGEUR_BRIQUE) or (self.x + LARGEUR_BRIQUE) > (balle.x - RAYON_BALLE) > self.x :
                balle.vx = -balle.vx
                return True

        return False

class Brique_x3(Brique):
    def __init__(self, x, y, couleur):
        super().__init__(x, y, couleur)

    def dessine(self,surface):
        pygame.draw.rect(surface, self.couleur, (self.x, self.y, LARGEUR_BRIQUE, HAUTEUR_BRIQUE))

        # Choisir la police, la taille et la couleur du texte
        font = pygame.font.Font(None, 24)
        text_color = (0, 0, 0)  # Couleur du texte en RGB (ici noir)

        # Créer l'objet texte
        texte = font.render("x3", True, text_color)

        # Calculer la position du texte pour le centrer sur la brique
        text_rect = texte.get_rect(center=(self.x + LARGEUR_BRIQUE / 2, self.y + HAUTEUR_BRIQUE / 2))

        # Dessiner le texte sur la surface
        surface.blit(texte, text_rect)

    def activer_bonus(self):
        global liste_balles
        vx, vy = 0.3, 0.5
        bonus_balle_1 = Balle(self.x + LARGEUR_BRIQUE / 2, self.y + HAUTEUR_BRIQUE, vx, vy)
        bonus_balle_2 = Balle(self.x + LARGEUR_BRIQUE / 2, self.y + HAUTEUR_BRIQUE, vx, -vy)
        liste_balles.extend([bonus_balle_1, bonus_balle_2])

    def est_en_collision_avec(self, balle):
        collision = super().est_en_collision_avec(balle)
        if collision:
            self.activer_bonus()
        return collision

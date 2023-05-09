import pygame
from pygame.locals import *
import random
from balle import Balle




# Taille de la balle
RAYON_BALLE = 10



class Brique:
    def __init__(self, x, y, Lb, Hb, couleur):
        self.x = x
        self.y = y
        self.couleur = couleur
        self.Lb = Lb
        self.Hb = Hb
        self.rect = pygame.Rect(self.x, self.y, self.Lb, self.Hb)
        self.bonus = 'None'

    def dessine(self, surface):
        #création brique à partir du coin qui correspond au plus petits x et y (vecteur ey vers le bas)
        pygame.draw.rect(surface, self.couleur, self.rect)

    def est_en_collision_avec(self, balle):
        #collision verticale
        if balle.x  >= self.x and balle.x <= self.x + self.Lb:
            if self.y <= (balle.y + RAYON_BALLE) <= (self.y + self.Hb) or (self.y + self.Hb) >= (balle.y - RAYON_BALLE) >= self.y :
                balle.vy = -balle.vy
                return (True,self.bonus)
        #collision horizontale
        if balle.y  >= self.y and balle.y <= self.y + self.Hb:
            if self.x <= (balle.x + RAYON_BALLE) <= (self.x + self.Lb) or (self.x + self.Lb) >= (balle.x - RAYON_BALLE) >= self.x :
                balle.vx = -balle.vx
                return (True,self.bonus)

        return (False,'')

class Brique_x2(Brique):
    def __init__(self, x, y,Lb,Hb,couleur):
        super().__init__(x, y,Lb,Hb,couleur)
        self.bonus = 'x2'

    def dessine(self,surface):
        pygame.draw.rect(surface, self.couleur, self.rect)

        # Choisir la police, la taille et la couleur du texte
        font = pygame.font.Font(None, 24)
        text_color = (0, 0, 0)  # Couleur du texte en RGB (ici noir)

        # Créer l'objet texte
        texte = font.render("x2", True, text_color)

        # Calculer la position du texte pour le centrer sur la brique
        text_rect = texte.get_rect(center=(self.x + self.Lb / 2, self.y + self.Hb / 2))

        # Dessiner le texte sur la surface
        surface.blit(texte, text_rect)

    def generer(self,balle):
            return(Balle(balle.x,balle.y, -1.2*balle.vx, -1.2*balle.vy))

class Brique_3PV(Brique):
    def __init__(self,x,y,Lb,Hb,couleur):
        super().__init__(x,y,Lb,Hb,couleur)
        self.vie = 3
        self.bonus = '3pv'

    def dessine(self,surface):
        pygame.draw.rect(surface, self.couleur, self.rect)

        # Choisir la police, la taille et la couleur du texte
        font = pygame.font.Font(None, 24)
        text_color = (0, 0, 0)  # Couleur du texte en RGB (ici noir)

        # Créer l'objet texte
        texte = font.render("{} PV".format(self.vie), True, text_color)

        # Calculer la position du texte pour le centrer sur la brique
        text_rect = texte.get_rect(center=(self.x + self.Lb / 2, self.y + self.Hb / 2))

        # Dessiner le texte sur la surface
        surface.blit(texte, text_rect)

    def est_en_collision_avec(self, balle):
        #collision verticale
        if balle.x  >= self.x and balle.x <= self.x + self.Lb:
            if self.y <= (balle.y + RAYON_BALLE) <= (self.y + self.Hb) or (self.y + self.Hb) >= (balle.y - RAYON_BALLE) >= self.y :
                balle.vy = -balle.vy
                self.vie -= 1
                return (True, '3pv')
        #collision horizontale
        elif balle.y  >= self.y and balle.y <= self.y + self.Hb:
            if self.x <= (balle.x + RAYON_BALLE) <= (self.x + self.Lb) or (self.x + self.Lb) >= (balle.x - RAYON_BALLE) >= self.x :
                balle.vx = -balle.vx
                self.vie -= 1
                return (True, '3pv')

        return(False,'')

class Brique_Raquette(Brique):
    def __init__(self, x, y, lb, hb, couleur):
        super().__init__(x, y, lb,hb,couleur)
        self.bonus_actif = False
        self.bonus = 'Raquette'
        self.collisions_restantes = 10

    def activer_bonus(self, raquette):
        if not self.bonus_actif:
            self.bonus_actif = True
            raquette.largeur *= 2

    def desactiver_bonus(self, raquette):
        if self.bonus_actif:
            self.bonus_actif = False
            raquette.largeur //= 2




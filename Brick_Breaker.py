import pygame
from pygame.locals import *
import random
from balle import Balle
from raquette import Raquette
from brique import Brique

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

# Taille des briques
LARGEUR_BRIQUE = 50
HAUTEUR_BRIQUE = 20

# Fonction principale
def main():
    pygame.init()

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
    pygame.display.set_caption("Casse-briques")

    # Création de la balle
    balle = Balle(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2,0.2,0.2)

    # Création de la raquette
    raquette = Raquette(LARGEUR_FENETRE / 2 - LARGEUR_RAQUETTE / 2, HAUTEUR_FENETRE - HAUTEUR_RAQUETTE - 10)

    # Création des briques
    briques = []
    for i in range(8):
        for j in range(4):
            x = i * LARGEUR_BRIQUE + 60
            y = j * HAUTEUR_BRIQUE + 50
            couleur = random.choice([ROUGE, VERT, BLEU])
            briques.append(Brique(x, y, couleur))

    # Boucle principale
    while True:
        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                pygame.quit()
                return

        # Déplacement de la balle
        balle.deplace()

        # Rebond de la balle sur les murs
        balle.rebondit_sur_murs()

        # Rebond de la balle sur la raquette
        balle.rebondit_sur_raquette(raquette)

        # Vérification si la balle est sortie
        if balle.est_sortie():
            pygame.quit()
            return

        # Déplacement de la raquette
        touches = pygame.key.get_pressed()
        if touches[K_LEFT]:
            raquette.deplace("gauche")
        elif touches[K_RIGHT]:
            raquette.deplace("droite")

        # Affichage
        fenetre.fill(NOIR)

        balle.dessine(fenetre)
        raquette.dessine(fenetre)

        for brique in briques:
            brique.dessine(fenetre)
            if brique.est_en_collision_avec(balle):
                briques.remove(brique)

        pygame.display.flip()


# Appel de la fonction principale
if __name__ == "__main__":
    main()

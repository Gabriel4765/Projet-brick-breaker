import pygame
from pygame.locals import *
import random
from balle import Balle
from raquette import Raquette
from brique import Brique
from brique import Brique_x3

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
JAUNE = (255, 255, 0)
vx = 0.5
vy= 0.5

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
def jeu():
    pygame.init()

    # Création de la fenêtre
    fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE),pygame.FULLSCREEN | pygame.NOFRAME)
    pygame.display.set_caption("Casse-briques")

    # Création d'un calque pour les briques
    calque_briques = pygame.Surface((LARGEUR_FENETRE, HAUTEUR_FENETRE), pygame.SRCALPHA, 32)
    calque_briques.fill((0, 0, 0, 0))  # Remplir le calque avec une couleur transparente

    # Compte à rebours avant le début de la partie
    font = pygame.font.SysFont(None, 100)
    temps_restant = 3
    while temps_restant > 0:
        fenetre.fill(NOIR)
        texte = font.render(str(temps_restant), True, ROUGE)
        texte_rect = texte.get_rect(center=(LARGEUR_FENETRE // 2, HAUTEUR_FENETRE // 2))
        fenetre.blit(texte, texte_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        temps_restant -= 1

    # Création de la balle
    balle = Balle(LARGEUR_FENETRE / 2, HAUTEUR_FENETRE / 2,vx,vy)

    # Création de la raquette
    raquette = Raquette(LARGEUR_FENETRE / 2 - LARGEUR_RAQUETTE / 2, HAUTEUR_FENETRE - HAUTEUR_RAQUETTE - 10)



    # Création des briques
    briques = []
    for i in range(8):
        for j in range(4):
            x = i * LARGEUR_BRIQUE + 60
            y = j * HAUTEUR_BRIQUE + 50
            couleur = random.choice([ROUGE, VERT, BLEU])
            if random.random() < 0.5:  # 10% de chance de créer une brique bonus
                brique = Brique_x3(x, y, couleur)
            else:
                brique = Brique(x, y, couleur)
            brique.dessine(calque_briques)
            briques.append(brique)


    pygame.display.flip()


    # Boucle principale
    while True:

        # Affichage
        fenetre.fill(NOIR)

        # Copier le calque des briques sur la surface principale
        fenetre.blit(calque_briques, (0, 0))

        # Gestion des événements
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                break

        # Déplacement de la balle
        balle.deplace()

        # Rebond de la balle sur les murs
        balle.rebondit_sur_murs()

        # Rebond de la balle sur la raquette
        balle.rebondit_sur_raquette(raquette)

        # Vérification si la balle est sortie
        if balle.est_sortie():
            break

        # Déplacement de la raquette
        touches = pygame.key.get_pressed()
        if touches[K_LEFT]:
            raquette.deplace("gauche")
        elif touches[K_RIGHT]:
            raquette.deplace("droite")



        balle.dessine(fenetre)
        raquette.dessine(fenetre)

        for brique in briques:
            if brique.est_en_collision_avec(balle):
                briques.remove(brique)
                # Effacer la brique du calque
                brique_rect = brique.rect.inflate(2, 2)  # Ajouter une marge pour éviter les artefacts
                calque_briques.fill((0, 0, 0, 0), brique_rect)

        pygame.display.flip()

#fenêtre d'accueil
def acceuil():
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE),pygame.FULLSCREEN | pygame.NOFRAME)

    font = pygame.font.SysFont(None, 100)
    texte = font.render('Bienvenu', True, (255, 0, 0))
    texte_rect = texte.get_rect(center=(250, 250))
    bouton_jouer = pygame.Rect(75, 100, 100, 50)
    bouton_quitter = pygame.Rect(225, 100, 100, 50)
    bouton_option = pygame.Rect(375, 100, 100, 50)
    font_bouton = pygame.font.SysFont('Arial', 20)
    texte_jouer = font_bouton.render('Jouer', True, (255, 0, 0))
    texte_quitter = font_bouton.render('Quitter', True, (255, 0, 0))
    texte_option = font_bouton.render('Option', True, (255, 0, 0))
    pygame.draw.rect(ecran, (255, 255, 255), bouton_jouer)
    pygame.draw.rect(ecran, (255, 255, 255), bouton_quitter)
    pygame.draw.rect(ecran, (255, 255, 255), bouton_option)
    ecran.blit(texte, texte_rect)
    ecran.blit(texte_jouer, (100, 115))
    ecran.blit(texte_quitter, (250, 115))
    ecran.blit(texte_option, (400, 115))

    pygame.display.flip()
    while True:
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                pygame.quit()
                return
            elif evenement.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bouton_jouer.collidepoint(pos):
                    return (1)
                elif bouton_quitter.collidepoint(pos):
                    pygame.quit()
                    return (0)
                elif bouton_option.collidepoint(pos):
                    option()

def option():
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE), pygame.FULLSCREEN | pygame.NOFRAME)

def defaite():
    pygame.init()
    ecran = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE),pygame.FULLSCREEN | pygame.NOFRAME)

    font = pygame.font.SysFont(None, 100)
    texte = font.render('Game Over', True, (255, 0, 0))
    texte_rect = texte.get_rect(center=(250, 250))
    bouton_rejouer = pygame.Rect(150, 100, 100, 50)
    bouton_quitter = pygame.Rect(250, 100, 100, 50)
    font_bouton = pygame.font.SysFont('Arial', 20)
    texte_rejouer = font_bouton.render('Rejouer', True, (255, 0, 0))
    texte_quitter = font_bouton.render('Quitter', True, (255, 0, 0))
    pygame.draw.rect(ecran, (255, 255, 255), bouton_rejouer)
    pygame.draw.rect(ecran, (255, 255, 255), bouton_quitter)
    ecran.blit(texte, texte_rect)
    ecran.blit(texte_rejouer, (175, 115))
    ecran.blit(texte_quitter, (280, 115))
    pygame.display.flip()
    while True:
        for evenement in pygame.event.get():
            if evenement.type == QUIT:
                pygame.quit()
                break
            elif evenement.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if bouton_rejouer.collidepoint(pos):
                    return (1)
                elif bouton_quitter.collidepoint(pos):
                    pygame.quit()
                    return (0)


# Appel de la fonction principale
if __name__ == "__main__":
    j = acceuil()
    while j == 1:
        jeu()
        j = defaite()


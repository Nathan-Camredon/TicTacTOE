import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

#------------------------------------------------------------------------------------------------------------------------
#                   VARIABLE
#------------------------------------------------------------------------------------------------------------------------
#--- couleur ---
noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
vert = (0, 255, 0)
gris = (200, 200, 200)

#--- Pygame ---
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

#--- Texte Jeu ---
TourX = font.render("A vous de jouer ! Joueur X ", True, noir)
TourO = font.render("A vous de jouer ! Joueur O ", True, noir)
VictoireO = font.render("Le joueur O a gagne !", True, noir)
VictoireX = font.render("Le joueur X a gagne !", True, noir)
Nul = font.render("Match nul !!", True, noir)
txt_quitter = font.render("Quitter", True, blanc)
txt_reset = font.render("Reset", True, blanc)

#--- Valeurs grille ----
plateau = [
    [None, None, None],  
    [None, None, None], 
    [None, None, None]   
]

#--- Tours du joueurs --- 
gagnant = None
Tour = random.choice(["X", "O"])
mode_ia = False

#--- Forme rectangle des boutons ---
rect_quitter = pygame.Rect(1000, 600, 200, 50)
rect_reset = pygame.Rect(100, 600, 200, 50)
rect_ia = pygame.Rect(540, 600, 200, 50)

#------------------------------------------------------------------------------------------------------------------------
#                   FONCTION
#------------------------------------------------------------------------------------------------------------------------

def ordinateur_random(board, signe):
    i = random.choice([0, 1, 2]) 
    j = random.choice([0, 1, 2])

    while board[i][j] != None:
        i = random.choice([0, 1, 2])
        j = random.choice([0, 1, 2])
    board[i][j] = signe

def ordinateur(board, signe):
    if signe == "X":
        a = "O"
    if signe == "O":
        a = "X"
    if board[1][1] == None:
        board[1][1] = signe
        return
    for i in range (3):
        n = 0

def Grille_jeux():
    # --- Lignes Verticales ---
    pygame.draw.line(screen, noir, (415, 135), (415, 585), 5)
    pygame.draw.line(screen, noir, (565, 135), (565, 585), 5)
    pygame.draw.line(screen, noir, (715, 135), (715, 585), 5)
    pygame.draw.line(screen, noir, (865, 135), (865, 585), 5)

    # --- Lignes Horizontales ---
    pygame.draw.line(screen, noir, (415, 135), (865, 135), 5)
    pygame.draw.line(screen, noir, (415, 285), (865, 285), 5)
    pygame.draw.line(screen, noir, (415, 435), (865, 435), 5)
    pygame.draw.line(screen, noir, (415, 585), (865, 585), 5)

    # --- Boutons --- 
    pygame.draw.rect(screen, rouge, rect_quitter) 
    pygame.draw.rect(screen, bleu, rect_reset)
    
    if mode_ia == True:
        pygame.draw.rect(screen, vert, rect_ia)
    else:
        pygame.draw.rect(screen, gris, rect_ia)
        
    screen.blit(txt_quitter, (1050, 610))
    screen.blit(txt_reset, (160, 610)) 
    
    txt_ia = font.render(f"Mode IA: {mode_ia}", True, noir)
    screen.blit(txt_ia, (580, 610)) # Ajusté pour centrer

def pion():
    """
    Fais apparaitre des formes X et O en fonction de cmment ils sont remplis dans le tableau
    """
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == "X":
                pygame.draw.line(screen, rouge, (430 + j * 150, 150 + i * 150), (550 + j * 150, 270 + i * 150), 5)
                pygame.draw.line(screen, rouge, (550 + j * 150, 150 + i * 150), (430 + j * 150, 270 + i * 150), 5)
            elif plateau[i][j] == "O":
                pygame.draw.circle(screen, bleu, (490 + j * 150, 210 + i * 150), 60, 5)

def verifier_gagnant():
    """
    Verifie si il y a une combinaison gagnante
    """
    n = 0
    for i in range(3):
        for j in range(3):
            if plateau[i][j] != None:
                n += 1
    # Lignes
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] and plateau[i][0] is not None:
            return plateau[i][0]
    # Colonnes
    for i in range(3):
        if plateau[0][i] == plateau[1][i] == plateau[2][i] and plateau[0][i] is not None:
            return plateau[0][i]
    # Diagonales
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] is not None:
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] is not None:
        return plateau[0][2]        
    
    if n == 9: 
        return "nul" 

    return None

def Ecriture():
    """
    Commande ecriture qui permet de faire apparaitre tout les textes sur l'état de la partie
        Elle modifie la valeur gagnant en l'appellant en global (sinon le jeu marche)
    """
    global gagnant 
    gagnant = verifier_gagnant()
    
    if gagnant == "X":
        screen.blit(VictoireX, (500, 50))
    elif gagnant == "O":
        screen.blit(VictoireO, (500, 50))
    elif gagnant == "nul":
        screen.blit(Nul, (500,50))
    else:
        if Tour == "X":
            screen.blit(TourX, (500, 50))
        else:
            screen.blit(TourO, (500, 50))

def reset(): 
    """
    Parametre d'usine du jeu
    """
    global plateau, Tour, gagnant 
    plateau = [
        [None, None, None],  
        [None, None, None], 
        [None, None, None]   
    ]
    Tour = random.choice(["X", "O"])
    gagnant = None

#------------------------------------------------------------------------------------------------------------------------
#                   LANCEMENT
#------------------------------------------------------------------------------------------------------------------------

while running:
    screen.fill(blanc)
    
    # --- Action joueurs ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (x, y) = pygame.mouse.get_pos()
                
                if rect_quitter.collidepoint(x, y):
                    running = False
                
                elif rect_reset.collidepoint(x, y):
                    reset()
                
                elif rect_ia.collidepoint(x, y):
                    mode_ia = not mode_ia
                elif gagnant is None:  #Tant que pas de gagnant on laisse de nouveua élement rentrer 
                    if x > 415 and x < 865 and y > 135 and y < 585:
                        colonne = (x - 415) // 150
                        ligne = (y - 135) // 150
                        
                        if plateau[ligne][colonne] == None:
                            plateau[ligne][colonne] = Tour 
                            # Changement de tour
                            if Tour == "X":
                                Tour = "O"
                            else:
                                Tour = "X"
    
    #--- Affichage ---
    Ecriture()
    pion() 
    Grille_jeux()

    pygame.display.flip()
    clock.tick(30) 

pygame.quit()
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
import random
#------------------------------------------------------------------------------------------------------------------------
#                   VARIABLE
#------------------------------------------------------------------------------------------------------------------------
#--- couleur ---
noir = (0, 0, 0)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
bleu = (0, 0, 255)

#--- Pygame ---
clock = pygame.time.Clock()     #Horloge pour limiteus ips (pas touche Nath)
font = pygame.font.SysFont("Arial", 30)

#--- Texte ---
TourX = font.render("A vous de jouer ! Joueurs X ", True, noir)
TourO =  font.render("A vous de jouer ! Joueurs O ", True, noir)
VictoireO =  font.render("Le joueurs O à gagné !", True, noir)
VictoireX =  font.render("Le joueurs X à gagné !", True, noir)
Nul = font.render("Match nul !!", True, noir)

#--- Valeurs grille ----
plateau = [
    [None, None, None],  
    [None, None, None], 
    [None, None, None]   
]

#--- Tours du joueurs --- 
gagnant = None
Tour = random.choice(["X", "O"])
#------------------------------------------------------------------------------------------------------------------------
#                   FONCTION
#------------------------------------------------------------------------------------------------------------------------
def ordinateur1(board, signe):
    i = random.choice([1, 2, 3])
    j = random.choice([1, 2, 3])

    while board[i][j] != None:
        board[i][j] = signe
    
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

def pion():
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == "X":
                pygame.draw.line(screen, rouge, (430 + j * 150, 150 + i * 150), (550 + j * 150, 270 + i * 150), 5)
                pygame.draw.line(screen, rouge, (550 + j * 150, 150 + i * 150), (430 + j * 150, 270 + i * 150), 5)
            elif plateau[i][j] == "O":
                pygame.draw.circle(screen, bleu, (490 + j * 150, 210 + i * 150), 60, 5)

def verifier_gagnant():
    n = 0
    for i in range(3):
        for j in range(3):
            if plateau[i][j] != None:
                n += 1
        if plateau[i][0] == plateau[i][1] == plateau[i][2] and plateau[i][0] is not None:
            return plateau[i][0]
        if plateau[0][i] == plateau[1][i] == plateau[2][i] and plateau[0][i] is not None:
            return plateau[0][i]
    if plateau[0][0] == plateau[1][1] == plateau[2][2] and plateau[0][0] is not None:
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] and plateau[0][2] is not None:
        return plateau[0][2]        
    if n == 9: 
        return "nul" 

    return None

def Ecriture():
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

#------------------------------------------------------------------------------------------------------------------------
#                   LANCEMENT
#------------------------------------------------------------------------------------------------------------------------

while running:
    screen.fill(blanc)
    Ecriture()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and gagnant is None:
            if event.button == 1:
                (x, y) = pygame.mouse.get_pos()
                if x > 415 and x < 865 and y > 135 and y < 585:
                    colonne = (x - 415) // 150
                    ligne = (y - 135) // 150
                    if plateau[ligne][colonne] == None:
                        plateau[ligne][colonne] = Tour 
                        if Tour == "X":
                            Tour = "O"
                        else:
                            Tour = "X"
    pion() 
    Grille_jeux()

    pygame.display.flip()
    clock.tick(5) 

pygame.quit()
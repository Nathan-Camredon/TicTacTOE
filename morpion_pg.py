import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
#------------------------------------------------------------------------------------------------------------------------
#                   VARIABLE
#------------------------------------------------------------------------------------------------------------------------
clock = pygame.time.Clock()     #Horloge pour limiteus ips (pas touche Nath)
#--- couleur ---
black = (0, 0, 0)
white = (255, 255, 255)
#--- Valeurs cases ----
grille_data = [
    [None, None, None],  # Ligne 0
    [None, None, None],  # Ligne 1
    [None, None, None]   # Ligne 2
]
#------------------------------------------------------------------------------------------------------------------------
#                   FONCTION
#------------------------------------------------------------------------------------------------------------------------

def Grille_jeux():
    # --- Lignes Verticales ---
    pygame.draw.line(screen, black, (415, 135), (415, 585), 5)
    pygame.draw.line(screen, black, (565, 135), (565, 585), 5)
    pygame.draw.line(screen, black, (715, 135), (715, 585), 5)
    pygame.draw.line(screen, black, (865, 135), (865, 585), 5)

    # --- Lignes Horizontales ---
    pygame.draw.line(screen, black, (415, 135), (865, 135), 5)
    pygame.draw.line(screen, black, (415, 285), (865, 285), 5)
    pygame.draw.line(screen, black, (415, 435), (865, 435), 5)
    pygame.draw.line(screen, black, (415, 585), (865, 585), 5)
    


#------------------------------------------------------------------------------------------------------------------------
#                   LANCEMENT
#------------------------------------------------------------------------------------------------------------------------


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    Grille_jeux()





    pygame.display.flip()

    clock.tick(15) 

pygame.quit()
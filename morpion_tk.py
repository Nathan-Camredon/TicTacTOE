from tkinter import *

window = Tk()
window.title("Tic Tac Toe")
# --- LES VARIABLES ---
player = ""
# --- LES FONCTIONS ---
def jouer_coup(l, c):
    global player 
    bouton_clique = grille_boutons[l][c]
    if bouton_clique['text'] == " ":
        if player == "X":
            bouton_clique.config(text="X")
            player = "O"
        else:
            bouton_clique.config(text="O")
            player = "X"

# --- LA GRILLE ---
grille_boutons = [] 
for i in range(3):
    ligne_temp = []
    for j in range(3):
        btn = Button(window, text=" ", width=10, height=5, 
                     command=lambda l=i, c=j: jouer_coup(l, c))
        
        btn.grid(row=i, column=j)
        ligne_temp.append(btn)
        
    grille_boutons.append(ligne_temp)

window.mainloop()
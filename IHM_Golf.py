from tkinter import *

#1ere fenetre
fenetre = Tk()

#personnalisition de la fenetre
fenetre.title("Ma premiere IHM")
fenetre.geometry("1024x768")#taille de l'écran sur lequel sera l'ihm
#fenetre.minsize(480,360)#taille minimale
fenetre.iconbitmap("golf.ico")
fenetre.config(background='red')



#afficher 
fenetre.mainloop()
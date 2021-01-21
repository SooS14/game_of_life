from tkinter import * 
import threading


def comptage():
    global b
    while 1:
        b=b+1
        texte.configure(text="Compteur :"+ str(b))
        if b>500000:
            break

b=1  
t = threading.Thread(target=comptage)
fenetre=Tk()							
texte=Label(fenetre,text="Compteur :") 
texte.grid(row=1,column=1)			 
t.start()

fenetre.mainloop() 

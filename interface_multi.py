import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import font as tkfont
from PIL import ImageTk,Image
from functools import partial

from connexion import Connexion
from breizhClass import PlaceholderEntry

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("900x900")
        self.maxsize(900, 900)
        self.minsize(900, 900)



        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # for F in (Accueil):
        page_name = Accueil.__name__
        frame = Accueil(parent=container, controller=self)
        self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Accueil")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



class Accueil(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # création de l'image de bus
        self.img = tk.PhotoImage(file='bus.png')

        # zone d'entête
        self.head_frame = tk.Frame(self, width=900, height=300)
        self.head_frame.grid(row=0, columnspan = 2)
        # zone image
        self.picture_frame = tk.Frame(self.head_frame, width=500, height=300)
        self.picture_frame.grid(row=0, column=0)
        # zone de titre
        self.title_frame = tk.Frame(self.head_frame, width=400, height=300)
        self.title_frame.grid(row=0, column=1)
        # zone des boutons modif/ajout/suppression 
        self.bouton_frame= tk.Frame(self, width=900, height=50)
        self.bouton_frame.grid(row=1)
        # zone de corps de page (sélection ligne/affichage)
        self.corps_frame= tk.Frame(self, width=900, height=550)
        self.corps_frame.grid(row=2)

        # titre
        fontStyle = tkfont.Font(family="Helvetica", size=50)
        self.main_title = tk.Label(self.title_frame, text="Breizhibus", font=fontStyle)
        self.main_title.place(x=200, y=150, anchor='center')
    
        # image/logo
        self.logo = tk.Label(self.picture_frame, image=self.img, relief='flat', bd = 0, borderwidth=0, highlightthickness=0)
        self.logo.pack()

        # bouton pour ouvrir les pages de modif
        self.button_accueil = tk.Button(self.bouton_frame,text="Accueil",command=self.accueil)
        self.button_accueil.grid(row=0, column=0)
        self.button_ajout = tk.Button(self.bouton_frame,text="Ajouter/supprimer",command=self.ajoutSuppr)
        self.button_ajout.grid(row=0, column=1)
        self.button_modif = tk.Button(self.bouton_frame,text="Modifier",command=self.modif)
        self.button_modif.grid(row=0, column=2)
        self.bouton_frame.grid_columnconfigure(0, minsize=100)
        self.bouton_frame.grid_columnconfigure(1, minsize=100)
        self.bouton_frame.grid_columnconfigure(2, minsize=100)

    def accueil(self):
        for widget in self.corps_frame.winfo_children():
            widget.destroy()
        #frame qui contient l'affichage des données recherchées
        self.actions_frame = tk.Frame(self.corps_frame, width=450, height=600)#,  bg='red'
        self.actions_frame.grid(row=0, column = 0)
        self.actions_frame.grid_rowconfigure(0, minsize=600)
        self.actions_frame.grid_columnconfigure(0, minsize=450)

        self.ligne_frame = tk.Frame(self.actions_frame, width=450, height=500)
        self.ligne_frame.grid(row=0)
        

        # zone qui définie les champs d'affichage
        self.show_frame = tk.Frame(self.corps_frame, width=450, height=600)#, bg='blue'
        self.show_frame.grid(row=0, column=1)
        self.show_frame.grid_columnconfigure(0, minsize=0)
        self.show_frame.grid_columnconfigure(1, minsize=100)
        self.show_frame.grid_columnconfigure(2, minsize=100)
        self.show_frame.grid_columnconfigure(3, minsize=185)

        loulou = Connexion.get_ligne()
         
        for i in range (len(loulou)):
            tk.Button(self.ligne_frame, text=loulou[i],width=18, height = 3, command=lambda x=loulou[i]: self.jou(x)).grid(row=i+1, column=0, sticky='ns')

    def jou(self, lign):
        #destruction de frame lors d'une nouvelle sélection
        for widget in self.show_frame.winfo_children():
            widget.destroy()
            
        # tableau contenant les donnees
        index = ["arret", "adresse", "bus"]
        for i in range(len(index)):
            tk.Label(self.show_frame, text=index[i],width=18, height = 3).grid(row=0, column=i+1)
        c_get_arrets = Connexion.get_arrets(lign)
        c_get_bus = Connexion.get_bus(lign)
        for i in range (len(c_get_arrets)):
            tk.Label(self.show_frame ,text=c_get_arrets[i].name, width=18, height = 3 ).grid(row=i+1, column=1)
            tk.Label(self.show_frame ,text=c_get_arrets[i].adresse, width=18, height = 3 ).grid(row=i+1, column=2)
        for i in range (len(c_get_bus)):
            tk.Label(self.show_frame ,text=c_get_bus[i].numero, width=18, height = 3 ).grid(row=i+1, column=3)



    def ajoutSuppr(self):
        for widget in self.corps_frame.winfo_children():
            widget.destroy()
        
        self.add_frame = tk.Frame(self.corps_frame, width=450, height=550)
        self.add_frame.grid(row = 0, column=0)
        self.add_frame.grid_rowconfigure(0, minsize=100)

        self.suppr_frame = tk.Frame(self.corps_frame, width=450, height=550)
        self.suppr_frame.grid(row=0, column=1)

        #########
        # Ajout #
        #########
        fontStyle_suppr = tkfont.Font(family="Helvetica", size=20)
    
        self.add = tk.Label(self.add_frame, text="",font=fontStyle_suppr)
        self.add.grid(row=0, column=0)
        self.add_frame.grid_rowconfigure(0, minsize=100)

        self.add = tk.Label(self.add_frame, text="Ajouter",font=fontStyle_suppr)
        self.add.grid(row=1, column=0)

        self.numero = PlaceholderEntry(self.add_frame, "Numéro de bus")
        self.numero.grid(row=2, column=0, padx=20, pady=20)
        self.plaque = PlaceholderEntry(self.add_frame, "Immatriculation")
        self.plaque.grid(row=3, column=0, padx=20, pady=20)
        self.n_place = PlaceholderEntry(self.add_frame, "Nombre de place")
        self.n_place.grid(row=4, column=0, padx=20, pady=20)
        self.combot = PlaceholderEntry(self.add_frame, "id_ligne")
        self.combot.grid(row=5, column=0, padx=20, pady=20)


        # self.ligne = PlaceholderEntry(self.add_frame, "Ligne").grid(row=0, column=3, padx=20, pady=20)
        # combobox
        # self.lign = Connexion.get_ligne()
        # self.combot = ttk.Combobox(self.add_frame, values = self.lign, state='readonly')
        # self.combot.config(width=10, font=('Helvetica', 12))
        # self.combot.grid(row=0, column=3, padx=20, pady=20 )

        self.add_frame.grid_columnconfigure(0, minsize=450)
        self.suppr_frame.grid_columnconfigure(0, minsize=450)

        self.add_bus = tk.Button(self.add_frame, text="Ajouter", command=lambda: Connexion.ajout_bus(self.numero.get(), self.plaque.get(), self.n_place.get(), self.combot.get()))
        self.add_bus.grid(row=6, column=0, pady=20)


        ################
        # Suppression  #
        ################
        fontStyle_suppr = tkfont.Font(family="Helvetica", size=20)
    
        self.suppr = tk.Label(self.suppr_frame, text="Supprimer",font=fontStyle_suppr)
        self.suppr.grid(row=0, column=0)

        # menu déroulant
        self.bu = Connexion.show_bus()
        self.combo = ttk.Combobox(self.suppr_frame, values = self.bu, state='readonly', postcommand=lambda: self.combo.config(values=Connexion.show_bus()))
        self.combo.config(width=30, font=('Helvetica', 12))
        self.combo.grid(pady=35, row=1, column=0)

        # bouton de suppression de bus
        self.del_bus = tk.Button(self.suppr_frame, text="Supprimer", command=lambda: Connexion.del_bus(self.combo.get()))
        self.del_bus.grid(row=2, column=0, padx=35)
        # self.suppr_frame.grid_rowconfigure(0, minsize=100)
        

    def modif(self):
        for widget in self.corps_frame.winfo_children():
            widget.destroy()

        self.select_frame = tk.Frame(self.corps_frame, width=900, height=275, bg="blue")
        self.select_frame.grid(row=0, column=0)
        self.modif_frame = tk.Frame(self.corps_frame, width=900, height=275, bg="orange")
        self.modif_frame.grid(row=0, column=1)

        self.bu = Connexion.show_bus()
        self.combo = ttk.Combobox(self.select_frame, values = self.bu, state='readonly', postcommand=lambda: self.combo.config(values=Connexion.show_bus()))
        self.combo.config(width=20, font=('Helvetica', 12))
        self.combo.grid(padx=20, pady = 10, row=0, column=0)


        def truc():
            popo = Connexion.get_bus_modif

            self.plaque = PlaceholderEntry(self.modif_frame, popo.immatriculation)
            self.plaque.grid(row=0, column=0, padx=20, pady=20)
            self.n_place = PlaceholderEntry(self.modif_frame, "Nombre de place")
            self.n_place.grid(row=1, column=0, padx=20, pady=20)
            self.combot = PlaceholderEntry(self.modif_frame, "id_ligne")
            self.combot.grid(row=2, column=0, padx=20, pady=20)
            self.modif_bus = tk.Button(self.modif_frame, text="Modifier", command=lambda: Connexion.modif_bus(self.numero.get(), self.plaque.get(), self.n_place.get(), self.combot.get()))
            self.modif_bus.grid(row=3, column=0, padx=35)


        self.select_frame.grid_columnconfigure(0, minsize=450)
        self.modif_frame.grid_columnconfigure(0, minsize=450)














# inpname = PlaceholderEntry(inpframe, "texte à afficher", font=("Helvetica", "8", "italic"))
# inpname.pack(pady=5)
# inpnum = PlaceholderEntry(inpframe, "texte à texte", font=("Helvetica", "8", "italic"))
# inpnum.pack()
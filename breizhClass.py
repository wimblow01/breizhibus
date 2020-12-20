from tkinter import ttk

class Arret():

    def __init__(self, id, name, adresse):
        self.id=id
        self.name=name
        self.adresse=adresse

    def __repr__(self):
        return self.name + "-" + self.adresse + "\n"

class Bus():

    def __init__(self, id, numero, plaque, place):
        self.id=id
        self.numero=numero
        self.plaque=plaque
        self.place=place

    def __repr__(self):
        # return self.numero + "-" + self.plaque + "\n"
        return self.numero 


class Ligne():

    def __init__(self, ligne):
        self.id=id
        self.ligne=ligne

    def __repr__(self):
        return self.ligne 
    

class BusLigne():

    def __init__(self, id, numero, plaque, place, id_ligne):
        self.id=id
        self.numero=numero
        self.plaque=plaque
        self.place=place
        self.id_ligne=id_ligne


class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.placeholder = placeholder
        self.field_style = kwargs.pop("style", "TEntry")
        self.placeholder_style = kwargs.pop("placeholder_style", self.field_style)
        self["style"] = self.placeholder_style
        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
    def _clear_placeholder(self, e):
        if self["style"] == self.placeholder_style:
            self.delete("0", "end")
            self["style"] = self.field_style
    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = self.placeholder_style

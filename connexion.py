import mysql.connector
import tkinter as tk
from breizhClass import Arret, Bus, Ligne, BusLigne

class Connexion:
    

    @classmethod
    def connect(cls):
        cls.bdd = mysql.connector.connect(
            user='root', 
            password='root', 
            host='localhost', 
            port='8081',
            database='breizhibus', 
            raise_on_warnings=True)
        cls.cursor = cls.bdd.cursor()
        # print("Connexion réussie")
    
    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.bdd.close()

    @classmethod
    def get_ligne(cls):
        cls.connect()
        cls.cursor.execute("SELECT * FROM lignes")
        liste_ligne = []

        res = cls.cursor.fetchall()
        for row in res:
            id_p = row[1]
            liste_ligne.append(id_p)
        cls.close()
        return liste_ligne

    # @classmethod
    # def get_lignes(cls):
    #     cls.connect()
    #     cls.cursor.execute("SELECT * FROM lignes")
    #     liste_ligne = []

    #     res = cls.cursor.fetchall()
    #     for row in res:
    #         id = row[0]
    #         ligne = row[1]
    #         ligne = Ligne(id, ligne)
    #         liste_ligne.append(ligne)
    #     cls.close()
    #     return liste_ligne

    @classmethod
    def get_arrets(cls, choix_ligne):
        cls.connect()
        liste_arret = []
        cls.cursor.execute(f"SELECT * FROM arrets\
            JOIN arret_ligne ON arrets.id_arret = arret_ligne.id_arret\
            JOIN lignes ON arret_ligne.id_ligne = lignes.id_ligne\
            WHERE ligne = '{choix_ligne}'")
        
        rep = cls.cursor.fetchall()
        for row in rep:
            id=int(row[0])
            name = str(row[1])
            adresse = str(row[2])
            arret = Arret(id, name, adresse)
            liste_arret.append(arret)
        cls.close()
        return liste_arret


    @classmethod
    def get_bus(cls, choix_ligne):
        cls.connect()
        liste_bus = []
        cls.cursor.execute(f"SELECT * FROM bus\
            JOIN lignes ON bus.id_ligne = lignes.id_ligne\
            WHERE ligne = '{choix_ligne}'")
        
        rep = cls.cursor.fetchall()
        for row in rep:
            id=int(row[0])
            numero=str(row[1])
            plaque=str(row[2])
            place=str(row[3])
            bus = Bus(id,numero,plaque, place)
            liste_bus.append(bus)
        cls.close()
        return liste_bus

    @classmethod
    def show_bus(cls):
        cls.connect()
        liste_bus = []
        cls.cursor.execute(f"SELECT * FROM bus")
        
        rep = cls.cursor.fetchall()
        for row in rep:
            id=int(row[0])
            numero=str(row[1])
            plaque=str(row[2])
            place=str(row[3])
            bus = Bus(id,numero,plaque, place)
            liste_bus.append(bus)
        cls.close()
        return liste_bus

    @classmethod
    def del_bus(cls, choix):
        cls.connect()
        cls.cursor.execute(f"DELETE FROM bus\
            WHERE numero = '{choix}'")
        cls.bdd.commit()
        cls.close()


    @classmethod
    def ajout_bus(cls, numero, immatriculation, nombre_place, ligne ):
        cls.connect()
        # query = f"INSERT iNTO bus VALUES ({numero}, {immatriculation}, {nombre_place}, {id_ligne})"

        # cls.cursor.execute(f"""
        #     INSERT iNTO bus 
        #     VALUES (NULL, '{numero}', '{immatriculation}', '{nombre_place}', '{id_ligne}')
        #     WHERE 
        #     NOT EXISTS (SELECT * FROM bus 
        #     WHERE numero = '{numero}')
        # """)
        print(numero)
        print(immatriculation)
        print(nombre_place)
        print(ligne)
        cls.cursor.execute(f"INSERT iNTO bus \
            VALUES (NULL, '{numero}', '{immatriculation}', '{nombre_place}', '{ligne}')")
        cls.bdd.commit()
        cls.close()

    @classmethod
    def modif_bus(cls, numero, immatriculation, nombre_place, ligne):
        cls.connect()
        cls.cursor.execute(
            f""" UPDATE bus 
            SET (immatriculation = '{immatriculation}', nombre_ligne = '{nombre_place}', id_ligne = '{ligne}') 
            WHERE numero = '{numero}'
            """)
        cls.bdd.commit()
        cls.close()

    @classmethod
    def get_bus_modif(cls, choix_bus):
        cls.connect()
        liste_bus = []
        cls.cursor.execute(
            f"SELECT * FROM bus\
            WHERE numero = '{choix_bus}'")
        
        rep = cls.cursor.fetchall()
        for row in rep:
            id=int(row[0])
            numero=str(row[1])
            plaque=str(row[2])
            place=str(row[3])
            id_ligne=int(row[4])
            bus = BusLigne(id,numero,plaque, place, id_ligne)
            liste_bus.append(bus)
        cls.close()
        return liste_bus
import random
from os import sep
from tkinter.constants import END
import re

class Cromosoma:
    nombre = ""
    kilocalorias = 0
    def __init__(self, nombre, kilocalorias, tipo):
        self.nombre = nombre
        self.kilocalorias = kilocalorias
        self.tipo = tipo

    def printNombre(self):
        print(self.nombre)
    
    def printKilocalorias(self):
        print(self.kilocalorias)

    def printAll(self):
        print(self.kilocalorias, self.nombre, self.tipo)

class Individuos:
    cromosomas = []
    kilocalorias = 0

    def __init__(self, cromosomas):
        self.cromosomas = cromosomas
        pass

    def getKilocalorias(self):
        return self.kilocalorias
    
    def getIngrediente(self, pos):
        return self.cromosomas[pos]
    
    def getIngrediente(self):
        return random.choice(self.cromosomas)

class Subway:
    numIngredietes = 0
    probMutar = 0.0
    prob = 0.0
    numIngredietes = 0
    numSeleccionados = 0
    poblacion = []
    individuos = []

    def __init__(self, nombFich):
        self.abrirFichero(self, nombFich)
        pass

    def abrirFichero(self, nombFich):
        aux = []
        cromosomas = []
        tipo = ""

        with open(nombFich, 'r') as fichero:
            for linea in fichero.readlines():
                aux.append(re.sub(r'\n|\t','',linea))

        for i in aux:
            dat = i.split(sep=':')
            if not (re.match("(-)",dat[0])):
                self.numIngredietes = self.numIngredietes + 1
                nom = dat[0]
                kcal = dat[1]
                cromosomas.append(Cromosoma(nom, kcal, tipo))
            else:
                tipo = re.sub("(-)", "", dat[0])

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


aux = []
with open('SubwayMenu.txt', 'r') as fichero:
    for linea in fichero.readlines():
        aux.append(re.sub(r'\n|\t','',linea))

cromosomas = []
for i in aux:
    dat = i.split(sep=':')
    if not (re.match("(-)",dat[0])):
        nom = dat[0]
        kcal = dat[1]
        cromosomas.append(Cromosoma(nom, kcal, tipo))
    else:
        tipo = re.sub("(-)", "", dat[0])

for cromosoma in cromosomas:
    print(cromosoma.printAll())
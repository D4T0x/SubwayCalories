from random import choice, choices, randint, random
from os import sep
from tkinter.constants import END
import re

class Individuo:
    cromosomas = []
    kilocalorias = 0

    def __init__(self, cromosomas):
        self.cromosomas = cromosomas
        for i in cromosomas:
            queso = 0
            proteina = 0
            if i.nombre == 'Queso' and i.tipo == 'Extra':
                self.kilocalorias += queso
            elif i.nombre == 'Doble Proteina' and i.tipo == 'Extra':
                self.kilocalorias += proteina
            elif i.tipo == 'Proteina':
                proteina = i.kilocalorias
                self.kilocalorias += proteina
            elif i.tipo == 'Queso':
                queso = i.kilocalorias
                self.kilocalorias += queso
            else:
                self.kilocalorias += i.kilocalorias
        pass
    
    #def __init__(self, individuo):
    #    self = individuo
    #    pass
    
    def printCromosomas(self):
        for i in self.cromosomas:
            i.printAll()
    
    def getKilocalorias(self):
        return self.kilocalorias
    
    def getIngrediente(self, pos):
        return self.cromosomas[pos]
    
    def getIngrediente(self):
        return random.choice(self.cromosomas)
    
    
    class Cromosoma:
        nombre = ""
        kilocalorias = 0
        tipo = ''
        def __init__(self, nombre, kilocalorias, tipo):
            self.nombre = nombre
            self.kilocalorias = int(kilocalorias)
            self.tipo = tipo

        def printNombre(self):
            print(self.nombre)

        def printKilocalorias(self):
            print(self.kilocalorias)

        def printAll(self):
            print(self.nombre, self.tipo, self.kilocalorias)
        
        def getTipo(self):
            return self.tipo



class Subway:
    numIngredietes = 1
    probMutar = 0.0
    prob = 0.0
    numSeleccionados = 0
    poblacion = []
    tPoblacion = 5
    cromosomas = []

    def __init__(self, nombFich):
        self.abrirFichero(nombFich)
        #Iniciamos una población del tamaño especificado
        for i in range(self.tPoblacion):
            genotipos = []
            #Generamos individuos con al menos 1 pan distinto
            genotipos.append(choice(self.getListaPan))
            
            
            '''
            if i < 5:
                genotipos.append(self.cromosomas[i])
            else: 
                genotipos.append(self.cromosomas[randint(0, 4)])
            #Añadimos una proteina
            genotipos.append(self.cromosomas[randint(4,11)])
            ingSelect = 2
            while ingSelect < self.numIngredietes:
                genotipos.append(self.cromosomas[randint(12,len(self.cromosomas)-1)])
                ingSelect += 1
            '''
            self.poblacion.append(Individuo(genotipos))
        pass
    
    def getListaPan(self):
        pan = []
        for i in self.cromosomas:
            if i.getTipo() == 'Pan':
                pan.append(i)
        return pan
            
    
    def getPoblacion(self):
        return self.poblacion

    def abrirFichero(self, nombFich):
        aux = []
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
                self.cromosomas.append(Individuo.Cromosoma(nom, kcal, tipo))
            else:
                tipo = re.sub("(-)", "", dat[0])

prueba = Subway('SubwayMenu.txt')
for i in prueba.poblacion:
    print(i.getKilocalorias())
    i.printCromosomas()
#for i in prueba.cromosomas:
#    i.printNombre()
#individuo = prueba.poblacion[1]
#cromosomas = individuo.getCromosomas()
#print(cromosomas[0])
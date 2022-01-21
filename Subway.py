from random import choice, choices, randbytes, randint, random
from os import sep
from tkinter.constants import END
import re

class Individuo:
    cromosomas = []
    kilocalorias = 0

    def __init__(self, cromosomas):
        self.cromosomas = cromosomas
        proteina = 0
        queso = 0
        for i in cromosomas:
            if i.nombre == 'Queso' and i.tipo == 'Extra':
                self.kilocalorias += queso
                i.setKilocalorias(queso)
            elif i.nombre == 'Doble Proteina' and i.tipo == 'Extra':
                self.kilocalorias += proteina
                i.setKilocalorias(proteina)
            elif i.tipo == 'Proteina':
                proteina = i.kilocalorias
                self.kilocalorias += proteina
            elif i.tipo == 'Queso':
                queso = i.kilocalorias
                self.kilocalorias += queso
            else:
                self.kilocalorias += i.kilocalorias
        pass
       
    def printCromosomas(self):
        for i in self.cromosomas:
            i.printAll()
    
    def getKilocalorias(self):
        return self.kilocalorias
    
    def getIngrediente(self, pos):
        return self.cromosomas[pos]
    
    def getIngrediente(self):
        return random.choice(self.cromosomas)
    
    def getCromosoma(self):
        return self.cromosomas
    
    def getCromosomaLen(self):
        contador = 0
        for _ in self.cromosomas:
            contador += 1
        return contador
    
    @staticmethod
    def recombinar(i1, i2):
        i1Len = int(i1.getCromosomaLen()) 
        i2Len = int(i2.getCromosomaLen())
        if i1Len >= i2Len:
            #Generar plantilla
            boleanos = [True, False]
            plantilla = choices(boleanos, k=i1Len)
            ii1 = []
            ii2 = []
            pos = 0
            for i in plantilla:
                if i:
                    ii1.append(i1.cromosomas[pos])
                    if pos < i2Len:
                        ii2.append(i2.cromosomas[pos])
                    pos += 1
                else:
                    if pos < i2Len:
                        ii1.append(i2.cromosomas[pos])
                    ii2.append(i1.cromosomas[pos])
                    pos += 1
            return i1, i2
        else:
            return i1.recombinar(i2, i1)
    
    def mutar(self, cromosomas):
        for i in self.cromosomas:
            if randbytes(1):
                ingredientes, longitud = self.getListaIngredientes(i.getTipo(), cromosomas)
                i = ingredientes[randint(0, longitud-1)]
    
    def getListaIngredientes(self, ingrediente, cromosomas):
        ingredientes = []
        longitud = 0
        for i in cromosomas:
            if i.getTipo() == ingrediente:
                ingredientes.append(i)
                longitud += 1
        return ingredientes, longitud
    
    class Cromosoma:

        nombre = ""
        kilocalorias = 0
        tipo = ''
        def __init__(self, nombre, kilocalorias, tipo):
            self.nombre = nombre
            self.kilocalorias = int(kilocalorias)
            self.tipo = tipo

        def getNombre(self):
            return self.nombre
        
        def setKilocalorias(self, kilocalorias):
            self.kilocalorias = kilocalorias

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
    probMutar = 0.99
    prob = 0.99
    poblacion = []
    tPoblacion = 5
    cromosomas = []
    numGeneraciones = 5
    kilocaloriasDeseadas = 0

    def __init__(self, nombFich, kilocalorias):
        self.kilocaloriasDeseadas = kilocalorias
        self.abrirFichero(nombFich)
        #Iniciamos una población del tamaño especificado
        for i in range(self.tPoblacion):
            genotipos = []
            #Generamos individuos con al menos 1 pan distinto
            lista_pan, longitud = self.getListaIngredientes('Pan')
            genotipos.append(lista_pan[randint(0, longitud-1)])
            #Generamos individuos con ingredientes aleatorios
            lista, longitud = self.getListaIngredientes('Proteina')
            genotipos.append(lista[randint(0, longitud-1)])
            if randbytes(1):
                lista, longitud = self.getListaIngredientes('Queso')
                genotipos.append(lista[randint(0, longitud-1)])
            if randbytes(1):
                lista, longitud = self.getListaIngredientes('Extra')
                genotipos.append(lista[randint(0, longitud-1)])
            if randbytes(1):
                lista, longitud = self.getListaIngredientes('Vegetales')
                for _ in range(randint(0, longitud-1)):
                    if randbytes(1):
                        genotipos.append(lista.pop(randint(0, longitud-1)))
                        longitud -= 1
            if randbytes(1):
                lista, longitud = self.getListaIngredientes('Salsas')
                for _ in range(randint(0, longitud-1)):
                    if randbytes(1):
                        genotipos.append(lista.pop(randint(0, longitud-1)))
                        longitud -= 1
            self.poblacion.append(Individuo(genotipos))
        pass
    
    def getListaIngredientes(self, ingrediente):
        pan = []
        longitud = 0
        for i in self.cromosomas:
            if i.getTipo() == ingrediente:
                pan.append(i)
                longitud += 1
        return pan, longitud       
    
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

    def getMejor(self):
        actual = self.poblacion[0]
        mejor = actual
        contador = 1
        while True:
            if actual.getKilocalorias() <= self.kilocaloriasDeseadas:
                if mejor.getKilocalorias() <= self.kilocaloriasDeseadas:
                    if mejor.getKilocalorias() < actual.getKilocalorias():
                        mejor = actual
            contador += 1
            if contador == 5:
                break
        return mejor
    
    def evolucionar(self):
        generacion = 0
        while generacion <= self.numGeneraciones:
            while True:
                idx1 = randint(0, self.tPoblacion-1)
                idx2 = randint(0, self.tPoblacion-1)
                if idx1 != idx2:
                    break
            #Seleccion
            i1Tmp = self.poblacion[idx1]
            i2Tmp = self.poblacion[idx2]
            #Recombinar
            if random() <= self.prob:
                i1Tmp, i2Tmp = i1Tmp.recombinar(i1Tmp ,i2Tmp)
            #Mutar
            if random() <= self.probMutar:
                i1Tmp.mutar(self.cromosomas)
            generacion += 1
            #Sustituir en poblacion
            if self.poblacion[idx1].getKilocalorias() < self.kilocaloriasDeseadas:
                if i1Tmp.getKilocalorias() < self.kilocaloriasDeseadas:
                    self.poblacion[idx1] = i1Tmp
            elif i1Tmp.getKilocalorias() < self.kilocaloriasDeseadas:
                self.poblacion[idx1] = i1Tmp
            if self.poblacion[idx2].getKilocalorias() < self.kilocaloriasDeseadas:
                if i2Tmp.getKilocalorias() < self.kilocaloriasDeseadas:
                    self.poblacion[idx2] = i2Tmp
            elif i2Tmp.getKilocalorias() < self.kilocaloriasDeseadas:
                self.poblacion[idx2] = i2Tmp

#prueba = Subway('SubwayMenu.txt', 1000)
#prueba.evolucionar()
#mejor = prueba.getMejor()
#print(mejor.getKilocalorias(), mejor.printCromosomas())



#from classes.rastro import *
from random import choice, randint, random

class Corpo:
    def __init__(self, massa, raio, cor=[255, 255, 255], lugar=[100,10], nome='None'):
        self.nome = nome
        self._massa = massa
        self._densidade = massa/raio
        self._raio = raio
        self._cor = cor
        #self._cor = (randint(100,255), randint(100,255), randint(230,255))
        self._tamanho = raio
        self.lugar = lugar
        self.raio = raio
        self._velocidade = [0,0]
        self._aceleracao = [0,0]
        self._lista_rastros = []
        self.append_rastro = [True]

    def update(self, dt, show_rastro=False):
        lugar_antigo = [self.lugar[0], self.lugar[1]]
        
        self._velocidade[0] += self._aceleracao[0] *dt
        self._velocidade[1] += self._aceleracao[1] *dt

        self.lugar[0] += self._velocidade[0] * dt
        self.lugar[1] += self._velocidade[1] * dt

        if show_rastro:
            if len(self._lista_rastros) > 100: self._lista_rastros.remove(self._lista_rastros[0])
            if self.append_rastro[0]:
                self._lista_rastros.append((lugar_antigo, self.lugar[:], self._cor, 1))
                self.append_rastro = [False, False, True]
            else:
                self.append_rastro.remove(self.append_rastro[0])

    def getAceleracao(self): return self._aceleracao
    def getVelocidade(self): return self._velocidade
    def getMassa(self): return self._massa
    def getLugar(self): return self.lugar
    def getRaio(self): return self._raio
    def getTamanho(self): return self._tamanho
    def getCor(self): return self._cor
    def putForca(self, forca, dt=0):
        self._velocidade[0] += (forca[0]/self._massa) *dt
        self._velocidade[1] += (forca[1]/self._massa) *dt

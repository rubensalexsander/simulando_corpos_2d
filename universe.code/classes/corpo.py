
from classes.rastro import *

class Corpo:
    def __init__(self, massa, raio, cor=[255, 255, 255], lugar=[100,10], nome='None'):
        self.nome = nome
        self._massa = massa
        self._densidade = massa/raio
        self._raio = raio
        self._cor = cor
        self._tamanho = raio
        self.lugar = lugar
        self.raio = raio
        self._velocidade = [0,0]
        self._aceleracao = [0,0]
        self.showRastro = True
        self._lista_rastros = []

    def update(self, dt):
        lugarxa = self.lugar[0]
        lugarya = self.lugar[1]
        self._velocidade[0] += self._aceleracao[0] *dt
        self._velocidade[1] += self._aceleracao[1] *dt

        self.lugar[0] += self._velocidade[0] * dt
        self.lugar[1] += self._velocidade[1] * dt
        
        """if self.showRastro:
            
            if len(self._lista_rastros) > 500:
                self._lista_rastros.remove(self._lista_rastros[0])
            self._lista_rastros.append([self._cor,(lugarxa, lugarya), self.lugar, 1])"""
            


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

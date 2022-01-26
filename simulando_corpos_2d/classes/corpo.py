from random import randint

class Corpo:
    def __init__(self, massa, raio, cor=[255, 255, 255], lugar=[100,10], velocidade=[0,0], nome='None'):
        self.nome = nome
        self._massa = massa
        self._densidade = massa/raio
        self._raio = raio
        self._cor = cor
        #self._cor = (randint(100,255), randint(100,255), randint(230,255))
        self._tamanho = raio #mts
        self.lugar = lugar
        self.raio = raio
        self._velocidade = velocidade #m/s
        self._aceleracao = [0,0]
        self._lista_rastros = []

    def update(self, dt, show_rastro=False):
        self._velocidade[0] += self._aceleracao[0] *dt
        self._velocidade[1] += self._aceleracao[1] *dt
        self.lugar[0] += self._velocidade[0] * dt
        self.lugar[1] += self._velocidade[1] * dt

        if show_rastro: self.trail.update(self.lugar[:])
        else: self.trail.trass = []

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

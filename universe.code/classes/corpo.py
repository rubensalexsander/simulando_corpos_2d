from pygame import image, transform
from classes.rastro import *
from math import sqrt

class Corpo:

    def __init__(self, massa, raio, mundo, cor=[255, 255, 255], lugar=[100,10]):
        self._massa = massa
        self._densidade = massa/raio
        self._raio = raio
        self._mundo = mundo
        self._cor = cor
        self._tamanho = raio/mundo.km_pixel
        self._lugar_km = lugar

        self._velocidade = [0,0]
        self._aceleracao = [0,0]
        self._lista_rastros = []
        self._lugar_pixel = [self._lugar_km[0] / self._mundo.km_pixel, self._lugar_km[1] / self._mundo.km_pixel]
        mundo.addCorpo(self)
        #self.img_circulo_gravidade = image.load('circulotransparente.png').convert_alpha()

    def update(self, dt):
        self._tamanho = self._raio / self._mundo.km_pixel

        self._velocidade[0] += self._aceleracao[0] *dt
        self._velocidade[1] += self._aceleracao[1] *dt
        lugarxa = self._lugar_km[0]
        lugarya = self._lugar_km[1]
        self._lugar_km[0] += self._velocidade[0] *dt
        self._lugar_km[1] += self._velocidade[1] *dt

        self._lugar_pixel = [self._lugar_km[0] / self._mundo.km_pixel, self._lugar_km[1] / self._mundo.km_pixel]

        if self._mundo.showRastro:

            if len(self._lista_rastros) > 500:
                self._lista_rastros.remove(self._lista_rastros[0])
            self._lista_rastros.append([self._mundo._display, self._cor,(lugarxa/self._mundo.km_pixel, lugarya/self._mundo.km_pixel), self._lugar_pixel, 1])
            for rastro in self._lista_rastros:
                draw.line(rastro[0], rastro[1], rastro[2], rastro[3], rastro[4])

        if self._mundo.showGravity:

            self.area_gravidade = int(self._raio * 10 / self._mundo.km_pixel)
            self.circulo_gravidade = transform.scale(self.img_circulo_gravidade, [self.area_gravidade, self.area_gravidade])
            #self._mundo.getDisplay()[0].blit(self.circulo_gravidade, (self._lugar_pixel[0]-(self.area_gravidade/2), self._lugar_pixel[1]-(self.area_gravidade/2)))

        #self._sprite = draw.circle(self._mundo.getDisplay()[0], self._cor, self._lugar_pixel, self._tamanho)

    def getAceleracao(self): return self._aceleracao
    def getVelocidade(self): return self._velocidade
    def getMassa(self): return self._massa
    def getLugar(self, qual):
        if qual == 'km':
            return self._lugar_km
        elif qual == 'pixel':
            return self._lugar_pixel
    def getRaio(self): return self._raio
    def getTamanho(self): return self._tamanho
    def getCor(self): return self._cor
    #def getSprite(self): return self._sprite

    def putForca(self, forca, dt=0):
        self._velocidade[0] += (forca[0]/self._massa) *dt
        self._velocidade[1] += (forca[1]/self._massa) *dt

from classes.corpo import Corpo
from math import sqrt
from random import randint
#from libs.rastro_animation import *
from libs.line_trail import *


class Universo:
    G = 6.67408*(10**-11)

    def __init__(self):
        self.corpos = []
        self.showRastro = False
        #self.rastro_animation = Rastro_animation()
        #self.line_trail = Line_trail()

    def update(self, dt, show_rastro=False):
        #self.rastro_animation.update()

        for corpo in self.corpos:
            corpo.update(dt, show_rastro)
            
            for corpo2 in self.corpos:
                if corpo != corpo2:
                    d = self.getD(corpo, corpo2)
                    Fg = self.getFg(corpo, corpo2, d)

                    corpo2.putForca(Fg[1], dt)

                    if d < (corpo._raio+corpo2._raio):
                        massa1, massa2 = corpo.getMassa(), corpo2.getMassa()
                        massas = massa1+massa2

                        cor1, cor2 = corpo.getCor(), corpo2.getCor()
                        cor = int((cor1[0]*massa1+cor2[0]*massa2)/massas), int((cor1[1]*massa1+cor2[1]*massa2)/massas), int((cor1[2]*massa1+cor2[2]*massa2)/massas)
                        
                        velocidade = [((corpo._velocidade[0]*massa1+corpo2._velocidade[0]*massa2)/massas), ((corpo._velocidade[1]*massa1+corpo2._velocidade[1]*massa2)/massas)]
                        
                        lugar1, lugar2 = corpo.lugar, corpo2.lugar
                        lugar = [int((lugar1[0]*massa1+lugar2[0]*massa2)/massas), 
                                int((lugar1[1]*massa1+lugar2[1]*massa2)/massas)]

                        raio1, raio2 = corpo.getRaio(), corpo2.getRaio()
                        raios = raio1
                        if raio1 < raio2:
                            raios=raio2

                        new_corpo = self.new_corpo(
                            massa=massas, 
                            raio=raios, 
                            lugar=lugar,
                            velocidade=velocidade,
                            cor=cor, 
                            nome=corpo.nome)
                        
                        new_corpo.trail.trass = corpo.trail.trass+corpo2.trail.trass

                        try:
                            self.corpos.remove(corpo)
                            self.corpos.remove(corpo2)
                        except: 
                            pass

                        break
    
    def getD(self, corpo1, corpo2):
        lugar1, lugar2 = corpo1.getLugar(), corpo2.getLugar()
        d = sqrt((lugar1[0]-lugar2[0])**2+(lugar1[1]-lugar2[1])**2)
        return d

    def getFg(self, corpo1, corpo2, d):
        m1, m2 = corpo1.getMassa(), corpo2.getMassa()
        lugar1, lugar2 = corpo1.getLugar(), corpo2.getLugar()
        dx = lugar2[0]-lugar1[0]
        dy = lugar2[1]-lugar1[1]
        Fg = (self.G*m1*m2)/d**2
        Fx = -dx*(Fg/(abs(dx)+abs(dy)))
        Fy = -dy*(Fg/(abs(dx)+abs(dy)))
        return Fg, [Fx, Fy]

    def new_corpo(self, massa=1, raio=1000, cor=[255, 255, 255], lugar=[0,0], velocidade=[0,0], nome='None'):
        corpo = Corpo(massa=massa, raio=raio, lugar=lugar, velocidade=velocidade, cor=cor, nome=nome)
        self.corpos.append(corpo)
        corpo.trail = Trail(corpo._cor, 1)
        return corpo

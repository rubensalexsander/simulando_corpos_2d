from math import sqrt


class Mundo:
    G = 6.67408*(10**-11)
    #img_circulo_gravidade = image.load('circulodegravidade.png')
    def getD(self, corpo1, corpo2):
        lugar1, lugar2 = corpo1.getLugar('km'), corpo2.getLugar('km')
        d = sqrt((lugar1[0]-lugar2[0])**2+(lugar1[1]-lugar2[1])**2)
        return d
    def getFg(self, corpo1, corpo2, d):
        m1, m2 = corpo1.getMassa(), corpo2.getMassa()
        lugar1, lugar2 = corpo1.getLugar('km'), corpo2.getLugar('km')
        dx = lugar2[0]-lugar1[0]
        dy = lugar2[1]-lugar1[1]
        Fg = (self.G*m1*m2)/d**2
        Fx = -dx*(Fg/(abs(dx)+abs(dy)))
        Fy = -dy*(Fg/(abs(dx)+abs(dy)))
        return Fg, [Fx, Fy]

    def __init__(self, resolucao, zoom=1, visualizar=1000):
        self.visualizar = visualizar
        self.km_pixel = visualizar/resolucao[0]
        # Cria tela de jogo
        self._resolucao = resolucao
        '''self._display = display
        self._display.set_caption('Mundo')
        self._display = self._display.set_mode(resolucao)'''
        self._zoom = zoom
        # Define dados
        self._lista_corpos = []
        #self.metro = ((resolucao[0]+resolucao[1])*zoom)/80000
        # -----------------------------------------
        self.GRAVITY = 30
        self.showGravity = False
        self.showRastro = False

    def update(self, dt):
        self.km_pixel = self.visualizar / self._resolucao[0]

        # Blit corpos
        for corpo in self._lista_corpos:
            corpo.update(dt)
            for corpo2 in self._lista_corpos:

                if corpo != corpo2:
                    d = self.getD(corpo, corpo2)

                    Fg = self.getFg(corpo, corpo2, d)
                    corpo2.putForca(Fg[1], dt)

                    if d < (corpo._raio+corpo2._raio):
                        massa1 = corpo.getMassa()
                        massa2 = corpo2.getMassa()
                        massas = massa1+massa2
                        cor1 = corpo.getCor()
                        cor2 = corpo2.getCor()
                        cor = int((cor1[0]*massa1+cor2[0]*massa2)/massas), int((cor1[1]*massa1+cor2[1]*massa2)/massas), int((cor1[2]*massa1+cor2[2]*massa2)/massas)
                        velocidade = [((corpo._velocidade[0]*massa1+corpo2._velocidade[0]*massa2)/massas), ((corpo._velocidade[1]*massa1+corpo2._velocidade[1]*massa2)/massas)]
                        lugar1 = corpo._lugar_km
                        lugar2 = corpo2._lugar_km
                        lugar = [(lugar1[0]*massa1+lugar2[0]*massa2)/massas, (lugar1[1]*massa1+lugar1[1]*massa2)/massas]

                        maior = corpo
                        menor = corpo2

                        if massa1 < massa2:
                            maior = corpo2
                            menor = corpo

                        raio1 = maior.getRaio()
                        raio2 = menor.getRaio()
                        raios = raio1 + ((raio1+raio2)/raio1)

                        maior._massa = massas
                        maior._raio = raios
                        maior._cor = cor
                        #maior._lugar_km = lugar
                        maior.putForca([menor._velocidade[0]*menor._massa, menor._velocidade[1]*menor._massa], dt)
                        maior._velocidade = velocidade

                        try:
                            self._lista_corpos.remove(menor)
                        except: pass

                        break


    def getListadecorpos(self):
        return self._lista_corpos

    def setListadecorpos(self, listaDecorpos):
        self.listaCorpos = listaDecorpos

    def addCorpo(self, corpo):
        self._lista_corpos.append(corpo)

    def getDisplay(self): return 0, self._resolucao

    def setVisualizar(self, visualizar): self.visualizar = visualizar
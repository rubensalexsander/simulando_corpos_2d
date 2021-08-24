from pygame import draw

class Rastro():
    def __init__(self, corpo):
        self._corpo = corpo
        self._cor = corpo.getCor()
        self._lugar_km_rastro = [int(corpo.getLugar('km')[0]), int(corpo.getLugar('km')[1])]
        self.lugarkmbackup = [str(self._lugar_km_rastro[0]), str(self._lugar_km_rastro[1])]

    def update(self):
        self._lugar_pixel = [self._lugar_km_rastro[0]/self._corpo._mundo.km_pixel, self._lugar_km_rastro[1]/self._corpo._mundo.km_pixel]
        self._tamanho = int(self._corpo.getRaio()/5 / self._corpo._mundo.km_pixel) + 1
        self._tamanho = 1
        draw.circle(self._corpo._mundo.getDisplay()[0], self._cor, self._lugar_pixel, self._tamanho)

    def getLugar(self, qual):
        if qual == 'km': return self._lugar_km_rastro
        elif qual == 'pixel': return self._lugar_pixel

    def excluir(self):
        pass
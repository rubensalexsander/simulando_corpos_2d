from random import randint

class Rastro:
    def __init__(self, tipo='line', lugar=[200, 200], cor=(255,255,255), comprimento=20, velocidade=5):
        self.type = tipo
        self.lugar = lugar
        self.cor = cor
        self.comprimento = comprimento
        self.velocidade = velocidade
        self.frags = []
    
    def update(self, ):
        self.novo_frag()

        for frag in self.frags:
            frag['lugar'][0] -= frag['velocidade'][0]
            frag['lugar'][1] -= frag['velocidade'][1]

            frag['velocidade'][0] *= 0.9
            frag['velocidade'][1] *= 0.9

            frag['tamanho'] -= 1

            if frag['tamanho'] < 0:
                self.frags.remove(frag)
    
    def novo_frag(self):

        if self.type == 'line':


        elif self.type == 'fragment':
            a = randint(30, 100)/100

            frag = {
                'lugar':[self.lugar[0], self.lugar[1]],
                'cor':(self.cor[0]*a,self.cor[1]*a,self.cor[2]*a),
                'velocidade':[randint(-100, 100), randint(-1000, 1000)],
                'tamanho':randint(5,self.comprimento),
            }

        self.frags.append(frag)

class Rastro_animation:
    def __init__(self):
        self.rastros = []
    
    def new_rastro(self, lugar=[200, 200], cor=(0,250,0), comprimento=10, velocidade=5):
        rastro = Rastro(lugar=lugar, cor=cor, comprimento=comprimento, velocidade=velocidade)
        self.rastros.append(rastro)
        return rastro
    
    def update(self):
        for rastro in self.rastros:
            rastro.update()
    
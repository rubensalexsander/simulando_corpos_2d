from libs.arFront import *
from classes.universo import Universo
from classes.corpo import Corpo
from time import time
from random import randint
from utils import *

#Variáveis--------
zoom = 500000 #Zoom inicial
centroTela = [int(zoom/2), int(zoom/2)] #Local de início ---
#centroTela = [-10000000, -10000000]
changeCenter = None
changeZoom = None
show_squadinfors = False
show_rastro = False

def criaCorpos():
    corpos = []
    terra = Corpo((5.972 * (10**24)), raio=6500, lugar=[250000, 250000], cor=(0, 0, 255), nome='Terra')
    terra._velocidade = [0, 0]
    corpo1 = Corpo((5.972 * (9**24)), raio=4000, lugar=[400000, 300000], cor=(200, 200, 255), nome='corpo1')
    corpo1._velocidade = [35000, -35000]
    corpo2 = Corpo((5.972 * (9**24)), raio=2500, lugar=[200000, 400000], cor=(150, 255, 180), nome='corpo2')
    corpo2._velocidade = [-45000, -2000]
    corpo3 = Corpo((5.972 * (7**24)), raio=2200, lugar=[500000, 10000], cor=(50, 100, 155), nome='corpo3')
    corpo3._velocidade = [-23000, -8500]
    corpo4 = Corpo((5.972 * (7**24)), raio=2200, lugar=[300000, 50000], cor=(250, 100, 155), nome='corpo4')
    corpo4._velocidade = [30000, -2500]
    corpo5 = Corpo((5.972 * (6**24)), raio=3200, lugar=[100000, 10000], cor=(150, 180, 155), nome='corpo5')
    corpo5._velocidade = [30000, -8500]
    corpo6 = Corpo((5.972 * (8**24)), raio=2200, lugar=[500000, 50000], cor=(50, 100, 155), nome='corpo6')
    corpo6._velocidade = [-20000, -5500]
    corpo7 = Corpo((5.972 * (7**24)), raio=2200, lugar=[300000, 10000], cor=(150, 200, 255), nome='corpo7')
    corpo7._velocidade = [-25000, -8500]

    corpos.append(terra)
    corpos.append(corpo1)
    corpos.append(corpo2)
    corpos.append(corpo3)
    corpos.append(corpo4)
    corpos.append(corpo5)
    corpos.append(corpo6)
    corpos.append(corpo7)
    
    return corpos

#Definições-------
mouse = ()
universo = Universo(corpos=criaCorpos())
#-----------------
#Times------------
tempo_inicio = time()
#-----------------

corpo_seguir = universo.corpos[0]
seguir = False

app = App(nomeJanela='Simulando corpos em Python :P', tema=universeCodeTheme, resolucao=[800,600])
app.FPS_rate = 60
app.txFps.active = True
app.txARTI.active = True
app.txARTI.tamanho = 10

def finalizar():
    return 'finish'

btFinalizar = app.novoBotao(
    string='X',
    tamanhoTexto=20,
    lugar=[0.995, 0.01],
    tamanho = [40, 40],
    corTexto=(255,0,0),
    command=finalizar,
    refer='nr',
    bordas=1,
    corBordas=(255,0,0)
)

def centerUP():
        centroTela[1] -= zoom/10

btCenterUP = app.novoBotao(
    lugar=[0.15, -0.01],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.7, 0.1],
    command=centerUP,
    string='UP',
    tamanhoTexto=18,
    end_draw=True)

def centerDOWN():
    centroTela[1] += zoom/10

btCenterDOWN = app.novoBotao(
    lugar=[0.15, 0.91],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.7, 0.1],
    command=centerDOWN,
    string='DOWN',
    tamanhoTexto=18,
    end_draw=True)

def centerLEFT():
        centroTela[0] -= zoom/10

btCenterLEFT = app.novoBotao(
    lugar=[-0.01, 0.15],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.1, 0.7],
    command=centerLEFT,
    string='LEFT',
    tamanhoTexto=18,
    end_draw=True)

def centerRIGHT():
    centroTela[0] += zoom/10

btCenterRIGHT = app.novoBotao(
    lugar=[0.91, 0.15],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.1, 0.7],
    command=centerRIGHT,
    string='RIGHT',
    tamanhoTexto=18,
    end_draw=True)

txZoom = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 30]
)

sqZoom = app.novoSquare(
    lugar=[0.99, 0.99],
    refer='sr',
    tamanho=[0.12,50],
    cor=(-1,-1,-1),
    bordas=1,
    corBordas=app.cor_back_secundaria,
    active=False
)

def menosZoom():
    global zoom
    zoom += zoom * 0.25

btMenosZoom = app.novoBotao(
    string='-',
    lugar=[0.91, 0.99],
    tamanho=[30,50],
    tamanhoTexto=25,
    refer='sr',
    cor=(-1,-1,-1),
    bordas=1,
    command=menosZoom
)

def maisZoom():
    global zoom
    zoom -= zoom * 0.25

btMaisZoom = app.novoBotao(
    string='+',
    lugar=[0.98, 0.99],
    tamanho=[30,50],
    tamanhoTexto=25,
    refer='sr',
    cor=(-1,-1,-1),
    bordas=1,
    command=maisZoom
)

txBtZoom = app.novoTexto(
    lugar=[0.975, 0.9],
    refer='sr',
    string='ZOOM',
    cor=app.cor_back_secundaria
)

def change_rastro():
    global show_rastro
    if show_rastro:
        show_rastro = False
    else:
        show_rastro = True

bt_rastro = app.novoBotao(
    lugar=[0.01, 0.86],
    tamanho=[85,30],
    string='Rastro',
    command=change_rastro
)

def change_infors():
    global show_squadinfors
    if show_squadinfors:
        show_squadinfors = False
    else:
        show_squadinfors = True

bt_infors = app.novoBotao(
    lugar=[0.01, 0.925],
    tamanho=[85,30],
    string='Informações',
    command=change_infors
)

#Loop de game
running = True
while running:

    if not seguir:
        if changeCenter == 'btChangecenterCima':
            centroTela[1] -= zoom/100
        elif changeCenter == 'btChangecenterBaixo':
            centroTela[1] += zoom/100
        elif changeCenter == 'btChangecenterLeft':
            centroTela[0] -= zoom/100
        elif changeCenter == 'btChangecenterRight':
            centroTela[0] += zoom/100

    if seguir:
        centroTela = corpo_seguir.lugar
    
    txZoom.string = 'Zoom: ' + getStringdist(zoom)

    if app.FPS:
        universo.update(1 / app.FPS, show_rastro)
    
    # Escreve corpos
    for corpo in universo.corpos:
        tamanho_corpo = corpo.getTamanho()
        lugar_corpo = corpo.getLugar()
        tamanhoCorpoPixel = distanciaKmToPixel(tamanho_corpo, app.resolucao[0], zoom)
        lugarCorpoPixel = getLugarPixel([lugar_corpo[0]-centroTela[0], lugar_corpo[1]-centroTela[1]], app.resolucao, zoom)

        app.drawCircle(corpo.getCor(), lugarCorpoPixel, tamanhoCorpoPixel)

        if show_squadinfors:
            #Escrve squadInfors
            app.drawSquare(
                lugar=lugarCorpoPixel,
                refer='c',
                cor=(-1,-1,-1),
                bordas=1,
                corBordas=(0,255,0)
            )

            app.drawText(
                string=corpo.nome,
                lugar=[lugarCorpoPixel[0]-10, lugarCorpoPixel[1]-25],
                refer='c',
                cor=(0,255,0),
                tamanho=10
            )
        
        if show_rastro:
            
            for linha in corpo._lista_rastros:
                tamanho_screen = app.screen.get_size()
                ponto1 = getLugarPixel([linha[0][0]-centroTela[0], linha[0][1]-centroTela[1]], app.resolucao, zoom)
                ponto2 = getLugarPixel([linha[1][0]-centroTela[0], linha[1][1]-centroTela[1]], app.resolucao, zoom)
                
                app.drawLine(
                    ponto1,
                    ponto2,
                    linha[2],
                    linha[3]
                    )

    saida = app.update()

    if saida == 'finish':
        running = False

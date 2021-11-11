from libs.arFront import *
from classes.universo import Universo
from classes.corpo import Corpo
from time import time
from random import randint
from utils import *

#Variáveis--------
zoom = 500000 #Zoom inicial
centroTela = [int(zoom/2), int(zoom/2)] #Local de início
#centroTela = [-10000000, -10000000]
changeCenter = None
changeZoom = None
show_squadinfors = True

def criaCorpos():
    corpos = []
    lua5 = Corpo((9.34 * (10**19)), raio=1737, lugar=[250000, 400000], cor=(0, 255, 50), nome='Lua')
    lua5.putForca([555**9,200**9], 1)
    lua6 = Corpo((7.34 * (10**19)), raio=1737, lugar=[350000, 150000], cor=(255, 145, 150), nome='Lua')
    lua6.putForca([-530**9,200**9], 1)
    lua7 = Corpo((7.34 * (10**19)), raio=1737, lugar=[250000, 150000], cor=(255, 255, 100), nome='Lua')
    lua7.putForca([530**9,200**9], 1)
    corpo8 = Corpo((12.34 * (10**19)), raio=2737, lugar=[400000, 400000], cor=(100, 150, 200), nome='Lua')
    corpo8.putForca([-540**9,100**9], 1)
    terra = Corpo((5.972 * (10**24)), raio=6371, lugar=[zoom/2, zoom/2], cor=(0, 0, 255), nome='Terra')
    terra._velocidade = [-500, 200]
    terra2 = Corpo((7.972 * (10**20)), raio=3371, lugar=[int(zoom*0.3), int(zoom*0.2)], cor=(230, 170, 50), nome='Terra')
    terra2._velocidade = [25000, 200]

    corpos.append(lua5)
    corpos.append(lua6)
    corpos.append(lua7)
    corpos.append(corpo8)
    corpos.append(terra)
    corpos.append(terra2)
    
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

app = App(nomeJanela='Universe.code :P', tema=universeCodeTheme, resolucao=[800,600])
app.FPS_rate = 60
app.txFps.active = True
app.txARTI.active = True
app.txARTI.tamanho = 10

def finalizar():
    return 'finish'

btFinalizar = app.novoBotao(
    string='EXIT',
    lugar=[0.9, 0.01],
    tamanho = [0.075,0.085],
    corTexto=(255,0,0),
    command=finalizar,
)

def centerUP():
        centroTela[1] -= zoom/100

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
        centroTela[1] += zoom/100

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
        centroTela[0] -= zoom/100

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
        centroTela[0] += zoom/100

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

#sqTeste = app.novoSquare(lugar=[0.5,0.5])

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
    
    if changeZoom == 'btMaisZoom':
        zoom -= zoom*0.025
    elif changeZoom == 'btMenosZoom':
        zoom += zoom*0.025

    if seguir:
        centroTela = corpo_seguir.lugar

    if app.FPS:
        universo.update(1 / app.FPS)
    
    # Escreve corpos
    for corpo in universo.corpos:
        tamanhoCorpoPixel = distanciaKmToPixel(corpo.getTamanho(), app.resolucao[0], zoom)
        lugarCorpoPixel = getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], app.resolucao, zoom)

        app.drawCircle(corpo.getCor(), lugarCorpoPixel, tamanhoCorpoPixel)

    saida = app.update()

    if saida == 'finish':
        running = False

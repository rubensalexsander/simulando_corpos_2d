from libs.arFront import *
from classes.universo import Universo
from classes.corpo import Corpo
from time import time
from utils import *
import random

def criaCorpos(universo1):
    corpo1 = universo1.new_corpo(
        massa=(5972 * (8**24)), 
        raio=8000, 
        lugar=[100000, 100000], 
        cor=(200, 200, 255),
        velocidade=[5000, 0], 
        nome='corpo1')
    
    corpo2 = universo1.new_corpo(
        massa=(555.972 * (7**24)), 
        raio=4000, 
        lugar=[300000, 300000],
        velocidade=[-45000, 12000],
        cor=(150, 100, 255), 
        nome='corpo2')
    
    corpo3 = universo1.new_corpo(
        massa=(455.972 * (7**24)), 
        raio=5000, 
        lugar=[100000, 600000],
        velocidade=[40000, -2000],
        cor=(250, 255, 255), 
        nome='corpo3')
    
    corpo4 = universo1.new_corpo(
        massa=(355.972 * (7**24)), 
        raio=5000, 
        lugar=[200000, 500000],
        velocidade=[35000, 0],
        cor=(150, 155, 255), 
        nome='corpo4')
    
    corpo5 = universo1.new_corpo(
        massa=(255.972 * (7**24)), 
        raio=7000, 
        lugar=[0, 600000],
        velocidade=[-25000, -40000],
        cor=(155, 90, 255), 
        nome='corpo5')
    
    corpo6 = universo1.new_corpo(
        massa=(355.972 * (8**24)), 
        raio=7000, 
        lugar=[400000, 800000],
        velocidade=[-30000, 10000],
        cor=(200, 205, 195), 
        nome='corpo6')
    corpo7 = universo1.new_corpo(
        massa=(255.972 * (7**24)), 
        raio=7000, 
        lugar=[-100000, 200000],
        velocidade=[-65000, -70000],
        cor=(255, 190, 155), 
        nome='corpo7')
    corpo8 = universo1.new_corpo(
        massa=(255.972 * (7**24)), 
        raio=7000, 
        lugar=[300000, 600000],
        velocidade=[-25000, -20000],
        cor=(200, 190, 155), 
        nome='corpo8')
    
    #universo1.new
    
    terra = Corpo((5972 * (10**24)), raio=6371, lugar=[0, 0], cor=(0, 0, 255), nome='Terra')
    terra._velocidade = [15000, 24000]
    #lugar = [384400, 0], Massa = 7,349 x 10^22, Raio = 17374
    lua = Corpo((7349 * (10**22)), raio=1737, lugar=[406000, 0], cor=(200, 200, 200), nome='Lua')
    lua._velocidade = [0, -10904000+(447920)]

    #Lugar = [-149600000, 0], Massa = 1,989 × 10^30, Raio = 696.340
    sol = Corpo((1989 * (10**30)), raio=696340, lugar=[-152100000, 0], cor=(255, 255, 0), nome='Sol')
    sol._velocidade = [0, 500000]
    
#Variáveis--------
mouse = ()
universo1 = Universo()
criaCorpos(universo1)
app = App(nomeJanela='Simulando corpos em Python :P', tema=universeCodeTheme, resolucao=[800,600])
app.txARTI.active = False

#Definições iniciais-------
zoom = 400000 #Zoom inicial
centroTela = [0, 0] #Local de início ---
corpo_seguir = 0
seguir = True
show_squadinfors = False
show_rastro = False
app.FPS_rate = 60
app.txFps.active = True
#--------------------------

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
    lugar=[0.35, -0.01],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.3, 0.1],
    command=centerUP,
    string='UP',
    tamanhoTexto=18,
    end_draw=True)

def centerDOWN():
    centroTela[1] += zoom/10

btCenterDOWN = app.novoBotao(
    lugar=[0.35, 0.91],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.3, 0.1],
    command=centerDOWN,
    string='DOWN',
    tamanhoTexto=18,
    end_draw=True)

def centerLEFT():
        centroTela[0] -= zoom/10

btCenterLEFT = app.novoBotao(
    lugar=[-0.01, 0.35],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.1, 0.3],
    command=centerLEFT,
    string='LEFT',
    tamanhoTexto=18,
    end_draw=True)

def centerRIGHT():
    centroTela[0] += zoom/10

btCenterRIGHT = app.novoBotao(
    lugar=[0.91, 0.35],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.1, 0.3],
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
    if show_rastro: show_rastro = False
    else: show_rastro = True

bt_rastro = app.novoBotao(
    lugar=[0.01, 0.86],
    tamanho=[85,30],
    string='Rastro',
    command=change_rastro
)

def change_infors():
    global show_squadinfors
    if show_squadinfors: show_squadinfors = False
    else: show_squadinfors = True

bt_infors = app.novoBotao(
    lugar=[0.01, 0.925],
    tamanho=[85,30],
    string='Informações',
    command=change_infors
)


tx_time = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 50]
)

tx_corpos = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 70]
)

iniciou = False

#Loop de game
running = True
while running:
    if seguir:
        centroTela = universo1.corpos[corpo_seguir].lugar[:]
    
    txZoom.string = 'Zoom: ' + getStringdist(zoom)
    tx_corpos.string = 'N corpos: ' + str(len(universo1.corpos))

    if app.FPS:
        if not iniciou:
            iniciou = True
            time_inicio = time()
        universo1.update(1 / app.FPS, show_rastro)
        tx_time.string = f'Tempo: {round(time()-time_inicio, 1)}'
    
    # Escreve corpos
    for corpo in universo1.corpos:
        if show_rastro:
            for trass in corpo.trail.trass:
                tamanho_screen = app.screen.get_size()
                ponto1 = getLugarPixel([trass['pt1'][0]-centroTela[0], trass['pt1'][1]-centroTela[1]], app.resolucao, zoom)
                ponto2 = getLugarPixel([trass['pt2'][0]-centroTela[0], trass['pt2'][1]-centroTela[1]], app.resolucao, zoom)

                app.drawLine(ponto1, ponto2, trass['color'], trass['thickness'])
            
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

    saida = app.update()

    if saida == 'finish':
        running = False

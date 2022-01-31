from time import time
from utils import *
from classes.universo import Universo
from interface_front import *
import faz_corpos
    
#Variáveis--------
mouse = ()
universo1 = Universo()
#criaCorpos(universo1)
faz_corpos.manual(universo1)

#Definições iniciais-------
zoom = 500000 #Zoom inicia
centroTela = [0, 0] #Local de início ---
corpo_seguir = 0
seguir = False
show_squadinfors = False
show_rastro = False
show_orientation = False
pause = True
iniciou = False

def pausar():
    global pause
    if pause:
        pause = False
        btPause.cor = (-1,-1,-1)
        btPause.corTexto = app.cor_texto
    else:
        pause = True
        btPause.cor = app.cor_texto
        btPause.corTexto = app.cor_bt
    app.update()
btPause.command = pausar

def menosZoom():
    global zoom
    zoom += zoom * 0.25
btMenosZoom.command = menosZoom

def maisZoom():
    global zoom
    zoom -= zoom * 0.25
btMaisZoom.command = maisZoom

def change_rastro():
    global show_rastro
    if show_rastro: 
        show_rastro = False
        bt_rastro.cor = (-1,-1,-1)
        bt_rastro.corTexto = app.cor_texto
    else: 
        show_rastro = True
        bt_rastro.cor = app.cor_texto
        bt_rastro.corTexto = app.cor_bt
bt_rastro.command = change_rastro

def change_infors():
    global show_squadinfors
    global bt_infors
    if show_squadinfors: 
        show_squadinfors = False
        bt_infors.cor = (-1,-1,-1)
        bt_infors.corTexto = app.cor_texto
    else: 
        show_squadinfors = True
        bt_infors.cor = app.cor_texto
        bt_infors.corTexto = app.cor_bt
bt_infors.command = change_infors

def change_orientation():
    global show_orientation
    if show_orientation: 
        show_orientation = False
        bt_orientation.cor = (-1,-1,-1)
        bt_orientation.corTexto = app.cor_texto
    else: 
        show_orientation = True
        bt_orientation.cor = app.cor_texto
        bt_orientation.corTexto = app.cor_bt
bt_orientation.command = change_orientation

def centerUP():
    centroTela[1] -= zoom/10
btCenterUP.command = centerUP

def centerDOWN():
    centroTela[1] += zoom/10
btCenterDOWN.command = centerDOWN

def centerLEFT():
    centroTela[0] -= zoom/10
btCenterLEFT.command = centerLEFT

def centerRIGHT():
    centroTela[0] += zoom/10
btCenterRIGHT.command = centerRIGHT

#Loop de game
running = True
while running:

    if app.FPS:
        if not iniciou:
            iniciou = True
            time_inicio = time()
        universo1.update((1 / app.FPS), show_rastro, pause)
        tx_time.string = f'Tempo: {round(time()-time_inicio, 1)}s'
    
    if seguir:
        centroTela = universo1.corpos[corpo_seguir].lugar[:]
    
    txZoom.string = 'Zoom: ' + getStringdist(zoom)
    tx_corpos.string = 'N corpos: ' + str(len(universo1.corpos))
    
    # Escreve corpos
    for corpo in universo1.corpos:
        tamanho_corpo = corpo.getTamanho()
        lugar_corpo = corpo.getLugar()
        tamanhoCorpoPixel = distanciaKmToPixel(tamanho_corpo, app.resolucao[0], zoom)
        lugarCorpoPixel = getLugarPixel([lugar_corpo[0]-centroTela[0], lugar_corpo[1]-centroTela[1]], app.resolucao, zoom)
    
        if tamanhoCorpoPixel:
            app.drawCircle(corpo.getCor(), lugarCorpoPixel, tamanhoCorpoPixel)
        else:
            app.drawLine(lugarCorpoPixel, lugarCorpoPixel, corpo.getCor(), 1)

        if show_rastro:
            for trass in corpo.trail.trass:
                tamanho_screen = app.screen.get_size()
                ponto1 = getLugarPixel([trass['pt1'][0]-centroTela[0], trass['pt1'][1]-centroTela[1]], app.resolucao, zoom)
                ponto2 = getLugarPixel([trass['pt2'][0]-centroTela[0], trass['pt2'][1]-centroTela[1]], app.resolucao, zoom)
                app.drawLine(ponto1, ponto2, trass['color'], trass['thickness'])

        if show_orientation:
            vel_corpo = corpo.getVelocidade()[:]
            total_vel = abs(vel_corpo[0]) + abs(vel_corpo[1]) + 1
            tamanho_seta = 30
            seta_x = vel_corpo[0]/total_vel
            seta_y = vel_corpo[1]/total_vel
            app.drawLine(lugarCorpoPixel, [lugarCorpoPixel[0]+(seta_x*tamanho_seta), lugarCorpoPixel[1]+(seta_y*tamanho_seta)])

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

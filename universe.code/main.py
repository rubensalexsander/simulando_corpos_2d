import pygame
from pygame import draw
from classes.universo import Universo
from classes.corpo import Corpo
from classes.botao import Botao
from classes.mouse import Mouse
from time import time
from utils import *

#Configurações----
tamanhoTela = [700,700]
FPS_rate=30000
segundos_de_simulacao = 18000
show_squadinfors = False

corUniverso = (3, 6, 13)
corPrimaria = (13, 16, 23)
corSecundaria = (22, 27, 34)
corTextoPrimaria = (88, 166, 255)
corTextoSecundaria = (53, 114, 165)
corBranco = (255, 255, 255)

font = 'ARIAL'
tamanhoTexto = 0.1
#-----------------
#Variáveis--------
zoom = 500000 #Zoom inicial
centroTela = [int(zoom/2), int(zoom/2)] #Local de início
#centroTela = [-10000000, -10000000]
changeCenter = None
changeZoom = None
fps = 0
FPS = None
#-----------------
#Funções----------
def criaBotoes():
    botoes = []
    botoes.append(Botao(codigo='btMaisZoom', lugar=[int(tamanhoTela[0]*0.9), int(tamanhoTela[1]*0.72)], cor=corUniverso, tamanho=[60, 35]))
    botoes.append(Botao(codigo='btMenosZoom', lugar=[int(tamanhoTela[0]*0.9), int(tamanhoTela[1]*0.823)], cor=corUniverso, tamanho=[60, 35]))
    botoes.append(Botao(lugar=[int(tamanhoTela[0]*0.925), int(tamanhoTela[1]*0.025)], texto='x',tamanho=[int(tamanhoTela[0]*0.05), int(tamanhoTela[0]*0.05)],cor=corSecundaria, corTexto=(255,0,0), tamanhoTexto=tamanhoTexto, codigo=0))
    botoes.append(Botao(codigo='btChangecenterCima', lugar=[int(tamanhoTela[0]*0.15), 0], cor=corUniverso, tamanho=[int(tamanhoTela[0]*0.7), int(tamanhoTela[1]*0.15)]))
    botoes.append(Botao(codigo='btChangecenterBaixo', lugar=[int(tamanhoTela[0]*0.15), tamanhoTela[1]*0.85], cor=corUniverso, tamanho=[int(tamanhoTela[0]*0.7), int(tamanhoTela[1]*0.15)]))
    botoes.append(Botao(codigo='btChangecenterLeft', lugar=[0, int(tamanhoTela[1]*0.15)], cor=corUniverso, tamanho=[int(tamanhoTela[0]*0.2), int(tamanhoTela[1]*0.7)]))
    botoes.append(Botao(codigo='btChangecenterRight', lugar=[int(tamanhoTela[0]*0.8), int(tamanhoTela[1]*0.15)], cor=corUniverso, tamanho=[int(tamanhoTela[0]*0.2), int(tamanhoTela[1]*0.7)]))
    
    return botoes

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

#-----------------
#Definições-------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption('Universe.Code')
mouse = Mouse()
botoes = criaBotoes()
universo = Universo(corpos=criaCorpos())
#-----------------
#Times------------
tempo_inicio = time()
timeContoufps = time()
#-----------------

seguir = universo.corpos[0]
seguir = None

running = True
while running:
    # Escreve fundo
    screen.fill(corUniverso)

    # Executa comandos do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            changeCenter = None
            changeZoom = None
        if event.type == pygame.MOUSEBUTTONDOWN:
            areaClique = pygame.mouse.get_pos()
            for botao in botoes:
                if hasColision(botao.getArea(), mouse.getArea(areaClique)):
                    codigo = botao.codigo
                    if codigo == None:
                        print('Botão sem comando definido.')
                    elif codigo == 0:
                        running = False
                    elif codigo == 'btChangecenterCima':
                        changeCenter = codigo
                    elif codigo == 'btChangecenterBaixo':
                        changeCenter = codigo
                    elif codigo == 'btChangecenterLeft':
                        changeCenter = codigo
                    elif codigo == 'btChangecenterRight':
                        changeCenter = codigo
                    elif codigo == 'btMaisZoom':
                        changeZoom = codigo
                    elif codigo == 'btMenosZoom':
                        changeZoom = codigo
                        
                    break

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
        centroTela = seguir.lugar

    if FPS:
        universo.update(1 / FPS)

    # Escreve botões
    for botao in botoes:
        pygame.draw.rect(screen, botao.cor, (botao.lugar[0],botao.lugar[1],botao.tamanho[0],botao.tamanho[1]))
        myfont = pygame.font.SysFont(font, int((tamanhoTela[0] / 2) * tamanhoTexto))
        textsurface = myfont.render(botao.texto, True, botao.corTexto)
        screen.blit(textsurface, (int((botao.lugar[0])+botao.tamanho[0]*0.3), int((botao.lugar[1])-botao.tamanho[1]*0.2)))

    btZoom = pygame.image.load("images/imgbtzoom.png")
    screen.blit(btZoom, (int(tamanhoTela[0] * 0.9), int(tamanhoTela[1] * 0.7)))
    
    # Escreve corpos
    for corpo in universo.corpos:
        tamanhoCorpoPixel = distanciaKmToPixel(corpo.getTamanho(), tamanhoTela[0], zoom)
        lugarCorpoPixel = getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], tamanhoTela, zoom)
        for rastro in corpo._lista_rastros:
            draw.line(screen, rastro[0], rastro[1], rastro[2], rastro[3])
            
        def draw_squad(screen, lugar, tamanho, cor=[0, 255, 0]):
            lado_tamanho = tamanho*1.25
            ponto1 = [int(lugar[0]-lado_tamanho), int(lugar[1]-lado_tamanho)] 
            ponto2 = [int(lugar[0]+lado_tamanho), int(lugar[1]-lado_tamanho)]
            ponto3 = [int(lugar[0]-lado_tamanho), int(lugar[1]+lado_tamanho)]
            ponto4 = [int(lugar[0]+lado_tamanho), int(lugar[1]+lado_tamanho)]

            pygame.draw.line(screen, cor, ponto1, ponto2) #Linha 1
            pygame.draw.line(screen, cor, ponto3, ponto4) #Linha 2
            pygame.draw.line(screen, cor, ponto1, ponto3) #Linha 3
            pygame.draw.line(screen, cor, ponto2, ponto4) #Linha 4

            myfont = pygame.font.SysFont(font, int(lado_tamanho*0.2))
            textsurface = myfont.render(corpo.nome, True, cor)
            screen.blit(textsurface, (ponto1[0], ponto1[1]))
            textsurface = myfont.render(str([int(corpo.lugar[0]),int(corpo.lugar[1])]), True, cor)
            screen.blit(textsurface, (ponto1[0], ponto1[1]-(lado_tamanho*0.25)))
        
        if show_squadinfors and (not tamanhoCorpoPixel<1):
            draw_squad(screen, lugarCorpoPixel, tamanhoCorpoPixel, (0,255,0))
        
        pygame.draw.circle(screen, corpo.getCor(), lugarCorpoPixel, tamanhoCorpoPixel)

    #Escreve informações na tela
    myfont = pygame.font.SysFont(font, int((tamanhoTela[0] * 0.25) * tamanhoTexto))
    textsurface = myfont.render(f"FPS: {str(FPS)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 5))
    textsurface = myfont.render("Local centro da tela: "+f"[x={getStringdist(centroTela[0])}, y={getStringdist(centroTela[1])}]", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 25))
    textsurface = myfont.render(f"Zoom: {getStringdist(zoom)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 45))
    
    

    if (time() - timeContoufps) > 1:
        FPS = fps
        timeContoufps = time()
        fps = 0
    fps += 1

    # Verefica se o tempo de simulação chegou ao fim
    if (time() - tempo_inicio) > segundos_de_simulacao:
        running = False

    # Atualiza janela Pygame e define FPS
    pygame.display.flip()
    clock.tick(FPS_rate)

pygame.quit()

import pygame
from classes.universo import Universo
from classes.corpo import Corpo
from classes.botao import Botao
from classes.mouse import Mouse
from time import time
from utils import *

#Configurações----
tamanhoTela = [600,600]
FPS_rate=10000
segundos_de_simulacao = 180

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
zoom = 1000000 #Zoom inicial
centroTela = [int(zoom/2), int(zoom/2)] #Local de início
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
    lua = Corpo((7.34 * (10**19)), raio=1737, lugar=[784400, 400000], cor=(255, 255, 150))
    lua.putForca([530**9,300**9], 1)
    terra = Corpo((5.972 * (10**24)), raio=6371, lugar=[zoom/2, zoom/2], cor=(0, 0, 255))
    terra._velocidade = [1000, 2000]

    corpos.append(lua)
    corpos.append(terra)
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

    if FPS:
        universo.update(1 / FPS)

    # Escreve botões
    for botao in botoes:
        pygame.draw.rect(screen, botao.cor, (botao.lugar[0],botao.lugar[1],botao.tamanho[0],botao.tamanho[1]))
        myfont = pygame.font.SysFont(font, int((tamanhoTela[0] / 2) * tamanhoTexto))
        textsurface = myfont.render(botao.texto, True, botao.corTexto)
        screen.blit(textsurface, (int((botao.lugar[0])+botao.tamanho[0]*0.3), int((botao.lugar[1])-botao.tamanho[1]*0.2)))

    # Escreve corpos
    for corpo in universo.corpos:
        tamanhoCorpoPixel = distanciaKmToPixel(corpo.getTamanho(), tamanhoTela[0], zoom)
        lugarCorpoPixel = getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], tamanhoTela, zoom)
        #if tamanhoCorpoPixel < 1: tamanhoCorpoPixel=1
        pygame.draw.circle(screen, corpo.getCor(), getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], tamanhoTela, zoom), tamanhoCorpoPixel)
    btZoom = pygame.image.load("images/imgbtzoom.png")
    screen.blit(btZoom, (int(tamanhoTela[0] * 0.9), int(tamanhoTela[1] * 0.7)))

    #Escreve informações na tela
    myfont = pygame.font.SysFont(font, int((tamanhoTela[0] * 0.25) * tamanhoTexto))
    textsurface = myfont.render(f"FPS: {str(FPS)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 5))
    textsurface = myfont.render("Local centro da tela: "+str([int(centroTela[0]), int(centroTela[1])]), True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 25))
    textsurface = myfont.render(f"Zoom: {int(zoom)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 50))

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

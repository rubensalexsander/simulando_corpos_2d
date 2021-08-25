import pygame
from classes.universo import Universo
from classes.corpo import Corpo
from classes.botao import Botao
from classes.mouse import Mouse
from time import time
from utils import *

#Configurações----
tamanhoTela = [600,600]
FPS=60
TD = 0.1
segundos_de_simulacao = 120
corFundo = (0, 0, 20)
corPrimaria = (13, 16, 23)
corSecundaria = (22, 27, 34)
corTextoPrimaria = (88, 166, 255)
corTextoSecundaria = (53, 114, 165)
corBranco = (255, 255, 255)
font = 'ARIAL'
tamanhoTexto = 0.1
#-----------------
#Variáveis--------
botoes = []
botaoSair = []
zoom = 600000
centroTela = [int(zoom/2), int(zoom/2)]
changeCenter = None
changeZoom = None
fpss = 0
fps_rate = 0
#-----------------
#Definições-------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption('Universe.Code')
lugarBotao = int(tamanhoTela[0]*0.925), int(tamanhoTela[1]*0.025)
tamanhoBotao = [int(tamanhoTela[0]*0.05), int(tamanhoTela[0]*0.05)]
mouse = Mouse()
botaoSair = Botao(lugar=lugarBotao, texto='x',tamanho=tamanhoBotao,cor=corSecundaria, corTexto=(255,0,0), tamanhoTexto=tamanhoTexto, codigo=0)
btChangecenterCima = Botao(codigo='btChangecenterCima', lugar=[int(tamanhoTela[0]*0.15), 0], cor=corFundo, tamanho=[int(tamanhoTela[0]*0.7), int(tamanhoTela[1]*0.15)])
btChangecenterBaixo = Botao(codigo='btChangecenterBaixo', lugar=[int(tamanhoTela[0]*0.15), tamanhoTela[1]*0.85], cor=corFundo, tamanho=[int(tamanhoTela[0]*0.7), int(tamanhoTela[1]*0.15)])
btChangecenterLeft = Botao(codigo='btChangecenterLeft', lugar=[0, int(tamanhoTela[1]*0.15)], cor=corFundo, tamanho=[int(tamanhoTela[0]*0.2), int(tamanhoTela[1]*0.7)])
btChangecenterRight = Botao(codigo='btChangecenterRight', lugar=[int(tamanhoTela[0]*0.8), int(tamanhoTela[1]*0.15)], cor=corFundo, tamanho=[int(tamanhoTela[0]*0.2), int(tamanhoTela[1]*0.7)])
btMaisZoom = Botao(codigo='btMaisZoom', lugar=[int(tamanhoTela[0]*0.9), int(tamanhoTela[1]*0.72)], cor=corFundo, tamanho=[60, 35])
btMenosZoom = Botao(codigo='btMenosZoom', lugar=[int(tamanhoTela[0]*0.9), int(tamanhoTela[1]*0.823)], cor=corFundo, tamanho=[60, 35])
botoes.append(botaoSair)
botoes.append(btMaisZoom)
botoes.append(btMenosZoom)
botoes.append(btChangecenterCima)
botoes.append(btChangecenterBaixo)
botoes.append(btChangecenterLeft)
botoes.append(btChangecenterRight)
universo1 = Universo(tamanhoTela, visualizar=zoom)
lua = Corpo((7.34 * (10**19)), raio=1737, mundo=universo1, lugar=[200000, 100000], cor=(255, 255, 150))
lua.putForca([490**9,300**9], 1)
terra = Corpo((5.972 * (10**24)), raio=6371, mundo=universo1, lugar=[300000, 300000], cor=(0, 0, 255))
terra._velocidade = [-0, 2000]
#-----------------
#Times------------
tempo_inicio = time()
timeContoufps = time()
#-----------------

running = True
while running:
    # Escreve fundo
    screen.fill(corFundo)

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
                    try:
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

                    except:
                        print('Erro ao executar comando do botão.')
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
        zoom -= zoom*0.05
    elif changeZoom == 'btMenosZoom':
        zoom += zoom*0.05

    universo1.update(1 / FPS)

    for botao in botoes:
        pygame.draw.rect(screen, botao.cor, (botao.lugar[0],botao.lugar[1],botao.tamanho[0],botao.tamanho[1]))
        myfont = pygame.font.SysFont(font, int((tamanhoTela[0] / 2) * tamanhoTexto))
        textsurface = myfont.render(botao.texto, True, botao.corTexto)
        screen.blit(textsurface, (int((botao.lugar[0])+botao.tamanho[0]*0.3), int((botao.lugar[1])-botao.tamanho[1]*0.2)))

    for corpo in universo1._lista_corpos:
        tamanhoCorpoPixel = distanciaKmToPixel(corpo.getTamanho(), tamanhoTela[0], zoom)
        lugarCorpoPixel = getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], tamanhoTela, zoom)
        #if tamanhoCorpoPixel < 1: tamanhoCorpoPixel=1
        pygame.draw.circle(screen, corpo.getCor(), getLugatPixel([corpo.getLugar()[0]-centroTela[0], corpo.getLugar()[1]-centroTela[1]], tamanhoTela, zoom), tamanhoCorpoPixel)

    btZoom = pygame.image.load("images/imgbtzoom.png")
    screen.blit(btZoom, (int(tamanhoTela[0] * 0.9), int(tamanhoTela[1] * 0.7)))

    myfont = pygame.font.SysFont(font, int((tamanhoTela[0] * 0.25) * tamanhoTexto))

    textsurface = myfont.render(f"FPS: {int(fps_rate)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 5))
    textsurface = myfont.render("Local centro da tela: "+str([int(centroTela[0]), int(centroTela[1])]), True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 25))
    textsurface = myfont.render(f"Zoom: {int(zoom)}", True, corTextoSecundaria)
    screen.blit(textsurface, (int(tamanhoTela[0] * 0.025), 50))

    if (time() - timeContoufps) > 1:
        fps_rate = fpss
        timeContoufps = time()
        fpss = 0
    fpss += 1

    # Verefica se o tempo de simulação chegou ao fim
    if (time() - tempo_inicio) > segundos_de_simulacao:
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

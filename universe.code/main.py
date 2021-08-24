import pygame
from classes.mundo import Mundo
from classes.corpo import Corpo
from time import time

#Configurações----
tamanhoTela = [600,600]
zoom = 1
visualizar = 1000000
FPS=120
corFundo = (0, 0, 20)
TD = 0.1
segundos_de_simulacao = 60
#-----------------
#Definições-------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption('Universe.Code')
#-----------------

mundo1 = Mundo(tamanhoTela, zoom, visualizar=visualizar)

lua = Corpo((7.34 * (10**19)), 1737, mundo1, lugar=[100000,  300000], cor=(255,255,150))
terra = Corpo((5.972 * (10**24)), 6371, mundo1, lugar=[300000,300000], cor=(255,255,0))
terra2 = Corpo((5.972 * (10**24)), 6371, mundo1, lugar=[700000,700000], cor=(0,0,255))

lua.putForca([520**9,300**9], 1)
terra._velocidade = [-0, 15000]
terra2._velocidade = [0, -15000]

mundo1.showRastro = False
mundo1.showGravity = False

tempo_inicio = time()

running = True
while running:
    # Escreve fundo
    screen.fill(corFundo)

    # Executa comandos do usuário
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mundo1.update(TD)

    for corpo in mundo1._lista_corpos:
        pygame.draw.circle(screen, corpo.getCor(), corpo.getLugar('pixel'), corpo.getTamanho())

    # Verefica se o tempo de simulação chegou ao fim
    if (time() - tempo_inicio) > segundos_de_simulacao:
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

from libs.arFront import *

app = App(nomeJanela='Simulando corpos em Python :P', tema=universeCodeTheme, resolucao=[800,600])
app.txARTI.active = False
app.FPS_rate = 120
app.txFps.active = True

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

btPause = app.novoBotao(
    string='| |',
    cor=app.cor_back,
    tamanhoTexto=20,
    lugar=[0.94, 0.01],
    tamanho = [40, 40],
    corTexto=app.cor_bordas_bt,
    refer='nr',
    bordas=1,
    corBordas=app.cor_bordas_bt
)

btCenterUP = app.novoBotao(
    lugar=[0.35, -0.005],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.3, 50],
    string='UP',
    tamanhoTexto=12,
    end_draw=True)

btCenterDOWN = app.novoBotao(
    lugar=[0.35, 1.005],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[0.3, 50],
    string='DOWN',
    tamanhoTexto=12,
    end_draw=True,
    refer='sl')

btCenterLEFT = app.novoBotao(
    lugar=[-0.005, 0.35],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[50, 0.3],
    string='LEFT',
    tamanhoTexto=12,
    end_draw=True)

btCenterRIGHT = app.novoBotao(
    lugar=[1.005, 0.35],
    cor=app.cor_back,
    bordas=1,
    radius=10,
    tamanho=[50, 0.3],
    string='RIGHT',
    tamanhoTexto=12,
    end_draw=True,
    refer='nr')



sqZoom = app.novoSquare(
    lugar=[0.99, 0.99],
    refer='sr',
    tamanho=[0.12,50],
    cor=(-1,-1,-1),
    bordas=1,
    corBordas=app.cor_back_secundaria,
    active=False
)

btMenosZoom = app.novoBotao(
    string='-',
    lugar=[0.91, 0.99],
    tamanho=[30,50],
    tamanhoTexto=25,
    refer='sr',
    cor=(-1,-1,-1),
    bordas=1
)

btMaisZoom = app.novoBotao(
    string='+',
    lugar=[0.98, 0.99],
    tamanho=[30,50],
    tamanhoTexto=25,
    refer='sr',
    cor=(-1,-1,-1),
    bordas=1
)

txBtZoom = app.novoTexto(
    lugar=[0.975, 0.9],
    refer='sr',
    string='ZOOM',
    cor=app.cor_back_secundaria
)

bt_rastro = app.novoBotao(
    lugar=[0.01, 0.86],
    cor=app.cor_back,
    tamanho=[85,30],
    string='Rastro',
    bordas=1
)

bt_infors = app.novoBotao(
    lugar=[0.01, 0.925],
    cor=app.cor_back,
    tamanho=[85,30],
    string='Informações',
    bordas=1
)

bt_orientation = app.novoBotao(
    lugar=[0.01, 0.8],
    cor=app.cor_back,
    tamanho=[85,30],
    string='Setas',
    bordas=1
)

ltInfors = app.novoList(
    lugar=[5, 30],
    cor=(-1,-1,-1),
    corTexto=app.cor_texto_bt,
    draw_coluns=0,
    tamanho=[200, 120],
    tamanhoTexto=12,
    tamanhoDistancias=[80,20],
    padding=[5,5],
    content={},
    bordas=1
)
'''
txZoom = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 30]
)

tx_time = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 50]
)

tx_corpos = app.novoTexto(
    tamanho=11,
    lugar=[0.01, 70]
)'''
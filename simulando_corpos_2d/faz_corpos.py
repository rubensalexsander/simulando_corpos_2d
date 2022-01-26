from random import randint

def aleatorios(universo, quant, area, velocidade_min, velocidade_max, raio_min, raio_max, massa_min, massa_max):
    corpos = []

    for i in range(quant):
        massa = randint(massa_min, massa_max)
        raio = randint(raio_min, raio_max)
        lugar = [randint(area[0][0], area[1][0]), randint(area[0][1], area[1][1])]
        cor = (randint(50,255), randint(50,255), randint(50,255))
        velocidade = [randint(velocidade_min[0], velocidade_max[0]), randint(velocidade_min[1], velocidade_max[1])]

        corpo = universo.new_corpo(
        massa=massa, 
        raio=raio, 
        lugar=lugar, 
        cor=cor,
        velocidade=velocidade, 
        nome=f'corpo{i}')

        corpos.append(corpo)
    
    return corpos

def manual(universo):
    corpo1 = universo.new_corpo(
        massa=(6972 * (8**24)), 
        raio=12000, 
        lugar=[-250000, 0], 
        cor=(100, 150, 255),
        velocidade=[10000, 0], 
        nome='corpo1')
    
    corpo2 = universo.new_corpo(
        massa=(555.972 * (7**24)), 
        raio=4000, 
        lugar=[300000, 300000],
        velocidade=[-45000, 12000],
        cor=(150, 100, 255), 
        nome='corpo2')
    
    corpo3 = universo.new_corpo(
        massa=(455.972 * (7**24)), 
        raio=5000, 
        lugar=[150000, 550000],
        velocidade=[40000, -2000],
        cor=(250, 255, 255), 
        nome='corpo3')
    
    corpo4 = universo.new_corpo(
        massa=(355.972 * (7**24)), 
        raio=5000, 
        lugar=[200000, 500000],
        velocidade=[25000, 0],
        cor=(150, 155, 255), 
        nome='corpo4')

    corpo7 = universo.new_corpo(
        massa=(255.972 * (7**24)), 
        raio=7000, 
        lugar=[-100000, 200000],
        velocidade=[-85000, 40000],
        cor=(255, 190, 155), 
        nome='corpo7')
    
    terra = universo.new_corpo(
        massa=(2349 * (9**23)), 
        raio=7000, 
        lugar=[-300000, -600000],
        velocidade=[-35000, 40000],
        cor=(0, 0, 155), 
        nome='Terra')

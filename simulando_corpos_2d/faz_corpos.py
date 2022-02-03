from random import randint

def getD(ponto1, ponto2):
    lugar1, lugar2 = ponto1, ponto2
    d = ((lugar1[0]-lugar2[0])**2+(lugar1[1]-lugar2[1])**2)**(1/2)
    return d

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

def em_massa(universo, massas, raios, lugares, cores, velocidades):
    for i in range(len(massas)):
        universo.new_corpo(
            massa=massas[i], 
            raio=raios[i], 
            lugar=lugares[i], 
            cor=cores[i],
            velocidade=velocidades[i], 
            nome=f'corpo{i}'
            )

def em_circulo(universo, ponto, quant, distancia_min, distancia_max, massa):
    for i in range(quant):
        x_possivel = [ponto[0] - distancia_max, ponto[0] + distancia_max]
        y_possivel = [ponto[1] - distancia_max, ponto[1] + distancia_max]

        local_x = randint(x_possivel[0], x_possivel[1])
        local_y = randint(y_possivel[0], y_possivel[1])
        lugar = [local_x, local_y]

        dist = getD(ponto, lugar)

        while dist < distancia_min:
            local_x = randint(x_possivel[0], x_possivel[1])
            local_y = randint(y_possivel[0], y_possivel[1])
            lugar = [local_x, local_y]

            dist = getD(ponto, lugar)
        
        v_x = 50000
        v_y = 60000

        dist_x = local_x - ponto[0]
        dist_y = local_y - ponto[1]

        velocidade = [
            v_x*((distancia_max-dist_x)/distancia_max),
            v_y*((distancia_max-dist_y)/distancia_max)
            ]

        corpo = universo.new_corpo(
            massa=massa, 
            raio=500, 
            lugar=lugar, 
            cor=(200, 200, 255),
            velocidade=velocidade, 
            nome='corpo'
            )


def manual(universo):
    corpo1 = universo.new_corpo(
        massa=(6972 * (8**23)), 
        raio=5000, 
        lugar=[-450000, -150000], 
        cor=(100, 150, 255),
        velocidade=[10000, 60000], 
        nome='corpo1')
    
    corpo2 = universo.new_corpo(
        massa=(555.972 * (7**23)), 
        raio=4000, 
        lugar=[300000, 300000],
        velocidade=[-45000, 12000],
        cor=(150, 100, 255), 
        nome='corpo2')
    
    corpo3 = universo.new_corpo(
        massa=(455.972 * (7**23)), 
        raio=5000, 
        lugar=[150000, 550000],
        velocidade=[40000, -2000],
        cor=(250, 255, 255), 
        nome='corpo3')

    terra = universo.new_corpo(
        massa=(2349 * (9**23)), 
        raio=10000, 
        lugar=[0, 0],
        velocidade=[0, 0],
        cor=(50, 50, 255), 
        nome='Terra'
        )

    #em_circulo(universo, terra.lugar, 100, 400000, 500000, (455.972 * (7**24)))

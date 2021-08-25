def hasColision(area1, area2):
    area1ponto1 = area1[0]
    area1ponto2 = [area1[1][0], area1[0][1]]
    area1ponto3 = [area1[0][0], area1[1][1]]
    area1ponto4 = area1[1]
    area2ponto1 = area2[0]
    area2ponto2 = [area2[1][0], area2[0][1]]
    area2ponto3 = [area2[0][0], area2[1][1]]
    area2ponto4 = area2[1]
    if (area2ponto1[0]>=area1ponto1[0]) and (area2ponto1[1]>=area1ponto1[1]) and (area2ponto1[0]<=area1ponto4[0]) and (area2ponto1[1]<=area1ponto4[1]):
        return True
    elif (area1ponto2[0]>=area2ponto1[0]) and (area1ponto2[1]>=area2ponto1[1]) and (area1ponto2[0]<=area2ponto4[0]) and (area1ponto2[1]<=area2ponto4[1]):
        return True
    elif (area1ponto1[0]>=area2ponto1[0]) and (area1ponto1[1]>=area2ponto1[1]) and (area1ponto1[0]<=area2ponto4[0]) and (area1ponto1[1]<=area2ponto4[1]):
        return True
    elif (area2ponto2[0]>=area1ponto1[0]) and (area2ponto2[1]>=area1ponto1[1]) and (area2ponto2[0]<=area1ponto4[0]) and (area2ponto2[1]<=area1ponto4[1]):
        return True

    return False

def getLugatPixel(distanciaKm, tamanhoTela, zoom):
    #centroTela = [zoom/2, zoom/2]
    return [int(((tamanhoTela[0]/zoom)*(distanciaKm[0]))+(tamanhoTela[0]*0.5)),
            int(((tamanhoTela[1]/zoom)*(distanciaKm[1]))+(tamanhoTela[0]*0.5))]

def distanciaKmToPixel(distanciaKm, tamanhoTela, zoom):
    return int((tamanhoTela/zoom)*distanciaKm)
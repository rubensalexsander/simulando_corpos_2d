
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
    return [int(distanciaKmToPixel(distanciaKm[0], tamanhoTela[0], zoom)+(tamanhoTela[0]*0.5)),
            int(distanciaKmToPixel(distanciaKm[1], tamanhoTela[1], zoom)+(tamanhoTela[1]*0.5))]

def distanciaKmToPixel(distanciaKm, tamanhoTela, zoom):
    return int((tamanhoTela/zoom)*distanciaKm)

def getStringdist(distancia):
    flt = str(float(round(distancia, 1)))
    string = str(flt.replace(".", ",")) + " km"
    if len(string) == 9:
        string = string[:1] + "." + string[1:]
    elif len(string) == 10:
        string = string[:2] + "." + string[2:]
    elif len(string) == 11:
        string = string[:3] + "." + string[3:]
    elif len(string) == 12:
        string = string[:4] + "." + string[4:]
        string = string[:1] + "." + string[1:]
    elif len(string) == 13:
        string = string[:5] + "." + string[5:]
        string = string[:2] + "." + string[2:]
    elif len(string) == 14:
        string = string[:6] + "." + string[6:]
        string = string[:3] + "." + string[3:]
    elif len(string) == 15:
        string = string[:7] + "." + string[7:]
        string = string[:4] + "." + string[4:]
        string = string[:1] + "." + string[1:]
        
    return string

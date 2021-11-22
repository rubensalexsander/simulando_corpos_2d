def getLugarPixel(distanciaKm, tamanhoTela, zoom):
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

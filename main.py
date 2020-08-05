n = int(input())
p = int(input())
char_preto = input()
altura = pow(2,n)
totalCoordenadas = 0
index = 0

if p >= n: p = (n - 1)

for passos in range(p+1): totalCoordenadas += int(pow(3,passos))
tela = [[" " for i in range(altura)] for j in range(altura)]
coordenadas = [[0,0,altura]]


""" Método que utiliza recursão para obter as coordenadas dos novos quadrados após a subdivisão"""
def triplicar_quadrado(x, y, h):
    global index
    index += 1
    if len(coordenadas) == totalCoordenadas: return
    coordenadas.append([int(x), int(y+(h/4)), int(h/2)])
    coordenadas.append([(int(x) + int(h/2)), int(y), int(h/2)])
    coordenadas.append([(int(x) + int(h/2)), int(y + (h/2)), int(h/2)])
    triplicar_quadrado(coordenadas[index][0], coordenadas[index][1], coordenadas[index][2])
    triplicar_quadrado(coordenadas[index][0], coordenadas[index][1], coordenadas[index][2])
    triplicar_quadrado(coordenadas[index][0], coordenadas[index][1], coordenadas[index][2])


""" Método que desenha um quadrado de altura h nas coordenadas (x, y) """
def preencher_quadrado(x, y, h):
    for i in range(h):
        for j in range(h):
            tela[int(x+i)][int(y+j)] = char_preto


""" Método que desenha todos os quadrados após p passos """
def criar_tela():
    x = coordenadas[0][0]
    y = coordenadas[0][1]
    triplicar_quadrado(x, y, altura)
    for c in range((totalCoordenadas - int(pow(3, p))), totalCoordenadas):
        preencher_quadrado(coordenadas[c][0], coordenadas[c][1], coordenadas[c][2])

""" Método para desenhar a tela com moldura """
def print_tela_com_moldura():
    criar_tela()
    tela_com_moldura = tela

    for item in range(altura):
        tela_com_moldura[item].insert(0, "| ")
        tela_com_moldura[item].insert((altura + 1), " |")

    tela_com_moldura.insert(0, ["+", "+"])
    tela_com_moldura.insert(1, ["|", "|"])
    tela_com_moldura.append(["|", "|"])
    tela_com_moldura.append(["+", "+"])

    for item in range(altura+2):
        tela_com_moldura[0].insert(1, "-")
        tela_com_moldura[1].insert(1, " ")
        tela_com_moldura[len(tela_com_moldura) - 1].insert(1, "-")
        tela_com_moldura[len(tela_com_moldura) - 2].insert(1, " ")

    for item in range(altura+4):
        linha = "".join(tela_com_moldura[item])
        print(linha)

print_tela_com_moldura()

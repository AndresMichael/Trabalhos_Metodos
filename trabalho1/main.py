from trabalho1.contas import Diferencas, Integrais

c1 = Diferencas()

lista2 = []
lista_x = []
lista_y = []

# tratamento dos dados para realizar as contas de forma segura
with open('dados.txt', 'r') as arq:
    lista = arq.readlines()
    for linha in lista:
        for w in linha:
            if not w.count(' ') == 0:
                linha = linha[1:]
                continue
            break

        if 'x' in linha.lower():
            continue
        if '\t' in linha:
            linha = linha.replace('\t', ' ')
        if ',' in linha:
            linha = linha.replace(',', '.')
        lista2.append(linha.replace('\n', ''))

    for linha in lista2:
        cont = linha.count(' ')
        x, y = linha.split(cont * ' ')
        lista_x.append(float(x))
        lista_y.append(float(y))

print('============================================')

lista_final = []
# contas das derivadas finitas
for k in range(len(lista_x)):
    if k == 0:
        d = c1.diferenca_avancada(lista_x[0], lista_y[0], lista_x[1], lista_y[1])
        lista_final.append(d)
        continue
    if k == len(lista_x) - 1:
        d = c1.diferenca_regressiva(lista_x[k], lista_y[k], lista_x[k - 1], lista_y[k - 1])
        lista_final.append(d)
        continue
    d = c1.diferenca_centrada(lista_x[k], lista_y[k + 1], lista_x[k - 1], lista_y[k - 1])
    lista_final.append(d)

# Criando arquivo python para derivadas finitas
with open('derivadas.txt', 'w') as saida:
    saida.write('valor:x       valor: derivada \n')
    for i in range(len(lista_final)):
        saida.write(f'  {lista_x[i]}   ')
        saida.write(f'      {lista_final[i]}\n')

# para a integral :

# definindo o intervalo
integral = Integrais()
lista_integrais = integral.metodo_retangulo(lista_x=lista_x, lista_y=lista_y)
print(lista_integrais)

with open('integral.txt', 'w') as arquivo:
    arquivo.write('\tX\t\tIntegral \n')
    for i in range(len(lista_integrais)):
        arquivo.write(f'\t{lista_x[i]}\t')
        arquivo.write(f'\t{lista_integrais[i]}\n')

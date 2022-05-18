class Diferencas:

    def diferenca_avancada(self, x, y, x1, y1):
        return (y1 - y) / (x1 - x)

    def diferenca_regressiva(self, x, y, x1, y1):
        return (y - y1) / (x - x1)

    def diferenca_centrada(self, x, y, x1, y1):
        return (y - y1) / ((x - x1) * 2)


class Integrais:

    def metodo_retangulo(self, lista_x: list, lista_y: list) -> list:
        resultado = 0
        lista_integrais = []
        a = lista_x[0]
        b = lista_x[-1]
        delta_x = (b - a) / (len(lista_x)-1)
        print(delta_x)
        for n in range(len(lista_x)):
            resultado += delta_x * lista_y[n]
            print(f'n = {n}  {resultado}')
            lista_integrais.append(resultado)

        return lista_integrais

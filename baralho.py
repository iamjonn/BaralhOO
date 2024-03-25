import random

from carta import Carta
class Baralho:
    def __init__(self):
        self.cartas = {}
        naipes = ["Copas", "Ouros", "Paus", "Espadas"]
        for naipe in naipes:
            for valor in range(1, 14):
                nome_carta = f"{valor} de {naipe}"
                if valor == 1:
                    nome_carta = f"A de {naipe}"
                elif valor == 11:
                    nome_carta = f"J de {naipe}"
                elif valor == 12:
                    nome_carta = f"Q de {naipe}"
                elif valor == 13:
                    nome_carta = f"K de {naipe}"
                self.cartas[nome_carta] = Carta(naipe, valor)

    def embaralhar(self):
        chaves_embaralhadas = list(self.cartas.keys())
        random.shuffle(chaves_embaralhadas)
        cartas_embaralhadas = {}
        for chave in chaves_embaralhadas:
            cartas_embaralhadas[chave] = self.cartas[chave]
        self.cartas = cartas_embaralhadas

    def distribuir(self, num_jogadores):
        maos = [[] for _ in range(num_jogadores)]
        chaves = list(self.cartas.keys())
        random.shuffle(chaves)
        for i, chave in enumerate(chaves):
            maos[i % num_jogadores].append(self.cartas[chave])
        return maos
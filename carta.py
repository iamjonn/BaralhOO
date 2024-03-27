class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        if self.valor == 1:
            return f"A de {self.naipe}"
        elif self.valor == 11:
            return f"J de {self.naipe}"
        elif self.valor == 12:
            return f"Q de {self.naipe}"
        elif self.valor == 13:
            return f"K de {self.naipe}"
        else:
            return f"{self.valor} de {self.naipe}"
from baralho import Baralho


# Testando o baralho
baralho = Baralho()
baralho.embaralhar()
num_jogadores = 3  # Defina o número de jogadores aqui
maos_jogadores = baralho.distribuir(num_jogadores)
for i, mao in enumerate(maos_jogadores):
    print(f"Cartas do jogador {i+1}:")
    for carta in mao:
        print(carta)
    print()

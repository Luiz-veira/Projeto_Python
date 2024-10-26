import random


def gerar_introducao():
    introducoes = ["Na segunda, eu", "Na terça, eu", "Na quarta, eu", "Na quinta, eu", "Na sexta, eu"]
    return random.choice(introducoes)


def gerar_desenvolvimento():
    desenvolvimentos = ["fui para a escola.", "fui em uma reunião de trabalho.", "aprendi programação no curso.",
                         "sai com os meus parentes.", "fiquei quieto em casa."]
    return random.choice(desenvolvimentos)


def gerar_final():
    finais = ["E no final do dia deitei na cama exausto.", "E no final do dia sai em um rolê com os amigos.",
               "E no final do dia fui ver um filme na netflix.", "E no final do dia fiz o jantar.",
                 "E no final do dia eu estudei inglês."]
    return random.choice(finais)


def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia


if __name__ == "__main__":
    print(gerar_historia())
with open("Notas.txt", "r") as Notas:
    x = Notas.readlines()

for linha in x:
    nome, notas_str = linha.split(":")
    notas = [float(nota) for nota in notas_str.strip()[1:-1].split()]
    media = sum(notas) / len(notas)

    if media >= 7:
        with open("Aprovado.txt", "a") as Aprovado:
            Aprovado.write(nome.strip() + " " + str(media))
    elif media < 7 and media >= 5:
        with open("Exame.txt", "a") as Exame:
            Exame.write(nome.strip()+":" + str(f'[{media}]'))
    else:
        with open("Reprovado.txt", "a") as Reprovado:
            Reprovado.write(nome.strip()+":" + str(f'[{media}]'))

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip().split(":") for linha in linhas]

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_resultado(nome, media):
    if media >= 5:
        return "Aprovado após exame: " + nome
    else:
        return "Reprovado após exame: " + nome

def main():
    alunos = ler_arquivo("exame.txt")
    aprovados = []
    reprovados = []

    for aluno in alunos:
        nome, notas_str = aluno
        notas = [float(nota) for nota in notas_str.strip()[1:-1].split()]
        nota_exame = float(input('Digite a sua nota do exame: '))
        notas.append(nota_exame)
        media = calcular_media(notas)
        resultado = verificar_resultado(nome, media)

        if media >= 5:
            aprovados.append(resultado)
        else:
            reprovados.append(resultado)

    with open("aprovados.txt", "a") as arquivo_aprovados:
        for aprovado in aprovados:
            arquivo_aprovados.write(aprovado + '\n')

    with open("reprovados.txt", "a") as arquivo_reprovados:
        for reprovado in reprovados:
            arquivo_reprovados.write(reprovado + '\n')

if __name__ == "__main__":
    main()
while (True):
    nome = input("Digite seu nome:\n")
    try:
        nota1 = float(input("Digite sua primeira nota:\n"))
        nota2 = float(input("Digite sua segunda nota:\n"))
        nota3 = float(input("Digite sua terceira nota:\n"))
    except ValueError:
        print("Digite valores numericos para as notas.")
    
    print("Deseja continuar? 1-Sim e 2-Não")
    continuar = int(input())

    with open("Notas.txt" ,"a") as Notas:
        Notas.write(f"{nome}:[{nota1} {nota2} {nota3}]\n")
    
    if continuar == 2:
        break


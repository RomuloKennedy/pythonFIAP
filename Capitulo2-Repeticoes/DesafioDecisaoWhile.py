resposta = "SIM"

while resposta == "SIM":

    genero = input("Digite seu Genêro: ").upper()
    acesso = input("Digite seu Nivel de Acesso: ").upper()

    if acesso == "ADM":
        if genero == "MASCULINO":
            print("Olá Administrador!")
        else:
            print("Olá Administradora!")
    elif acesso == "USR":
        if genero == "MASCULINO":
            print("Olá usuário")
        else:
            print("Olá Usuária")
    elif acesso == "GUEST":
        print("Olá visitante")
    else:
        print("Olá Desconhecido(a)")

    resposta =input("Digite SIM para continuar: ").upper()
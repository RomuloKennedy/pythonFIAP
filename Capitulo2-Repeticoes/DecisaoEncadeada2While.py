adicionarpaciente = "SIM"
while(adicionarpaciente == "SIM"):

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

    while doenca_infectocontagiosa != "NÃO" and doenca_infectocontagiosa != "SIM":
         print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
         doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()
# PRIMEIRO PROBLEMA A SER RESOLVIDO

    if doenca_infectocontagiosa == "SIM":
     print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
     print("Encaminhe o paciente para sala BRANCA")

    # SEGUNDO PROBLEMA A SER RESOLVIDO
    if idade >= 65:
        print("Paciente COM prioridade")
    else:
        genero=input("Digite o gênero do paciente: ").upper()
        if genero =="FEMININO" and idade >10:
         gravidez=input("A Paciente está grávida ?").upper()
         if gravidez == "SIM":
            print("Paciente COM prioridade")
         else:
              print("Paciente SEM prioridade")
        else:
         print("Paciente SEM prioridade")

    adicionarpaciente =input("Deseja continuar adicionando pacientes ? Digite SIM para CONTINUAR: ").upper()
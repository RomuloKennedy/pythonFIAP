equipamento =[]
valor = []
numeroSerial = []
departamento = []

resposta = "S"

while(resposta == "S"):
    equipamento.append(input("Digite o Nome do Equipamento: "))
    valor.append(float(input("Digite o Valor: ")))
    numeroSerial.append(int(input("Digite o numeroSerial: ")))
    departamento.append(input("Digite o Departamento: "))

    resposta=input("Digite 'S' para continuar: ").upper()
print("--------------------------")
for indice in range(0,len(equipamento)):

    print("\tEquipamento = ",(indice+1))
    print("\tNome = ",equipamento[indice])
    print("\tValor = ",valor[indice])
    print("\tNumero Serial = ",numeroSerial[indice])
    print("\tDepartamento = ",departamento[indice])
    print("--------------------------")

busca=input("Digite o Nome do equipamento que deseja buscar: ")

for indice in range(0,len(equipamento)):
    if busca==equipamento[indice]:
        print("Valor: ",valor[indice])
        print("Serial: ",numeroSerial[indice])
        valor[indice] = float(input("Digite o Novo Valor"))
        print("Valor Novo = ",valor[indice])

busca=int(input("Digite o Número do Serial: "))
for indice in range(0,len(equipamento)):
    if busca == numeroSerial[indice]:
        del equipamento[indice]
        del numeroSerial[indice]
        del valor[indice]
        del departamento[indice]
        print("DELETADO")
        break;





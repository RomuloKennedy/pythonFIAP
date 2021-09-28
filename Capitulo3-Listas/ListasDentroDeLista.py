inventario=[]
resposta = "S"
while resposta == "S":
   #Adicionando um equipamento no inventário
   equipamento=[input("Dite o nome do equipamento"),
          float(input("Digite o Valor")),
          int(input("Digite o Numero Serial")),
          input("Departamento")]
   inventario.append(equipamento)
   resposta =input("Digite 'S' para continuar: ").upper()
    #Lista de equipamentos no inventario
for elemento in inventario:
    print("Nome........ = ", elemento[0])
    print("Valor....... = ", elemento[1])
    print("Serial...... = ", elemento[2])
    print("Departamento = ", elemento[3])

busca = input("Digite o nome do equipamento que deseja Buscar: ")
    #Busca de um equipamento no inventario
for elemento in inventario:

    if busca == elemento[0]:
        print("Valor = ", elemento[1])
        print("Serial = ", elemento[2])

depreciacao = input("Digite o nome do equipamento que será depreciado")
    #Depreciacao do item no inventário
for elemento in inventario:

    if depreciacao == elemento[0]:
        print("Valor Antigo = ", elemento[1])
        elemento[1] = elemento[1] * 0.9
        print("Novo Valor = ", elemento[1])
serial = int(input("Digite o serial do equipamento que será excluido: "))
     #Exclusao por meio da Serial
for elemento in inventario:
    if serial == elemento[2]:
        inventario.remove(elemento)
    #exibir itens do inventário
for elemento in inventario:
    print("Nome........ = " ,elemento[0])
    print("Valor....... = " ,elemento[1])
    print("Serial...... = " ,elemento[2])
    print("Departamento = " ,elemento[3])

valores = []
    #Informação de preço do inventário
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa: ",max(valores))
    print("O equipamento mais barato custa: ",min(valores))
    print("O total de equipamentos é de: ",sum(valores))
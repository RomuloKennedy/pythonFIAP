
def preencherInventario (lista):
    resp="S"
    while(resp=="S"):
        equipamento=[input("Nome do Equiapmento: "),
                     float(input("Valor: ")),
                     int(input("Numero Serial: ")),
                     input("Departamento: ")]
        lista.append(equipamento)
        resp=input("Digite 'S' para continuar adicionando: ").upper()

def exibirInventario(lista):

    for elemento in lista:
        print("Nome........: ",elemento[0])
        print("Valor.......: ",elemento[1])
        print("Serial......: ",elemento[2])
        print("Departamento: ",elemento[3])

def localizarPorNome(lista):
    busca=input("Digite o nome que você quer buscar: ")
    for elemento in lista:
        if elemento[0] == busca:
            print("Valor: ",elemento[1])
            print("Serial",elemento[2])

def depreciarPorNome(lista):
    produto=(input("Digite o Nome do Produto que vai ser depreciado: "))
    for elemento in lista:
        if produto == elemento[0]:
            print("Valor Antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-10/100)
            print("Valor Novo: ", elemento[1])

def excluirPorSerial(lista):
    serial=(input("Digite a Serial para excluir: "))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
        return "Itens Excluidos."

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("O Valor mais Alto é: ",max(valores))
        print("O Valor mais baixo é: ",min(valores))
        print("O Total de equipamento é de: ",sum(valores))


lista = []
preencherInventario(lista)
exibirInventario(lista)
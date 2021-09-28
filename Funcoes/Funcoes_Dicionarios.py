def perguntar():
    resposta=input("O que Deseja Realizar?"+
                   "\n<I> - Para Inserir um Usuário"+
                   "\n<P> - Para Pesquisar um Usuário"+
                   "\n<E> - Para Excluir um Usuário"+
                   "\n<L> - Para Listar um Usuário: ").upper()
    return resposta
def inserir(dicionario):
    dicionario[input("Digite o código de lançamento: ").upper()]=[input("Digite o Login: ").upper(),
                                                   input("Digite o Nome: ").upper(),
                                                   input("Digite a última data de acesso: "),
                                                   input("Qual a última estação de acesso? ").upper()]

def pesquisar(dicionario,chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Login: ",lista[0])
        print("Nome: ",lista[1])
        print("Ultima data de Acesso: ",lista[2])
        print("última estação de acesso: ",lista[3])

def excluir(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Usúario Deletado!")

def listar(dicionario):
    for chave,valor in dicionario.items():
        print("Objeto......")
        print("Código de Lançamento: ",chave)
        print("Valor: ",valor)


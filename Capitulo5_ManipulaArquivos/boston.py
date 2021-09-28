# with open("economic-indicators.csv","r") as economia:
#     resultado=0
#     for linha in economia.readlines():
#         variavel = linha.split(",")
#         if variavel[0] == "2014":
#             resultado = resultado + int(variavel[3])
#
#     print(resultado)
#
# with open("economic-indicators.csv","r") as economia2:
#     resultado2 = "0"
#     for linha2 in economia2.readlines()[1:]:
#         variavel = linha2.split(",")
#         if float(variavel[2]) > float(resultado2):
#             resultado2 = variavel[2]
#             mes = variavel[1]
#             ano = variavel[0]
# print("O Mês/Ano de maior movimento no aeroporto foi: ", str(mes),"/",str(ano))
#
# with open("economic-indicators.csv","r") as economia3:
#     passageiros = input("Qual o Ano você quer saber? ")
#     resultado3=0
#     for linha3 in economia3.readlines()[1:]:
#         variavel3=linha3.split(",")
#         if variavel3[0] == passageiros:
#             resultado3= resultado3+int(variavel3[3])
#     print("O Total de Passageiros foi: ", resultado3)
#
# with open("economic-indicators.csv","r") as economia4:
#     interacao=input("Qual Ano Você quer especificar?")
#     resultado4 = 0.0
#     for linha4 in economia4.readlines()[1:]:
#         variavel4=linha4.split(",")
#         if variavel4[0] == interacao:
#             if float(variavel4[5]) > resultado4:
#                 resultado4 = float(variavel4[5])
#                 resultadoF =variavel4[1]
#     print("O Mês com maior diária de hotel é: ",resultadoF)
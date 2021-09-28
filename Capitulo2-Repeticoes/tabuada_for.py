numero=int(input("Digite de qual número você quer conhecer a tabuada: "))
for numero2 in range(0,11,1):
    print("\t"+ str(numero)+"x"+str(numero2)+"= "+str(numero * numero2))
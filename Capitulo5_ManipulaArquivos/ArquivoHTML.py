with open("pagina.html","w") as pagina:
    pagina.write("<body><center><h1> Está é um teste para página WEB </h1></center>")
    pagina.write("<center><h2> Abaixo seguem alguns nomes importantes para o projeto: </h2></center>")
    pagina.write("<h3>")
    nome=""
    while nome != "SAIR":
        nome = input("Digute um nome ou SAIR: ").upper()
        if nome != "SAIR":
            pagina.write("<center>"+nome+"</center>")
    pagina.write("</h3></body>")
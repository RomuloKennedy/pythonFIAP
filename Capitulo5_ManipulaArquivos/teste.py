import json

with open("inventario_json.json","r") as arquivo_json:
    resultado = json.load(arquivo_json)
    for chave,dado in resultado.items():
        print(dado)

import json

if __name__ == "__main__":
    cityObject = json.load(open("./files/cidades_sc_distancias.json", encoding="utf-8"))

    for city in list(cityObject.keys()):
        print(f'Cidade {city}')

    cidadeOrigem = input("Insira a Cidade Inicial\n");
    cidadeDestino = input("Insira a Cidade Desejada\n")
    print(f'Origem: {cidadeOrigem}\n Destino: {cidadeDestino} ')

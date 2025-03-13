import json

if __name__ == "__main__":
    cityObject = json.load(open("./files/cidades_sc_distancias.json", encoding="utf-8"))

    for city in list(cityObject.keys()):
        print(f'Cidade {city}')
    
    while True:
        cidadeOrigem = input("Insira a Cidade Inicial\n");

        if cidadeOrigem in cityObject:
            break
        else:
            print(f"Erro: A cidade '{cidadeOrigem}' não foi encontrada! Tente novamente.")

    while True:
        cidadeDestino = input("Insira a Cidade Desejada\n")

        if cidadeDestino in cityObject:
            break
        else:
            print(f"Erro: A cidade '{cidadeDestino}' não foi encontrada! Tente novamente.")

    print(f'Origem: {cidadeOrigem}\nDestino: {cidadeDestino} ')

    print(f'Lista de cidades próximas: {", ".join(list(cityObject[cidadeOrigem].keys()))}')
    print(f'Lista de cidades próximas: {list(cityObject[cidadeOrigem].items())}')

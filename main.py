import json

if __name__ == "__main__":
    cityObject = json.load(open("./files/cidades_sc_distancias.json", encoding="utf-8"))

    print(f'O tipo da var é: {type(cityObject)}')

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


    distancia = 999999
    destino = ""
    for destino_aux, distancia_aux in cityObject[cidadeOrigem].items():
        if (distancia_aux < distancia):
            distancia = distancia_aux
            destino = destino_aux
    
    print(f'A cidade mais próxima é: {destino} - {distancia}Km')
    

    print(f'Lista de cidades próximas: {", ".join(list(cityObject[cidadeOrigem].keys()))}')
    print(f'Array de Debug: {list(cityObject[cidadeOrigem].items())}')

import json

def Guloso_Algorythm(data: dict, origemPoint: str, destinyPoint: str):

    fullValue = 0
    keyReturn = origemPoint
    keyHistoric = [origemPoint]

    while (keyReturn != destinyPoint):
        valueControl = 999999

        for key_aux, value_aux in data[keyReturn].items():
            if (value_aux < valueControl):
                    
                valueControl = value_aux
                keyReturn = key_aux

        if (keyReturn in keyHistoric):
            print(f'Próximo caminho {keyReturn} já foi passado')
            break
        
        else:
            fullValue += valueControl
            keyHistoric.append(key_aux)
            print(f'Próximo destino: {keyReturn} - {valueControl}Km')
    
    return keyReturn, fullValue

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


    destino, distanciaTotal = Guloso_Algorythm(cityObject, cidadeOrigem, cidadeDestino) 
    
    print(f'Você chegou a seu destino {destino} - {distanciaTotal}Km Total')

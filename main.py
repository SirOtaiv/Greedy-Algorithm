import json

def Guloso_Algorythm(data: dict, origemPoint: str, destinyPoint: str):

    fullValue = 0
    keyReturn = origemPoint
    keyHistoric = [origemPoint]
    error = None

    while (keyReturn != destinyPoint):
        valueControl = float('inf')

        for key_aux, value_aux in data[keyReturn].items():
            if (value_aux < valueControl and key_aux not in keyHistoric):
                valueControl = value_aux
                keyReturn = key_aux

        if valueControl == float('inf'):
            error = "Erro: Não há caminho válido para o destino."
            break

        # if (keyReturn in keyHistoric):
        #     print(f'Próximo caminho {keyReturn} já foi passado')
        #     break
        
        fullValue += valueControl
        keyHistoric.append(keyReturn)
        print(f'Próximo destino: {keyReturn} - {valueControl}Km')

        if keyReturn not in data:
            error = f"Erro: '{keyReturn}' não existe no dicionário de cidades."
            break
    
    return keyReturn, fullValue, error

if __name__ == "__main__":
    cityObject = json.load(open("./files/cidades_sc_distancias.json", encoding="utf-8"))

    # for city in list(cityObject.keys()):
    #     print(f'Cidade {city}')
    
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


    destino, distanciaTotal, err = Guloso_Algorythm(cityObject, cidadeOrigem, cidadeDestino) 
    
    if err is not None:
        print(err)
    else:
        print(f'Você chegou a seu destino {destino} - {distanciaTotal}Km Total')

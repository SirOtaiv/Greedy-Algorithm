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
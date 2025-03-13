import json

# Definindo uma classe para representar uma cidade
class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.cidades_proximas = {}

    def adicionar_cidade_proxima(self, cidade, distancia):
        self.cidades_proximas[cidade] = distancia

# Carregar o JSON
with open("./files/cidades_sc_distancias.json", encoding="utf-8") as file:
    cityObject = json.load(file)

# Criar um dicionário para armazenar objetos Cidade
cidades_objetos = {}

# Transformando cityObject em objetos Cidade
for cidade, proximas in cityObject.items():
    cidade_obj = Cidade(cidade)
    for cidade_proxima, distancia in proximas.items():
        cidade_obj.adicionar_cidade_proxima(cidade_proxima, distancia)
    cidades_objetos[cidade] = cidade_obj

# Agora você tem objetos Cidade e pode acessar as cidades e distâncias
# Exemplo de como acessar a cidade e suas cidades próximas:
cidade_origem = cidades_objetos['Abdon Batista']  # Exemplo de cidade origem
print(f"Cidade: {cidade_origem.nome}")
for cidade_proxima, distancia in cidade_origem.cidades_proximas.items():
    print(f"Cidade próxima: {cidade_proxima} - Distância: {distancia} km")

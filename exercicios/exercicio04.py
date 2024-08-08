"""
Descrição: Crie uma classe chamada Carro com os atributos marca, modelo e ano.
Métodos:
Um método __init__ que inicializa os atributos marca, modelo e ano.
Um método mostrar_detalhes que imprime os detalhes do carro.
Teste: Crie uma instância da classe Carro, defina a marca, o modelo e o ano,
e depois chame o método mostrar_detalhes

"""
class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_descricao(self):
        print(f'A marca do seu carro e: {self.marca}\nO modelo do se carro e: {self.modelo}\nO ano de fabricação do seu carro e de: {self.ano}\n')
        
meu_carro = Carro('Fiat', 'Fiorino', 2018)

meu_carro.mostrar_descricao()
"""
Crie uma class com um metodo __init__ e outro com o nome _mostrar_resultados

no metodo __init__ crie dois parametros, 1 que pegue o nome e o outro a idade
e no segundo metodo junte essas informaçoes e nos mostre.

"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def _mostrar_informacoes(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

humano = Pessoa('Gabriel', 24)

humano._mostrar_informacoes()
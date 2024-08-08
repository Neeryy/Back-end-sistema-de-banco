"""
Descrição: Crie uma classe base chamada Pessoa com os atributos nome e idade, 
e uma classe derivada chamada Aluno que herda de Pessoa e adiciona o atributo matricula.
Métodos:

Na classe Pessoa, um método __init__ que inicializa nome e idade, e um método mostrar_informacoes.

Na classe Aluno, um método __init__ que inicializa nome, 
idade e matricula, e um método mostrar_informacoes que também imprime a matrícula.

Teste: Crie uma instância da classe Aluno, defina o nome, 
a idade e a matrícula, e depois chame o método mostrar_informacoes.

"""

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_informacoes(self):
        print(f'Seu nome e: {self.nome}, Sua idade e: {self.idade}')

class aluno(Pessoa):

    def __init__(self, nome, idade, matricula):
        Pessoa.__init__(self, nome, idade)
        self.matricula = matricula

    def mostrar_informacoes(self):
        Pessoa.mostrar_informacoes(self)
        print(f'Matricula: {self.matricula}')

aluno1 = aluno('Gabriel', 24, 154789)

aluno1.mostrar_informacoes()

"""
Nesse exercicios vimos como funciona uma herança de classe
aonde a classe PESSOA tem seus atributos e a classe ALUNO
herda as informaçoes da classe PESSOA

"""
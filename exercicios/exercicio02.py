"""
Descrição: Crie uma classe chamada Retangulo com os atributos largura e altura.
Métodos:
Um método __init__ que inicializa os atributos largura e altura.
Um método area que retorna a área do retângulo.
Um método perimetro que retorna o perímetro do retângulo.
Teste: Crie uma instância da classe Retangulo, defina a largura e a altura,
e depois chame os métodos area e perimetro

"""

class retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area1(self):
        self.area = self.altura * self.largura
        return self.area

    def perimetro1(self):
        self.perimetro = self.altura * 2
        self.perimetroo = self.largura * 2
        return self.perimetro + self.perimetroo # return e usando para retorna o valor de algo mais algo
    
figura = retangulo(5, 3)

print(figura.area1())
print(figura.perimetro1())

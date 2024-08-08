# criando nosa primeira classe com python

class TV():

    cor = 'PRETA' # colocando a opção da cor aqui ela nunca mais poderar ser mudada,
                  # esse codigo e usado para quando voce quer manter um padrão para tudo.

    def __init__(self, tamanho):
        self.canal = 'Netflix'
        self.polegadas = tamanho
        self.ligada = False
        self.volume = 20

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal


tv_quarto = TV(tamanho=80)
tv_quarto.mudar_canal('TV Kids')

print(tv_quarto.polegadas)
print(tv_quarto.canal)
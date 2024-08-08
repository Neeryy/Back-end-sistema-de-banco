from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimo = [] 

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'O valor de caixa esta baixo: {self.caixa:,.2f}')
        else:
            print(f'O valor do caixa esta OK: {self.caixa:,.2f}')


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimo.append((valor, cpf, juros))
        else:
            print('O emprestimo foi negado pelo fato do caixa esta baixo')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000
        self.caixa_peypal = 0

    def depositar_peypal(self, valor):
        self.caixa -= valor
        self.caixa_peypal += valor

    def sacar_peypal(self, valor):
        self.caixa_peypal -= valor
        self.caixa += valor


class AgenciaPremiu(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio < 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não tem o patrimonio menimo para entrar na agencia premiun')


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000





if __name__ == '__main__':
    age = Agencia(111111111, 525252525, 4568)

    age.caixa = 1000000

    age.verificar_caixa()

    age.adicionar_cliente('Gabriel', 1234567890, 200)
    print(age.clientes)
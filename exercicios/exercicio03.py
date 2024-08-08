"""
Descrição: Crie uma classe chamada ContaBancaria com os atributos numero_conta e saldo.
Métodos:
Um método __init__ que inicializa os atributos numero_conta e saldo.
Um método depositar que adiciona um valor ao saldo.
Um método sacar que subtrai um valor do saldo, se houver saldo suficiente.
Um método mostrar_saldo que exibe o saldo atual da conta.
Teste: Crie uma instância da classe ContaBancaria, faça depósitos e saques, 
e depois chame o método mostrar_saldo

"""

class ContaBancaria:

    def __init__(self, num_conta, saldo):
        self.num_conta = num_conta
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'Seu saldo e de: {self.saldo:,.2f}')
    
    def depositar(self, valor):
        self.saldo += valor
        return self.depositar
    
    def sacar(self, valor):
        self.saldo -= valor
        return self.sacar
    
conta_gabriel = ContaBancaria('1234', 2000)

conta_gabriel.depositar(1000)

conta_gabriel.sacar(2500)

conta_gabriel.mostrar_saldo()



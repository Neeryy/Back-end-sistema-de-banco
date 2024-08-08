from datetime import datetime
from random import randint

class ContaCorrente:

# metodo de apoio aonde mostra as horas 
    @staticmethod
    def _data_hora():
        data = datetime.now()
        return data.strftime('%d/%m/%Y - %H:%M:%S')
    
# Metodo inicial 
    def __init__(self, nome, cpf, agencia, num_conta):   # essa função e a nossa função principla da nossa classe
        self.nome = nome             # mesmo criando def novas sempre sera baseadas nessas
        self.cpf = cpf               # como no exemplo abaixo.
        self.saldo = 0
        self.limite = None
        self.num_conta = num_conta
        self.agencia = agencia
        self.transacao = []
        self.cartoes = []

 # consulta o saldo atual da conta   
    def consultar_saldo(self):
        print(f'Seu saldo e de R${self.saldo:,.2f}')

# deoisita qualquer valor na conta destinada
    def despositar_saldo(self, valor):
        self.saldo += valor
        self.transacao.append((valor, self.saldo, ContaCorrente._data_hora()))

# define um limite de cheque especial
    def _limite_conta(self): # o uso do _ em uma metodo de classe, significa que esse metodo
        self.limite = -3000  # foi criado apenas para teste, um metodo PRIVADO.
        return self.limite
    
# Sacando um valor da conta
    def sacar_saldo(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Voce não tem saldo o suficiente')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacao.append((-valor, self.saldo, ContaCorrente._data_hora()))

# consultando o limite disponivel de cheque especial da conta
    def consultar_limite_chequeespecial(self):
        print(f'Seu saldo de cheque especial e de: {self._limite_conta():,.2f}')

# mostrando historioco de transaçoes 
    def consultar_historico_transacoes(self):
        print('Historico de transaçoes')
        print('Valor, Saldo, Hora')
        for transacoes in self.transacao:
            print(transacoes)

# retirando um valor de uma conta e passando para outra conta
    def tranferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacao.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacao.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        data = datetime.now()
        return data #strftime('%d/%m/%Y - %H:%M:%S')

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}' # validade do cartão de credito
        self.codigo_seguranca = f'{randint(0 , 9)}{randint(0 , 9)}{randint(0 , 9)}'
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)


    @property  # metodo get
    def senha(self):
        return self.senha
    
    @senha.setter # metodo setter, que verifica se a senha esta no padrão
    def senha(self, valor):
        if len(valor) == 4 and valor.is_numeric():
            self.senha = valor
        else:
            print('Nova senha invalida')
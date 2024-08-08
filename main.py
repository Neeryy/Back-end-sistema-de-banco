from contasbancos import ContaCorrente, CartaoCredito

# criando a conta
conta_gabriel = ContaCorrente('Gabriel', '123.456.678-12', 123, 123456)
conta_gabriel.consultar_saldo()

cartao_gabriel = CartaoCredito('Gabriel Nery', conta_gabriel)

print(cartao_gabriel.conta_corrente.num_conta)

print(conta_gabriel.cartoes[0].numero)

print(cartao_gabriel.codigo_seguranca)
from gestionale_pagamento import *

buro = Pagamento()
buro.setPagamento(20)
print(buro.getPagamento())
buro.dettagliPagamento()

pagamento = PagamentoContanti()
pagamento.setPagamento(1255.65)
print(pagamento.inPezziDa())
pagamento.dettagliPagamento()


pagamento1 = PagamentoCartaDiCredito("Luca Toni", date(2027, 9, 12), "AAAABBBBCCCCDDDD")
pagamento1.setPagamento(20000)
print(pagamento1.dettagliPagamento())
class Pagamento:

    _importo_pagamento:float 

    def __init__(self) -> None:
        self._importo_pagamento = 0
    
    def setPagamento(self, soldi:float) -> None:
        self._importo_pagamento = soldi

    def getPagamento(self) -> float:
        return self._importo_pagamento
    
    def dettagliPagamento(self) -> None:
        print(f"Importo del pagamento: {self._importo_pagamento:.2f}")
    
# sburo = Pagamento()
# sburo.setPagamento(20)
# print(sburo.getPagamento())
# sburo.dettagliPagamento()

class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()

        self._importo_pagamento = self.getPagamento()

    def dettagliPagamento(self):
        return super().dettagliPagamento()
    
    def inPezziDa(self) -> None:
        pass


pagamento = PagamentoContanti()
pagamento.setPagamento(255)
pagamento.inPezziDa()




from datetime import date 

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
    


class PagamentoContanti(Pagamento):

    def __init__(self):
        super().__init__()

        self._importo_pagamento = self.getPagamento()

    def dettagliPagamento(self):
        return super().dettagliPagamento()
    
    def inPezziDa(self) -> None:
        centesimi = int(round(self._importo_pagamento * 100))
        
        prezzi = [(50000, 500), (20000, 200), (10000, 100), (5000,  50 ), (2000, 20), (1000, 10), (500, 5), (200, 2) ,(100, 1),(50, 0.50),(20, 0.20),(10, 0.10),(5, 0.05),(1, 0.01)]

        risultato = []
        banconota_or_moneta = ""

        for valore, prezzo in prezzi:
            n_volte = centesimi // valore  

            if n_volte > 0:

                if prezzo >= 5:
                    banconota_or_moneta = "banconota/e"
                else:
                    banconota_or_moneta = "moneta/e"

                risultato.append(f"{n_volte} {banconota_or_moneta} da {prezzo}€")
                centesimi %= valore

        print(f"Pagamento in contanti di: {self._importo_pagamento}\n{self._importo_pagamento} euro da pagare in contanti con: ")
        return "\n".join(risultato)



class PagamentoCartaDiCredito(Pagamento):

    _titolare_carta:str 
    _data_scadenza:date
    _numero_cartacredito:str

    def __init__(self, titolare_carta:str, data_scadenza:date, numero_cartacredito:str):
        super().__init__()

        self._importo_pagamento = self.getPagamento()
        self._titolare_carta = titolare_carta
        self._data_scadenza = data_scadenza
        self._numero_cartacredito = numero_cartacredito

    def dettagliPagamento(self):
        return f"Pagamento di {self._importo_pagamento}€, effettuato con la Carta di Credito!\nTitolare della Carta di Credito: {self._titolare_carta}\nData di scadenza: {self._data_scadenza}\nNumero Carta di Credito: {self._numero_cartacredito}"


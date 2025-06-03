



class Aereporto:

    _nome:str
    _codice:str

    def __init__(self, nome:str, codice:str) -> None:

        self._nome = nome 
        self._codice = codice

    def get_codice(self) -> str:

        return self._codice 
    
    def set_nome(self, nome_aereporto:str) -> None:

        self._nome = nome_aereporto

    def get_nome(self) -> str:

        return self._nome
    

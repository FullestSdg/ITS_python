class Facoltà:

    _nome:str # noto alla nascita
    _tipo_facoltà:str # noto alla nascita

    def __init__(self, nome:str, tipo_facoltà:str) -> None:

        self._nome = nome 
        self._tipo_facoltà = tipo_facoltà

    def nome(self) -> str:  
        return self._nome 
    
    def tipo_facoltà(self) -> str:
        return self._tipo_facoltà
    
    
    def set_nome(self, nuovo_nome:str) -> None:
        self._nome = nuovo_nome
    
    def set_tipo_facoltà(self, nuova_tipo_facoltà:str) -> None:
        self._tipo_facoltà = nuova_tipo_facoltà
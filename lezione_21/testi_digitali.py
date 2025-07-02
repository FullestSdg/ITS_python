

class Documento:

    _testo:str

    def __init__(self, testo:str) -> None:
        self._testo = self.setText(testo)

    def setText(self, testo:str) -> None:
        self._testo = testo 

    def getText(self) -> str:
        return self._testo 
    
    def isInTest(self, parola:str) -> bool:

        testo = self._testo.split()

        for parole in testo:

            if parole.lower() == parola:
                return True 
            
            else:
                return False

class Email(Documento):

    _mittente:str 
    _destinatario:str
    _titolo_messaggio:str 

    def __init__(self, testo:str, mittente:str, destinatario:str, titolo_messaggio:str) -> None:   
        super().__init__(testo)
        self._mittente = self.setMittente(mittente)
        self._destinatario = self.setDestinatario(destinatario)
        self._titolo_messaggio = self.setTitoloMessaggio(titolo_messaggio)

    def setMittente(self, mittente:str) -> None:
        self._mittente = mittente

    def getMittente(self) -> str:
        return self._mittente

    def setDestinatario(self, destinatario:str) -> None:
        self._destinatario = destinatario

    def getDestinatario(self) -> str:
        return self._destinatario

    def setTitoloMessaggio(self, titolo_messaggio) -> None:
        self._titolo_messaggio = titolo_messaggio

    def getTitoloMessaggio(self) -> None:
        return self._titolo_messaggio

    def getText(self) -> str:
        
        return f"Da: {self._mittente}, A: {self._destinatario}\nTitolo: {self._titolo_messaggio}\nMessaggio: {self._testo}"

    def writeToFile(self, nome_percorso:str):
        
        with open(nome_percorso, "w") as file:

            file.write(self.getText())


class File(Documento):

    _nomePercorso:str 

    def __init__(self, nomePercorso:str) -> None:
        self._nomePercorso = self.setnomePercorso(nomePercorso)
        super().__init__(self.leggiTestoDaFile)

    def setnomePercorso(self, nome_percorso:str) -> None:
        self._nomePercorso = nome_percorso

    def getnomePercorso(self) -> str:
        return self._nomePercorso

    def leggiTestoDaFile(self) -> str:
        
        with open("document.txt", "r") as reader:
            testo = reader.read()

            return testo

    def getText(self) -> str:

        return f"Percorso: {self._nomePercorso}\nContenuto: {self.leggiTestoDaFile()}"

documento = Documento("ciao giuseppe roberto!")

email = Email("ciao giuseppe", "sdgsergiodg20@gmail.com", "candidodomenico87@gmail.com", "Esdrongo")

file = File("document.txt")

print(email.getText())
print("")
print(file.getText())
print("")
print(email.isInTest("ciao"))
print("")
print(file.isInTest("questo"))



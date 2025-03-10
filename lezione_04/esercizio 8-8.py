while True:
    name:str = input("Inserisci il nome di un artista: ")
    album_title:str = input("Inserisci il nome dell'album: ")

    def make_album(name:str, album_title:str, number_songs:int = None ):
        
        return {f"Artist : {name}, Album's Name : {album_title}"}

    mydict = make_album(name, album_title)
    print(mydict)

    

    if name == "stop" or album_title == "stop":
        break
def make_album(name:str, album_title:str, number_songs:int = None ):

    if number_songs != None:
        return {f"Artist : {name}, Album's Name : {album_title}, Number of songs : {number_songs}"}
    
    else:
        return {f"Artist : {name}, Album's Name : {album_title}"}
    
mydict1 = make_album("Imagine Dragons", "Origins")
print(mydict1)

mydict2= make_album("Imagine Dragons", "Evolve")
print(mydict2)

mydict3 = make_album("Imagine Dragons", "Night Visions")
print(mydict3)

mydict4 = make_album("Imagine Dragons", "Loom", 7)
print(mydict4)

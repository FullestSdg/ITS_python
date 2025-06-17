from typing import Any

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
# Perform following operations on given dictionary

'''
Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
Check if Key Exists in the dictionary
'''

my_dict.pop("profession")
print(my_dict)

for key in my_dict.keys():
    print(key)

def does_key_exist(my_dict:dict[str : Any], key:str ):

    my_dict_key:list[str] = []

    for k in my_dict.keys():

        my_dict_key.append(k)

    if key in my_dict_key:

        return True
    
    else:
        return False

key1 = "age"
key2 = "profession"

risultato1 = does_key_exist(my_dict, key1)
risultato2 = does_key_exist(my_dict, key2)
print(f"La chiave '{key1}' è nel dizionario {my_dict}?\n-----\nEsito: {risultato1}\n\nLa chiave '{key2}' è nel dizionario {my_dict}?\n-----\nEsito: {risultato2}")

'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print(f"Original dictionary: {my_dict}")

# Remove the 'model' key-value pair using del
del my_dict['profession']
print(f"Updated dictionary after removing 'profession': {my_dict}")

print("Printing all key-value pairs:")
for key, value in my_dict.items():
  print(f"{key}: {value}")
  
def check_key_exists(dictionary, key_to_check):
  return key_to_check in dictionary

key1 = 'age'
print(f"Does '{key1}' exist? {check_key_exists(my_dict, key1)}")

'''
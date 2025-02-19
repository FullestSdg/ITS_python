glossary: dict = {"sorted()": "to print your list in alphabetical order without modifying the actual list",
                  "sorted(reverse=True)":"to print your list in reverse-alphabetical order without changing the order of the original list",
                  "reverse()":"to change the order of your list",
                  "sort()" : "to change your list so it’s stored in alphabetical order",
                  "sort(reverse=True)":"to change your list so it’s stored in reverse-alphabetical order"}

parola1 = glossary["sorted()"]
print("sorted()\n",parola1)

parola2 = glossary["sorted(reverse=True)"]
print("sorted(reverse=True)\n",parola2)

parola3 = glossary["reverse()"]
print("reverse()\n",parola3)

parola4 = glossary["sort()"]
print("sort()\n",parola4)

parola5 = glossary["sort(reverse=True)"]
print("sort(reverse=True)\n",parola5)

# Con ciclo for

for i,x in glossary.items():
    print(i,"\n",x)
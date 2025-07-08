'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.
    Metodi:
    - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
    - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
    - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
    - list_recipes(): Elenca tutte le ricette esistenti.
    - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
    - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
'''

class RecipeManager:

    _ricette = {}

    def create_recipe(self, name:str, ingredients:list[str]) -> dict | str:

        for keys in self._ricette.keys():

            if keys == name:
                return f"La ricetta {name} esiste già!"

        self._ricette[name] = ingredients
        return {name: ingredients}
    
    def add_ingredient(self, recipe_name:str, ingredient:str) -> None:
        
        for keys, values in self._ricette.items():

            if keys == recipe_name:

                if ingredient in values:
                    return f"L'ingrediente {ingredient} è già presente nella ricetta!"

                else:
                    values.append(ingredient)

        return {recipe_name : self.list_ingredients(recipe_name)}
    
    def remove_ingredient(self, recipe_name:str, ingredient:str) -> None:
        
        for keys, values in self._ricette.items():

            if keys == recipe_name:

                if ingredient in values:
                    values.remove(ingredient)

                else:
                    return f"L'ingrediente {ingredient} non è presente nella ricetta"
        
        return {recipe_name : self.list_ingredients(recipe_name)}

    def update_ingredient(self, recipe_name:str, old_ingredient:str, new_ingredient:str) -> None:
        
        if recipe_name not in self._ricette:
            return f"La ricetta {recipe_name} non esiste!"
    
        for values in self._ricette.values():

            if old_ingredient not in values:
                return f"L'ingrediente {old_ingredient} non è presente nella ricetta"
            
            else:
                index = values.index(old_ingredient)
                values[index] = new_ingredient

        return {recipe_name : self.list_ingredients(recipe_name)}

    def list_recipes(self) -> list[dict[str,str]]:
        
        for keys in self._ricette.keys():
            return [keys]
    
    def list_ingredients(self, recipe_name) -> list[str] | str:
        
        for keys in self._ricette.keys():
            
            if keys == recipe_name:
                return self._ricette[keys]

    def search_recipe_by_ingredient(self, ingredient) -> dict[str,list[str]]:
        
        for keys, value in self._ricette.items():

            if ingredient in value:

                return self._ricette

# manager = RecipeManager()
manager2 = RecipeManager()
# print(manager.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
# print(manager.create_recipe("Torta di zucche", ["Farina", "Uova", "Zucche"]))
# print(manager2.create_recipe("Torta di mele", ["Farina", "Uova", "Mele"]))
# print(manager.add_ingredient("Torta di mele", "Burro"))
# print(manager.add_ingredient("Torta di mele", "Farina"))
# print(manager.remove_ingredient("Torta di mele", "Burro"))
# print(manager.remove_ingredient("Torta di mele", "Zucchero"))
# print(manager.update_ingredient("Torta di mele", "Uova", "Latte"))
# print(manager.update_ingredient("Torta di mele", "Francesco Totti", "Latte"))
# print(manager.update_ingredient("Torta di pere", "Uova", "Latte"))
# print(manager.list_recipes())
# print(manager.list_ingredients("Torta di mele"))
# print(manager.search_recipe_by_ingredient("Farina"))

manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Acqua', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
{'Pizza Margherita': ['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']}
['Farina', 'Lievito', 'Pomodoro', 'Mozzarella di Bufala', 'Basilico']
        

            
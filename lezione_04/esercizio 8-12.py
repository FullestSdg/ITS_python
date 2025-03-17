def sandwiches(*args) -> str:

    return args

ingredienti:str = sandwiches("panino", "salame", "formaggio")
ingredienti2:str = sandwiches("toast", "prosciutto", "formaggio")
ingredienti3:str = sandwiches("panino", "salsiccia", "friarelli")

print(f"Il panino contiene: {ingredienti}")
print(f"Il panino contiene: {ingredienti2}")
print(f"Il panino contiene: {ingredienti3}")

print(type(ingredienti))

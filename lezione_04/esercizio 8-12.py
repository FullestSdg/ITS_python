def sandwiches(*args) -> tuple:

    return args

ingredienti:tuple = sandwiches("panino", "salame", "formaggio")
ingredienti2:tuple = sandwiches("toast", "prosciutto", "formaggio")
ingredienti3:tuple = sandwiches("panino", "salsiccia", "friarelli")

print(f"Il panino contiene: {ingredienti}")
print(f"Il panino contiene: {ingredienti2}")
print(f"Il panino contiene: {ingredienti3}")


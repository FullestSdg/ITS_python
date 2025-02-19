numeri: dict = {"Sergio":"20", "Alessandro":"17", "Giuseppe":"46", "Daniel":"69", "Daniele":"104"}

numero1 = numeri["Sergio"]
print("Sergio",numero1)

numero2 = numeri["Alessandro"]
print("Alessandro",numero2)

numero3 = numeri["Giuseppe"]
print("Giuseppe",numero3)

numero4 = numeri["Daniel"]
print("Daniel",numero4)

numero5 = numeri["Daniele"]
print("Daniele",numero5) 

# Con ciclo for 

for i,x in numeri.items():
    print(i,x)

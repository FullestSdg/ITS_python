# def filter_and_concat(nums:list[int], min_val:int) -> str:

#     numeri_maggiori = []
    
#     for n in nums:

#         if n > min_val:

#             numeri_maggiori.append(n)

#     return ",".join([str(n) for n in numeri_maggiori])

# print(filter_and_concat([1,2,3,4,5], 3))

def calculate_std_dev(nums:list[float]) -> float:

    if len(nums) != 0:

        somma = 0

        for n in nums:
            somma += n 

        media = somma / len(nums)

        pre_varianza = 0 
        
        for n in nums:
            pre_varianza += (n-media)**2 

        varianza = pre_varianza / len(nums)

        deviazione_standard = varianza ** 0.5 

        return deviazione_standard
    
    else:
        raise ValueError("lista vuota")
    
print(calculate_std_dev([1.0,2.0,3.0,4.0,5.0]))
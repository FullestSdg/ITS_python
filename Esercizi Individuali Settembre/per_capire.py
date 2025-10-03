def dedup_stable(nums: list[int]) -> list[int]:
    
    if len(nums) == 0 or len(nums) == 1:
        return None 
    
    else:
        lista_non_duplicati = [nums[0]]

        for n in nums[1:]:

            if n != lista_non_duplicati[-1]:
                lista_non_duplicati.append(n)

    return lista_non_duplicati

print(dedup_stable([1,2,1,2,2]))

duce = [1,2]
print(duce[-1])
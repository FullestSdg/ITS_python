def int_to_roman(num:int) -> str:

    val:list[int] = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

    syms:list[str] = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", 
                      "X", "IX", "V", "IV", "I"]
    
    roman:str = ""

    for i in range(len(val)):

        while num >= val[i]:

            roman += syms[i]

            num -= val[i]

    return roman

print(int_to_roman(122))
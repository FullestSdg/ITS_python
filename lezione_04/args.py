mylist:list[int] = [1,2,3,4,5]

print(mylist)
print(*mylist) # "*" is crazy

mylist2:list[int,float] = [10,2.5]

print(*mylist2)
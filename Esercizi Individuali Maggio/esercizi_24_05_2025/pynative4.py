#Exercise 5: Merge two Python dictionaries into one
#Write a code to merge two dictionaries into a new dictionary and print it.

#Given:

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1 | dict2
print(dict3)

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

dict3 = {**dict1,**dict2}
print(dict3)

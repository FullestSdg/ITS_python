#Exercise 6: Count Character Frequencies
#Given a string, create a dictionary where keys are characters and values are their frequencies in the string.

#Given:

string1 = 'Jessa'
#Expected Output:

#Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}

def count_char_frequencies(input_string):
  
  frequency_dict = {}

  for char in input_string:
    # Use get() method: if char is in dict, get its value; otherwise, default to 0
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
  return frequency_dict

string1 = 'Jessa'
print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")

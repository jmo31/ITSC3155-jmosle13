# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes a string and
# returns the multiple of three that occurs the most
# in the string. For example, 093699 would return 9
# since 9 has occurred the most and is a multiple of 3.

def count_threes(n):
  threes_dict = {}
  for i in n:
    if i in threes_dict and (i == '3' or i =='6' or i == '9'):
      threes_dict[i] += 1
    else:
      threes_dict[i] = 0
  threes_result = int(max(threes_dict, key = threes_dict.get))
  return threes_result
# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
# If there is a tie between different characters, it should
# return all the tied characters.
def longest_consecutive_repeating_char(s):
  long_dict = {}
  count = 0
  letter = s[0]
  conseq_list = []
  for i in range(len(s)):
    conseq_count = 1
    for x in range(i+1, len(s)):
      if s[i] != s[x]:
         break
      conseq_count += 1
    if conseq_count >= count:
      count = conseq_count
      letter = s[i]
      long_dict[letter] = count
  dict_keys = long_dict.keys()
  dict_values = long_dict.values()
  max_value = 0
  for dict_keys, dict_values in long_dict.items():
    if(max_value < dict_values):
      max_value = dict_values
  for dict_keys, dict_values in long_dict.items():
    if(max_value == dict_values):
      conseq_list.extend(dict_keys)
  return conseq_list
# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  s = s.upper().replace(' ', '')
  if str(s) == str(s[::-1]):
      return True
  else:
      return False

  return

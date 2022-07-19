'''4. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to $;, except the first char itself.'''
def string_replace(str1):
  first_char = str1[0]
  modified_string= str1.replace(first_char, '$')
  str = first_char + modified_string[1:]
  return str

print(string_replace('restart'))
print(string_replace('except'))
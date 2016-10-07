import string

all_alpha = string.ascii_lowercase

def is_pangram(str1):
  result = []
  for c in str1.lower():
    if c in all_alpha and c not in result:
      result.append(c)
  if len(result) == len(all_alpha):
    return True
  else:
    return False


string1 = raw_input("Enter the String:")
print is_pangram(string1)


#test
#print is_pangram("The quick brown fox jumps over the lazy dog.")
#print is_pangram("Obviously not a pangram")

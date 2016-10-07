def filter_long_words(lst, n):
  return [w for w in lst if len(w) > n]

print filter_long_words(['Hello', 'world', 'Haiti', 'Pythonistas!'], 5)
print filter_long_words(['Python', 'stole', 'my', 'heart'], 4)
print filter_long_words(['This', 'will', 'be', 'cool'], 3)

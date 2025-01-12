def only_english(string):
  return "".join([char for char in string if char.isalpha()])

print(only_english('Hell0 w0r1d'))
def add2list(lst1, lst2):
  if len(lst1) == len(lst2):
      return [lst1[i] + lst2[i] for i in range(len(lst1))]
  else:
      return -1

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print(add2list(x, y))
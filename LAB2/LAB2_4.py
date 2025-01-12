def count_minus(str):
  return [sum(1 for number in str if number < 0)]

data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
print(count_minus(data))
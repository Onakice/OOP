def delete_minus(nums):
  return [list(filter(lambda item: item >= 0, num)) for num in nums]

x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]
print(delete_minus(x))
input_string = input("Enter string : ")
lowercase_count = sum(1 for char in input_string if char.islower())
uppercase_count = sum(1 for char in input_string if char.isupper())
print(lowercase_count)
print(uppercase_count)
largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j

        if str(product) == str(product)[::-1] and product > largest_palindrome:
            largest_palindrome = product

print("Palindrome with 3 digit", largest_palindrome)
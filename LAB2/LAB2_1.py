input = input()

numbers = [int(num) for num in input.split()]

sorted_numbers = sorted(numbers)

print(sorted_numbers)

if sorted_numbers[0] == 0:
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] != 0:
            sorted_numbers[0], sorted_numbers[i] = sorted_numbers[i], sorted_numbers[0]
            break

result = ''.join(map(str, sorted_numbers))
print(result)
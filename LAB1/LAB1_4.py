a = input("Input: ")

if len(a) == 1 and a.isdigit():
    a = int(a)
    result = a + int(str(a) * 2) + int(str(a) * 3) + int(str(a) * 4)
    print("Output:", result)
else:
    print("Error")
    exit()
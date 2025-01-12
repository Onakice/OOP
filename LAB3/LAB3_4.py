def char_count(str):
    char_count = {}

    for char in str:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(char_count('language'))

print(char_count('pongsapak tatongjai'))
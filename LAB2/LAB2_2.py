# x = ['abba', 'banana', 'ann']
# c = 'a'

# d = [s.count(c) for s in x]
# print(d)

def count_char_in_string(words, char):
  return [word.count(char) for word in words]

# w, c = input()
# print(count_char_in_string(w,c))

# input_str = input("Enter words and character : ")
# w, c = input_str.split()
# # result = count_char_in_string(w, c)
# # print(result)
# print(count_char_in_string(w, c))

user_input = input()
input_list = user_input.split()
w = input_list[:-1]
c = input_list[-1]
print(count_char_in_string(w, c))
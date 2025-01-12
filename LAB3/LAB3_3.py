def is_plusone_dictionary(dic):
  dic_arr = [value for item in dic.items() for value in item]
  return dic_arr == sorted(dic_arr) and dic_arr == list(range(min(dic_arr), max(dic_arr) + 1))

print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}))        #print True

print(is_plusone_dictionary({1:2, 3:10, 5:6, 7:8}))       #print False

print(is_plusone_dictionary({1:2, 2:3, 3:4, 4:5}))        #print False

print(is_plusone_dictionary({9:10, 11:12, 13:14, 15:16})) #print True
lst = ['hello', 1, 2, 'java', 'python', 9, True, 9.2, 'rust', 'c++', 8]

for item in lst[:]:
    if type(item) is str:
        lst.remove(item)

print (lst)
#Out: [1, 2, 9, True, 9.2, 8]
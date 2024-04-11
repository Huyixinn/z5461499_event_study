lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
lst1 = []
for i in lst:
    if i * i > 150:
        lst1.append(i * i)
    else:
        continue
    i = i + 1
print(lst1)



lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
new_lst = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_lst}')


numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
s_number = set(numbers)
lst = []
for i in s_number:
    if i % 2 == 0:
        lst.append(i)
print(lst)




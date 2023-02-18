lst = [x for x in range(1, 20)]
print(lst)

lst = map(lambda x: x + 10, lst)
print(lst)

lst = list(map(lambda x: x + 10, lst))
print(lst)

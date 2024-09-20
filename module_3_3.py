def print_params(a = 1, b = 'line', c = True):
    print(a, b, c)
#1
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
#2
value_list = (15, 'Yes', False)
print_params(*value_list)
values_dict = {'a' : 1, 'b' : 'apple', 'c' : False}
print_params(**values_dict)
#3
value_list2 = (54.32, 'строка')
print_params(*value_list2, 42)
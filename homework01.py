def sum(num):
    return num+num

def map(func, array):
    new_list = []
    for el in array:
        new_list.append(func(el))
    return new_list

my_list = [1,3,5,7,9]
print(map(sum,my_list))
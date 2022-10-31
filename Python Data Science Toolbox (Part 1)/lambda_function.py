from functools import reduce
#example of function lambda
raise_to_power = lambda x,y: x**y

print(raise_to_power(2,3))

num_list = [1,2,3,4,5,6,7,8,9,10]


square_all = map(lambda x : x ** 2, num_list)

num_new_list = list(square_all)

print(square_all)
print(num_new_list)


greetings = ["hello","bye","other greetings"]

result = reduce(lambda item1,item2: item1 + item2, greetings)

print(result)


# funciones nuevas map() filter() reduce() list() 
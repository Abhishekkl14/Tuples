tuple1 = (10, 5, 7, -10, )
tuple2 = ('os', 'Dsa')
tuple3 =(tuple1, tuple2)
print (tuple1, tuple2)

list1 = [100, 251,11]
print(tuple(list1))

print(tuple("jerry"))

print(tuple1.index(-10))

print(tuple1[1:4]) #slicing

tuple4 = tuple1+tuple2 #concatinations
print(tuple4)

repeat = tuple1*3 #REPEATING
print(repeat)

print(len(tuple2))  #length

print(10 in tuple1) #tuple membership it checks that the number is there in tuple 1 or not
print(1 in tuple1)

a, b, c, d = tuple1  #tuple unpacking
print(a, b, c, d)




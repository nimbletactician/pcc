# accessing element to list

bicycles = ['rad', 'trek', 'canondale', 'bmx']
print(bicycles[0].title())

# special syntax for accessing the last element in a list
print(bicycles[-1].title())

# access second from last element
print(bicycles[-2].title())

# add element to list
cars = ['honda','tesla', 'bmw']
cars.append('toyota')
print(cars)

# insert element into list
cars.insert(1, 'mercedes')
print(cars)

# remove element from list
if 'mercedes' in cars: 
    cars.remove('mercedes')
    print(cars)
else:
    print("not found")    

# remove element by index
del cars [0]
print(cars)

# remove element by pop method
# Removes the last element in the list
# And we have access to the removed element

motorcycles = ['suzuki','yamaha','bajaj','pulsar']

popped_motercycle = motorcycles.pop()
print(popped_motercycle)

# pop also supports removing item from a particular position
print (motorcycles.pop(1))
print (motorcycles)

# remove item by value

motorcycles.remove('suzuki')
print(motorcycles)

# Organizing a List

# Sorting a list permanently w/ sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print (cars)
# cars.sort(reverse=True)
# print (cars)

# Sorting a List Temporarily w/ sorted()

print ("Here is the original list:")
print (cars)

print ("Here is the sorted list:")
print (sorted(cars))

print ("Here is the original list:")
print (cars)

# Reversing a list
cars.reverse()
print (cars)

# length of list

print (len(cars))
print(cars[-1])

# Looping over list
for car in cars:
    print(car)

# Numerical lists

for num in range(1,5):
    print(num)

# range with step count
for num in range(1,5,2):
    print(num)

# tuples
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)


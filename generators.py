#play with generators 


##from the internet 
#will interate through an infinite sequence of numbers
#the yield prevents the memory from being created
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

x = infinite_sequence()
y = range(10) #should look up infinitity 
z = [x for x in range(20) if x %2 == 0]

a = [x**2 for x in z]
b = [x**2 for x in y]

print('a', a)
print('b', b)
print('b[0] ', b[0])
print('a[0] ', a[0])

print('x', x) #class reference 
print('y', y) #__str__ saying it is generator(0, 10)
print('y[0] ', y[0])
print('z ', z)
print('x.__next__() ', x.__next__()) 
print('y[1] ', y[1])
print('x.__next__() ',x.__next__())
print('y[2] ', y[2])
print('x.__next__() ', x.__next__())
print('y[3] ', y[3])
print('x.__next__() ', x.__next__())
print('y[4] ', y[4])



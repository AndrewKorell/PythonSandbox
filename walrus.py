

(Walrus := True)
print(Walrus)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11.5]

print([(witness2 := x) for x in a if (witness := x % 2) == 0])

print(witness) #modulo of the last rejected value
print(witness2) #last accepted value 





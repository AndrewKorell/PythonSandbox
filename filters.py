def check_input(io) :
    if io['type'] == "Input" :
        return True 
    return False 

# def check_even(number) :
#     if number % 2 == 0 :
#         return True 
#     return False 

numbers = [1,2,3,4,5,6,7,8,9,10]

io_list = [ {'offset': 0, 'type': 'Input'}, { 'offset': 1, 'type': 'Output' }]

#filter is library function filter(interator function_True/False return, interable_list_of_objects)
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
input_iterator = filter(check_input, io_list)

even_numbers = tuple(even_numbers_iterator)
print(even_numbers)


inputs = tuple(input_iterator)
for input in inputs :
    print("Input Offset: ", input['offset'])


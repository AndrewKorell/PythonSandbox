# this prints Test Test Test 
# or can print Test Point Status 

class Test(Exception) :
    def __init__(self) :
        pass

class Point(Test) :  #Change Test to Exception to print point when Point is raised
    def __init__(self) :
        pass 

class Status(Test) : #change Test to Exception to print Status when Status is raised  
    def __init__(self) :
        pass

e = [Test, Point, Status]

for x in e :
    try :
        raise x
    except Test as e:
        print("Test")
        print(repr(e))
    except Point :
        print("Point")
    except Status as e :
        print("Status")
        print('f !r', e)





 
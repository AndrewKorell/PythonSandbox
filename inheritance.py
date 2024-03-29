class parent_class :
    def __init__(self) :
        self.property1 = "property1"
    def feature1(self) :
        print("Feature 1 is working")

class child_class(parent_class):
    def __init__(self) :
        self.property2 = "property2"
    def feature2(self) :
        print("Feature 2 is working")

class child_child_class(child_class) :
    def __init__(self) :
        self.property4 = "property4"
    def feature4(self) :
        print("feature 4 is working")

goodboy = child_child_class()

goodboy.feature2()
goodboy.feature1()
goodboy.feature4()
#print(goodboy.property1)
print(goodboy.property4)
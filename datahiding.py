# python doesn't have private or protected
# a double underscore essentially makes a variable private 

class TestHiding :
    def __init__(self) :
        self.visible = 1
        self._likeprotected = 2 #have to rely on the underscore to tell user not to write to it
        self.__likeprivate = 3 #will be invisible, but still accessible with _ClassName__likeprivate

t = TestHiding()

t._likeprotected = 10

print(t.visible)
print(t._likeprotected)
print(t._TestHiding__likeprivate)
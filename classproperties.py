class Point :
    def __init__(self, x, y) :
        self._x = x
        self._y = y

    def get_x(self) :
        return self._x
    
    def set_x(self, x) :
        self._x = x

    def get_y(self) :
        return self._y
    
    def set_y(self, y) :
        self._y = y

# circle.py

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius
    
    def __str__(self) :
        return f"Area {3.14 * self._radius ** 2:.2f} Permiter {3.14 * 2 * self._radius:.2f}" 

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc= "The radius property."
    )

c = Circle(1)
print(c)

c._set_radius(10)

print(c)
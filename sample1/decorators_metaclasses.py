def add_property(cls):
    cls.new_property = property(lambda self: self._value * 2)
    return cls

@add_property
class MyClass:
    def __init__(self, value):
        self._value = value

obj = MyClass(5)
print(obj.new_property)  # Output: 10
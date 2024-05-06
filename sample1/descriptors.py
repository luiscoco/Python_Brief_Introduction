class ReversedString:
    def __get__(self, instance, owner):
        return instance._value[::-1]

    def __set__(self, instance, value):
        instance._value = value[::-1]

class MyClass:
    string = ReversedString()

    def __init__(self, value):
        self._value = value

obj = MyClass("hello")
print(obj.string)  # Output: olleh
obj.string = "world"
print(obj.string)  # Output: dlrow
# class Foo:
#     def __init__(self,x = None):
#         self._x = x
        
#     @property
#     def x(self):
#         return self._x or 0
    
#     @x.setter
#     def x(self,value):
#         self._x += value

# meu_foo = Foo(10)

# print(meu_foo.x)

# print(meu_foo._x)

# meu_foo.x = 10

# print(meu_foo.x)

# print(meu_foo._x)


'''Sintaxe sem o property'''

class Foo:
    def __init__(self,x = None):
        self._x = x
        

    def x(self):
        return self._x or 0
    

    def x_setter(self,value):
        self._x += value
        
    def x_deleter(self):
        print('deletando x')
        del self._x
        
meu_foo = Foo(10)
print(meu_foo.x())

print(meu_foo._x)
meu_foo.x_setter(10)
print(meu_foo._x)
'''ouuu'''
print(meu_foo.x())

meu_foo.x_deleter()

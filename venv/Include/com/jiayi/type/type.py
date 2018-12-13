import types


def fn():
    pass

def normalType():
    print(type(123))
    print(type("123"))
    print(type(123123.4444))
    print(type(list()))
    print(type(set()))
    print(type(tuple()))
    print(type(dict()))
    print(type(abs))
    print(type(123)==type(456))
    print(type(123)==int)
    print(type('abc')==type('123'))
    print(type('abc')==str)
    print(type('abc')==type(123))

class Animal():
    print("Animal class")
class Dog(Animal):
    print('Dog class')
class Husky(Dog):
        print("Husky class")
if __name__=='__main__':
    # normalType()
    print(type(fn),"========",types.FunctionType)
    print(type(fn)==types.FunctionType)
    print(type(abs),"========",types.BuiltinFunctionType)
    print(type(abs)==types.BuiltinFunctionType)
    print(type(lambda x: x),"========",types.LambdaType)
    print(type(lambda x: x)==types.LambdaType)
    print(type((x for x in range(10))),"========",types.GeneratorType)
    print(type((x for x in range(10)))==types.GeneratorType)

    a = Animal()
    d = Dog()
    h = Husky()
    print("isinstance h is a Husky : ", isinstance(h, Husky))
    print("isinstance h is an Animal : ", isinstance(h, Animal))
    print("isinstance(d, Dog) and isinstance(d, Animal) : ", isinstance(d, Dog) and isinstance(d, Animal))
    print("isinstance(d, Husky) : ",  isinstance(d, Husky))


    print("isinstance('a', str) ",isinstance('a', str))
    print("isinstance(123, int) ",isinstance(123, int))
    print("isinstance(b'a', bytes) ",isinstance(b'a', bytes))


    print("isinstance([1, 2, 3], (list, tuple)) ",isinstance([1, 2, 3], (list, tuple)))
    print("isinstance((1, 2, 3), (list, tuple)) ",isinstance((1, 2, 3), (list, tuple)))

    print("dir('ABC') : ", dir('ABC'))
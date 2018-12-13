class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    print('wangwangwang')
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    print('miaomiaomiao')

    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()
    print('run twice here')

if __name__=="__main__":
    dog = Dog()
    dog.run()
    cat = Cat()
    cat.run()


    a = list()
    b = Animal()
    c = Dog()
    print("a is a list", isinstance(a, list))
    print("b is an animal", isinstance(b, Animal))
    print("c is a dog", isinstance(c, Dog)," and c is also an animal", isinstance(c, Animal))

    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    run_twice(Tortoise())
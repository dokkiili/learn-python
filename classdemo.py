class MyClass:
    number = 0
    name = "noname"

# def Main():
#     me = MyClass()
#     me.number = 1234
#     me.name = "Hashsh"
#     print(me.name)

# Syntax for inheritance 

#class derived-classname(superclass-name) 

class Pet:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Cat(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)
    
# def Main():
#     thePet =  Pet("Pet",1)
#     Jack = Cat("Tom",2)

    # print(str(isinstance(Jack,Cat)))
    # print(str(isinstance(Jack,Pet)))
    # print(str(isinstance(thePet,Cat)))

class Reverse:
    "Reverse Class hold a data as it's field. and reverse it"
    

    def __init__(self,data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if  self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

def Main():
    a = Reverse('AppleCare')
    for char in a:
        print(char,end='-')



if __name__ =="__main__":
    Main()




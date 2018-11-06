"""
===================================
Part 6  :: Python class and OOP
===================================
Cover Chapter:25

use class to create objects 
-----------------------------------
"""
# 类是Python程序的组成单元，就像函数和模块一样封装 Data & Logic ,
#  data --> fields
#  logic --> methods
# class define a new namespace

# Advantage of Class
#   1. 多重实例，类是对象的工厂，对象可以读取类的属性，在自己的命名空间存储数据。
#   2. 通过继承进行定制 ，可以在类的外部重新定义属性而扩展类，还可以建立命名空间的层次结构
#   3. 运算符重载 --> 通过特定的协议方法，类可以定义对象来响应 built-in function 运算(__add__,__repr__...etc)
class  A1(object):
    COUNT = 0
    x = 1
    y = 2
    def __str__(self):
        #overloading 
        pass
    def attr(self):
        pass

#    表达式 object.attr 会从下至上搜索object-tree(对象继承树) 寻找attr属性.
#   searching B.COUNT --> A.COUNT 
class C1: # super class
    x = 1
    z = 2
class C2: # super class
    w = 3
    z = 4
#-------------------------------
class C0(C1,C2): # C1,C2 从左到右决定继承顺序，即多重继承
    x = 0
    y = 0
#-------------------------------
class B1(C0): # son 
    name = ""
class B2(C0):
    name = ""
#-------------------------------
#run test
"""
B1.x,B2.x       -->    C0.x   since C0 lower than C1 , C0.x redefines C1.x.
B1.y,B2.y       -->    C0.y   since the only place y appear
B1.z,B2.z       -->    C1.z   since C1 further to left than C2
B1.name,B2.name -->    return self.name 
"""
#-------Call object---------------
""" 
boy = B1(); 调用 boy.w  --> C2.w(boy)  #实例boy作为第一个参数
"""
class Father:
    def __init__(self,who): # Construtor 
        self.name = who
    def getName(self):
        return self.name
a = Father("father")
#------------------------------------------------
# 继承搜索如何查找属性? 继承搜索先在实例Instance中搜寻属性，然后创建实例的那个类Class,
# 之后才是所有的超类，由底端-->顶端，从左至右侧，属性一旦找到即停止.
# 类和对象有何不同? 类和实例都是命名空间，类是建立对象实例的工厂，类支持
# 运算符重载，由实例继承，类的函数是用来处理实例的特殊方法。
# 类中__init__方法，当类创建实例时，Python自动调用，叫构造函数。第一个参数叫self,
# 没有__init__方法，实例创建时只是一个命名空间。
#------------------------------------------------

"""
-----------------------------
Cover Chapter:26

Basics on class
-----------------------------
"""














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




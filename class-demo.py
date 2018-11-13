"""
=====================================================
Part 6  :: Introduction to  Python class and OOP
=====================================================
Cover Chapter:25 

use class to create objects 
=====================================================
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
# 类和对象有何不同? 类和实例都是命名空间，类是建立实例的工厂，类支持
# 运算符重载，由实例继承，类的函数是用来处理实例的特殊方法。
# 类中__init__方法，当类创建实例时，Python自动调用，叫构造函数。第一个参数叫self,
# 没有__init__方法，实例创建时只是一个空的命名空间。
#------------------------------------------------
#  Python 模型
#  Python中一切都是对象，Class、Module、Instance，
#  Module 只有一个实例，Class 可以生成多个实例。
#  class 语句生成 class对象，对class的调用生成实例。实例自动连接
#  创建实例的类。类连接超类，从左到右的顺序。
#  Python OOP 提供了代码的重用功能，是其他Python组件难以提供的。
#  类的继承、定制 是Module 和 function做不到的。
# ---------------------------------------------
#  Python程序框架
#  1.把常见的任务实现成类，混合在应用程序中，这些软件框架可以提供数据库接口，测试协议，GUI工具；
#  2.编写子类，实现方法，类树中较高位置的框架类将替代大部分工作。
#  3.理解设计模式
#---------------------------------------------


"""
==============================================
Cover Chapter:26

Basics on class
==============================================
"""

class clsName:
    def setdata(self,value):
        self.data = value
    def display(self):
        print(self.data)

class secName(clsName):
    def display(self):
        print("Current : %s" % self.data)
D1 = secName()
D1.setdata("alex") # use clsName.setdata
D1.display()  # use secName.display
"""
类存在于模块中，是模块内的属性.模块对应整个文件，类只是文件内的语句。
from myModule import Mylass
类来自于语句，实例来自调用。
执行class语句创建类对象并赋值给类变量名；
class newcls(Myclass):
    pass
"""
# 类截获Python运算符实现 Operator Overloading,如 __add__ 方法
class res:
    name = "res"
class son(res):
    pass
r = res()
s = son()
res.__dict__ # return a dict contains class object's namespace
res.__dict__.keys() # return the key
r.__class__ # <class '__main__.rec'>
son.__base__ # <class '__main__.rec'> return super class
"""
===========================================
Cover Chapter 27 more objects
===========================================
"""
# example  person.py
class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay*(1+percent))
    # print (instance)
    def __str__(self): 
        return '[Person::%s %s]' %(self.name,self.pay)

    
if __name__ =='__main__':
    bob = Person('bob jones', 'writer', 10000)
    sue = Person('sue')
    print(bob.name)
    print(sue.pay)
    print(bob.lastName())
    print(bob)
#使用继承扩展方法

class Manager(Person):  # Inherit
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay)  # call base init ,start on a supper className:Person

    def giveRaise(self,percent,bonus = 0.1): # Customize
        # instance.methods(args) --> class.methods(args) 
        return Person.giveRaise(self,percent + bonus) # use class name to avoid recurisive
    def some(self): pass     # extends                     
    

"""
组合类的其他方式 -- 设计模式
"""
class newManager(Person):
    "newManager 作为委托者管理者一个的对象person，并把方法给它"

    def __init__(self,name,pay):
        self.person = Person(name,'mgr',pay)  # 嵌入一个Person类
    def giveRaise(self,percent,bonus = 0.1):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self,attr):
        return getattr(self.person,attr) # 返回嵌入类的属性
    def __str_(self):
        return str(self.person) 

class Department:
    "Container used for manage person" 
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaise(self,percent):
        for p in self.members:
            p.giveRaise(percent)
    def showAll(self):
        for p in self.members:
            print(p)
# test 
p1 = Person('apple',pay=10000)
p2 = Person('google',"IT",10000)
p3 = Person('amazon',pay=5000)
depart = Department(p1,p2) #p1.pay=10000 p2.pay =10000
depart.addMember(p3) 
depart.giveRaise(0.1)
depart.showAll()
""" Output
[Person::apple 11000]
[Person::google 11000]
[Person::amazon 5500]
"""
# ================================
# Python Inspect Tools
print(p1.__class__)
print(p1.__class__.__name__)
print(p1.__dict__.keys())
# In class ,We should define __str__ method as blow:
# def __str__(self):
#     return '[{0}{1}]'.format(self.__class__.__name__....etc)
'''
self.__dict__ show attr of instance not class fields

'''
class AttrDisplay:
    """provides an inheritable print overload method display
    instances with their class and name=value pair.
    
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s--%s'%(key,getattr(self,key)))  
        return ', '.join(attrs)
    
    def __str__(self):
        return '[{0}: {1}]'.format(self.__class__.__name__,self.gatherAttrs())
# Now redefine the person class
class NewPerson(AttrDisplay):
    pass
""" 定制化显示类的信息 例如Person类和Manager类
"""



'''
=======================================
Chapter 28
=======================================
class 是语句，被执行（或被导入）时，产生类对象。并把对象赋值给类名 Class Object --> className
class 是复合语句，内嵌主体语句。

# execute process
class className(object):  # Assign to a classname
    data = value          # Shared class data attr
    def method(self):     # Methods
        self.member = value # Pre-instance data
When a class loaded, the class statement will execute once from head to end,
create variable/attr in the local scope.
'''  
class MixedNames:
    data = "INIT"    #第一个data
    def __init__(self,value):  
        self.data =  value  # 第二个data
    def display(self):
        print(self.data,MixedNames.data)

a = MixedNames("MOOC")
b = MixedNames("WOOC")
a.display()   # MOOC INIT
b.display()   # WOOC INIT

"""
调用 超类的构造函数 Supper.__init__(self,...)
"""
class SUP:
    def __init__(self):
        pass
class SUB(SUP):
    def __init__(self):
        SUB.__init__(self)

"""
当对象进行.运算时，会发生继承，程序代码会在内存中创建对象树
"""




class Supper:
    def method(self):
        print("Supper::method")

    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError("action must be defined!!!")
class Provide(Supper):
    def action(self):
        print("Provide::action::::")

son = Provide()
son.delegate() 

# 抽象超类 没有继承或实现该方法，而是由子类实现。
#  
# 子类自身定义的__init__ 构造函数

from abc import ABCMeta,abstractmethod

class supper(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

# X = supper() # 不能初始化抽象类
## add sub class 
class sub(supper):
    def action(self):
        print("Impled!")
X1 = sub()
X1.delegate()
"""
============================
Cover Chapter 29
============================
"""
#常用运算符重载
["__init__",'__add__',"__getattr__",'__getitem__','...etc',
"__iter__","__contains__",'__getattr__','__repr__','__str__']

# 索引与切片
class Indexer:
    "two args:instance & index"
    def __getitem__(self,index):  
        return index ** 2
X = Indexer()
print(X[2])
for i in range(5):
    print(X[i],end=" ")


print("Endhere!")


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




"""
Cover Chapter:30 How to design Class

"""
# Python & OOP 3 main idea:继承、多态、封装（隐藏数据和方法实现）
# Python 没有类型声明，属性在Runtime期间解析，实现相同接口的对象是可以交换的。
# Python不要求强制私有性，多态基于对象接口而不是类型。

# 程序员员角度：继承由属性.号启动运算，触发实例、类、超类的搜索。从设计师的角度继承定义了集合成员的关系：
# 类定义内容，子类实现了更具体化的定制。
"""
Example: 开一家Pizza 餐厅,聘请员工,为顾客服务,准备食物,机器人制作披萨

Employee: Chef -- Pizzarobot/ Server / 

"""

class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self,percent):
        self.salary = self.salary + (self.salary*percent)
    def work(self):
        print(self.name + " start Working...")
    def __repr__(self):
        return "[Employee:: name:%s, salary=%s]" % (self.name,self.salary)
    
class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,50000)
    def work(self):
        print(self.name + " makes food !")

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,40000)
    def work(self):
        print(self.name + " serve to customer.")

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)
    def work(self):
        print(self.name + " makes pizza")
# if __name__ == "__main__":
#     c3p0 = PizzaRobot("C3P0")
#     print(c3p0)
#     c3p0.work()
#     c3p0.giveRaise(0.1)
#     print(c3p0)
#     for kls in Employee,Chef,Server,PizzaRobot:
#         # create obj instance
#         obj = kls(kls.__name__)
#         obj.work()

#==========================================================

class Customer:
    def __init__(self,name):
        self.name = name
    def order(self,server):
        print(self.name," -Orders from- ",server)
    def pay(self,server):
        print(self.name,' pays for item to ',server)
    
class Oven: # 烤箱
    def bake(self):
        print("Oven bakes")
# Run a Pizza Shop
class PizzaShop:
    # init a pizzashop with some utilities.
    def __init__(self):
        self.server = Server('Pat')
        self.chef = Chef('Patrick')
        self.oven = Oven()
        
    def order(self,name):
        customer = Customer(name)    # Activate other objects
        customer.order(self.server)  # Customer orders from server
        self.chef.work()             # start workd                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        self.oven.bake()
        customer.pay(self.server)
if __name__ == "__main__":
    scene = PizzaShop()
    scene.order("HOMER") # Customer 1
    print('---')
    scene.order('Shaggy') # Customer 2 Shaggy

"""
==================================================================
Streams Process
"""
class Processor:
    def __init__(self,reader,writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self,data):
        assert False,"Converter must be defined! "
    
class UpperCase(Processor):
    def converter(self,data):
        pass

print("===========================================================")

# OOP 委托 __getattr__

class Wrap:
    def __init__(self,obj):
        self.wrapped = obj
    def __getattr__(self,attrname): 
        print("Wrap:: ",attrname)
        return getattr(self.wrapped,attrname)
class Num:
    def age(self):
        return 25
    def grade(self):
        return 100
num = Num()
a = Wrap(num) # 使用Wrap 管理任何带有属性的对象的存取如 Num, 以增强被包装的对象接口 [对象装饰器]
print(a.age())
print(a.grade())

"""类的变量名压缩
__exam ---> _Exam__exam
"""

class Exam:
    __exam = "testResults"
    def change(self,name):
        self.__exam = name

exam = Exam()
print(exam._Exam__exam)
print(exam.change("changed"))
print(exam._Exam__exam)

"""
Objcect对象持久化技术 Pickle &  Shelve
Pickle : Python Object and Bytes 序列化

"""
import shelve

class person:
    def __init__(self,name,title):
        self.name = name
        self.title = title
    def work(self):
        print(self.name + "now is start working.")
bob = person("bob li",'IT')
sue = person("sue su",'HR')
ann = person("ann na",'HR')
# Write into db
# db = shelve.open("persondb")
# for obj in (bob,sue,ann):
#     db[obj.name] = obj  --> 'bob li' = bob
# db.close()
# 
db =shelve.open('persondb')
print(len(db))
print(list(db.keys()))
bob = db['bob li']  # 从shelve db 获取实例，获取对象 不需要再事先导入person类
print(bob.__class__)


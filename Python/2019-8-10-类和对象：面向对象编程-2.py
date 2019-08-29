##继承
class Parent:
    def hello(self):
        print('父类funionn 条用')

class Child(Parent):
    def hello(self):
        print('正在调用子类')

    ##如果子类有相同名字函数，会自动屏蔽父类的函数


import random as r

class Fish:
    def __init__(self):
        print('这是Fish')

class GoldFish(Fish):
    def __init__(self):
       # Fish.__init__(self)##重新调用父类初始化方法，注意这里self是子类的实例对象
       
       super().__init__()##调用父类的方法
       print('这是金鱼')
class SHark(Fish):
    def __init__(self):
        print('这是鲨鱼')
    

##使用super
        
class Base1:
    def fool(self):
        print('我是fool 1')
class Base2:
    def fool(self):
        print('我是fool 2')
class C(Base1,Base2):
    pass

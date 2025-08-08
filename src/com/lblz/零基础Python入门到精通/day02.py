# 面向对象
print("=== 面向对象 ===")
class Dog:
    def __init__(self,name,age): #构造器
        self.name = name;
        self.age = age;
        self.__sex = 1; #如果前面有——则代表着私有属性
    def play(self): #python函数定义 如果是私有方法则在方法名前面加__代表着下划线
        print("汪汪汪~函数")
    @staticmethod
    def demo01():
        print("hello 我是一个静态方法")
    @classmethod
    def demo02(cls):
        print("hello 我是一个类方法哦")
dog = Dog("旺财",3);
print(dog.name);
print(dog.age)
# 继承
print("=== 面向对象 继承 ===")
class MidDog(Dog):
    def __init__(self): # 如果子类继承父类 那一定要手动调用父类的构造方法
        super(MidDog,self).__init__("旺财",3)
    def play(self):
        print("哐哐哐~~~")
minDog = MidDog()
minDog.play()
# 多态
print("=== 面向对象 多态 ===")
class Cat(Dog):
    def __init__(self): # 如果子类继承父类 那一定要手动调用父类的构造方法
        super(Cat,self).__init__("旺财",3)
    def play(self): #子类方法会覆盖父类方法,这点倒跟java是很像的东西
        print("滴滴滴~~~")
cat = Cat()
minDog.play()
cat.play()
print(isinstance(minDog,MidDog))
print(isinstance(minDog,Dog))
print(isinstance(cat,Dog))
# 异常
print("=== 异常 ===")
try: #常规的代码块处理异常,还有跟java异常的异常抛出
    print(1/0)
    raise Exception("这是一个抛出的错误信息")
except Exception:
    print("有异常啊,赶快处理异常")
finally:
    print("finally子语句,跟java很像哟")
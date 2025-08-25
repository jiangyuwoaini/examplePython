# import 是导入第三方软件包
import  zipfile



print("Hello World")
# 1、 python缩进
# 大多数编程语言（例如C，C ++，Java）都使用大括号{}来定义代码块。而Python使用缩进。
# 两者都是有效的并且做同样的事情。但是前一种风格更加清晰。缩进不正确将导致IndentationError。
if True:
    print('Hello')
    a = 5
if True: print('Hello'); a = 5
## 2、python基本类型 python是弱类型,并不需要指定具体类型
## 常见数组类型 数值,列表,元组,字符串,集合,字典 ...等等问题
number = 10
number1 = 1.1
website = "apple.com"
a, b, c = 5, 3.2, "Hello"
is_student = True # 布尔型
PI = 3.14
a1 = [5,10,15,20,25,30,35,40]
# 元组(Tuple)是项目的有序序列，与列表(List)相同。唯一的区别是元组是不可变的。元组一旦创建就不能修改。
t = (5,'program', 1+3j)
# Set 是唯一项的无序集合。Set 由用大括号 { } 括起来，并由逗号分隔的值的集合。集合中的项目是无序的
aset = {5,2,3,1,4}
# 大括号 {} 内定义了字典，每一项都是形式为 key:value 。键 和 值 可以是任何类型。
dmap = {1:'value','key':2}
print("a的类型",type(a))
print("a1的类型",type(a1))
print("number1的类型",type(number1))
print("flot类型转换int的值:",int(number1))
print("转换字符串内容:",float('2.5'))

# 3、运算符
x = 15
y = 4
# 输出: x + y = 19
print('x + y =',x+y)
# 输出: x - y = 11
print('x - y =',x-y)
# 输出: x * y = 60
print('x * y =',x*y)
# 输出: x / y = 3.75
print('x / y =',x/y)
# 输出: x // y = 3
print('x // y =',x//y)
# 输出: x ** y = 50625
print('x ** y =',x**y)
# 位运算符(与java类似) ========================================================
# 赋值运算符(与java类似)  ========================================================
# 比较运算符 ========================================================
# 输出: x > y 是 False
print('x > y 是 ',x>y)
# 输出: x < y 是 True
print('x < y 是 ',x<y)
# 输出: x == y 是 False
print('x == y 是 ',x==y)
# 输出: x != y 是 True
print('x != y 是 ',x!=y)
# 输出: x >= y 是 False
print('x >= y 是 ',x>=y)
# 输出: x <= y 是 True
print('x <= y 是 ',x<=y)

# 逻辑运算符 ========================================================
x = True
y = False
print('x and y 是 ',x and y)
print('x or y 是 ',x or y)
print('not x 是 ',not x)
# 特殊运算符 ========================================================
# is	如果操作数相同，则为真（引用同一对象）	x为真
# is not	如果操作数不相同，则为真（不引用同一对象）	x不是真
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# 输出: False
print(x1 is not y1)
# 输出: True
print(x2 is y2)
# 输出: False
print(x3 is y3)
# 成员运算符
# 用于测试在序列（字符串，列表，元组，集合和字典）中是否找到值或变量。
# 在字典中，我们只能测试键的存在，而不是值。
# in	如果在序列中找到值/变量，则为真	5 in x
# not in	如果在序列中未找到值/变量，则为真	5 not in x
x = 'Hello world'
y = {1:'a',2:'b'}
# 输出: True
print('H' in x)
# 输出: True
print('hello' not in x)

# 4、控制运算符
num = 3
if num > 0:
    print(num, "这是一个正数.")

if num > 0:
    print("正数")
elif num == 0:
    print("0")
else:
    print("负数")

genre = ['pop', 'rock', 'jazz']
# 使用索引遍历列表
for i in range(len(genre)):
    print("I like", genre[i])

counter = 0

while counter < 3:
    print("内部循环")
    counter = counter + 1
else:
    print("else语句")

for val in "string":
    if val == "i":
        break
    print(val)

# pass语句
# pass语句为空语句。在Python中，注释和pass语句之间的区别在于，尽管解释器完全忽略注释，而pass不会被忽略。
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

# 5、函数
def my_func(name):
    # Global 关键字
    # global关键字允许您在当前作用域之外修改变量。它用于创建全局变量并在局部上下文中对该变量进行更改。
    global a1;
    print("入参==",name);
    return (name+website);
print("函数的内容:",my_func("小小小"))
# 匿名函数
double = lambda x: x * 2
# 等同于
# def double(x):
#    return x * 2


# Python 全局,局部和非局部变量
# 跟java差不多,定义在类的是全局,定义在方法的是局部,非局部变量用于未定义局部作用域的嵌套函数。这意味着该变量既不能在局部范围内，也不能在全局范围内

# Python 文件操作(个人没细看,也就是操作相关file内容)
# IO流写入文件
# f = open("img.bmp",'r+b') # 以二进制模式读取和写入
# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
# IO流读取文件
# f = open("test.txt",'r',encoding = 'utf-8')
# f.read(4)    # 读取前4个数据
# f.tell()    # 获取当前文件位置
# f.readline() # 读取一行数据
# File文件的操作细节
# os.getcwd() 获取当前目录
# os.getcwd() 更改目录
# os.mkdir('test') 创建新目录
# os.listdir() 重命名目录或文件
# os.remove('old.txt') （删除）文件

# 异常
# try:
#    #执行某些代码
#    pass
# except ValueError:
#    # 处理ValueError异常
#    pass
# except (TypeError, ZeroDivisionError):
#    # 处理多个异常
#    # TypeError 和 ZeroDivisionError 异常
#    pass
# except:
#    # 处理所有其他异常
#    pass

# finally:
# try:
#    f = open("test.txt",encoding = 'utf-8')
#    # 执行文件操作
# finally:
#    f.close()

# 自定义异常
# 定义Python用户定义的异常
# class Error(Exception):
#    """其他异常的基类"""
#    pass
#
# class ValueTooSmallError(Error):
#    """当输入值太小时引发"""
#    pass
#
# class ValueTooLargeError(Error):
#    """当输入值过大时引发"""
#    pass


# 6、对象
class Parrot:

    # 类属性
    species = "鸟"
    # 示例属性 初始化构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 示例方法
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
# 示例化Parrot类
blu = Parrot("麻雀", 10)
woo = Parrot("鹦鹉", 15)
# 访问类属性
print("麻雀是 {}".format(blu.__class__.species))
print("鹦鹉也是 {}".format(woo.__class__.species))
# 访问示例属性
print("{} 有 {} 岁".format( blu.name, blu.age))
print("{} 有 {} 岁".format( woo.name, woo.age))
class MyClass:
	"这是我的第二个类"
	a = 10
	def func(self):
		print('Hello')
# 输出: 10
print(MyClass.a)
# 输出: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)
# 输出: '这是我的第二个类'
print(MyClass.__doc__)


# Python继承语法
# class BaseClass:
#   #基类主体
# class DerivedClass(BaseClass):
#   #派生类的主体

#python中的多重继承
# class Base1:
#     pass
# class Base2:
#     pass
# class MultiDerived(Base1, Base2):
#     pass
import json
import os.path
import pickle
import random
import sys
import math
import day03
from io import StringIO
from io import BytesIO
# 模块
print("=== 模块 ===")
print(day03.__name__)
print(dir(day03)) #dir函数 可以列出对象的模块标识符,标识符有函数,类和变量
day03.fib(10)
for path in sys.path: #sys模块是系统模块
    print(path)
print(sys.modules) #查找已导入的模块
print(os.path.exists("c:")) #os模块就相当于java file类
print("圆周率: ",math.pi) #math模块是一个数学运算的模块
print(random.random()) #random模块是生成随机数的
# 最后也可以安装一些 别的第三方库
# 文件与IO
print("=== 文件与IO ===")
file_name = "E:\software\PyCharm 2022.1.1\ProjectPath\examplePython\src\com\lblz\零基础Python入门到精通\day04.py"
# f = open(file_name,"UTF-8") #打开一个文件相当于 java中的new File("c"),如果无法打开则会报OSError
# txt = f.read(20)
# txt = f.readline()
# print(txt)  # 会报错 我也不知道为什么
# f.close() # 关闭流

# StringIO
strIo = StringIO()
strIo.write("hello")
strIo.write(" ")
strIo.write("world")
print(strIo.getvalue())

#bytesIO
byteIo = BytesIO()
byteIo.write("你好".encode("utf-8"))
print(byteIo.getvalue())
print(byteIo.getvalue().decode("utf-8"))

# 序列化和反序列化 pickle只支持python的序列化 不支持python的序列化
print("=== 序列化和反序列化 ===")
class Student:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
student = Student("小米",15,"男")
with open("student1.data","wb") as f:
    pickle.dump(student,f) #序列化
file = open("student1.data","rb")
data = file.read()
student1 = pickle.loads(data)
print("姓名 : ",student1.name,"年龄  : ",student1.age)
#json序列化
student2 = {
    "name": "小米",
    "age": "25",
    "gender": "男"
}
print(json.dumps(student2))
with open("student2.data","w") as f:
    json.dump(student2,f) #序列化
jsonFile = open("student2.data","r")
data1 = jsonFile.read()
student3 = json.loads(data1)
print("json反序列化",student3)
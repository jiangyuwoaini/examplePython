import random

# 这是一行注释
"""
    这是多行注释
"""
'''
   这也是多行注释
'''

# 变量定义，有规则只能有字母数组下划线,并且不能以数开头,左边是
MyNum = 1
myNumber = 2
_Number = 1
the_name = "name"
the_name1 = the_name * 2
the_name2 = the_name1[1:5] #字符串切片5,左闭右开,代表着切取下标为1 ~ 下标5之前的字符串
the_name3 = the_name1[3:] #表示下标3之后的所有
the_name4 = the_name1[1:6:1] #最后一个参数是步长,表示每次截取间隔1个
the_name5 = the_name1.replace('name','pig') #替换
arr = the_name1.split(" ") # 分割占位符，返回数组
the_name6 = "-".join(arr) # 将字符串列表拼合成一个字符串
#除了上述字符串操作外,字符串还有很多功能操作,列如转换大小写,空白剔除等
liebiao = [1,2,3] #列表
liebiao[0] = 1 # 根据索引位置更改内容,字符串不可以,因为字符串是不可变的
liebiao.append("4") # 末尾添加元素
liebiao.index(1,0)  # 指定索引添加元素
# liebiao.pop(0) # 根据下标删除元素
# liebiao.remove(2) #删除列表值的匹配的某个元素
# liebiao.clear() # 清空列表
# del liebiao # 删除列表
# liebiao.sort() # 列表排序
# liebiao = sorted(liebiao) # 列表排序
liebiao1 = [[1,2,3],[4,5,6]] #嵌套数组,可以无限嵌套
print(f"判断某个值是否在列表:{(1 in liebiao)}" )
print(f"判断某个值是否不在列表:{(1 not in liebiao)}" )
jihe = {1,2,3} # 集合
yuanzu = (1,2,3)  #元组
zidian = {'n':1,'b':2}  #字典 .keys() 返回所有key, .values()返回所有value, .items()返回元组
# del zidian['n'] 删除字典的某个key
# zidian.clear() 清空字段
print(f"字符串可以用*号,the_name * 2: {the_name1}")
print(f"字符串切片的值:{the_name2}")
#python的输出语句
print(f"1234 {zidian}") # 带有变量的输出
print("1234 "% zidian) # 带有变量的输出
a = input("请输入:") # 客户端输入值，并返回给变量(默认是字符串)
print(f"客户端输入的内容:\t{a}")

#类型转换
a1 = 15
a2 = str(a1)
a3 = float(a2)

# 生成一个随机数
a4 = random.randint(1,100)
a5 = random.uniform(1,100) # 生成带有小数的随机数
print(f"变量a4:{a4},变量a5:{a5}")

# 运算符(+ - * / **(多少次方) %(求余运算))
a6 = 1
a6 = a6 - 1
print(f"a6的值:{a6}")
a6 -= 1 #上下同理
print(f"a6的值:{a6}")

# boolean类型有3种诶行 与(and) 或(or) 非(not)
boolean = False
boolean1 = not boolean
print('boolean类型:\t',boolean,boolean1)


# 流程控制中之 条件控制语句
a7 = 11
boolean2 = (a7 % 2) == 0 # 小数为 5
if boolean2:
    print("是偶数")
else:
    print("不是偶数")
a8 = 100
if a8 < 0 or a8 > 100:
    print("分数不合格")
elif a8 == 100:
    print("合格")
# 流程控制中之 循环语句
a9 = 0
while a9 < 10:
    a9 += 1
    if a9 == 5:
        print(f"a9的值是{a9},已跳出循环")
        break #对比的还有continue 退出本次循环
str1 = "ABCDEFGHITLMNOPQRSG"
for i in str1:
    print(f"流程控制for循环值:{i}")
else:
    print("循环正常结束了！")
a10 = range(5) # range(5)表示从0到它 左闭右开的一个区间 0,1,2,3,4



# 函数
def tes(n,age =18, *args, ** kwargs):
    print(n)
    print(age)
    for i in args:
        print(i)
    print(kwargs["ns"])
    print("逻辑模拟中~~")
tes(1,196,2,3,4,5,6,ns=15)
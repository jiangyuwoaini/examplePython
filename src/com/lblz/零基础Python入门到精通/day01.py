# python运算符
print("python运算符")
print( 10 % 3 )
print( 10 > 5)
day01a = 100
day01b = 100;
day01a += 100
print(day01a)
# python逻辑运算符
print("====python逻辑运算符===")
print(True and True) #和java的&&一样
print(True or False) #和java的||一样
print(not False) #和java的! 一样
# python关键字in和is
print("====python关键字in和is====")
day01arrays = (1,2,5,7,8,10)
print(5 in day01arrays) #是否包含
print(5 not in day01arrays)
print(day01a is day01b) # 数值比较
# python表达式
print("====python表达式====")
day01c = day01d = "Hello Python"
print(day01c +"==="+day01d)
# python的三种基本数据类型 列表,元组,字符串
print("====python的三种基本数据类型 列表,元组,字符串====")
print([1,2,3,4]) #列表
print((1,2,3,4)) #元组
print("字符串") #字符串
print([1,2,3,4][0:3]) #切片操作
#也可以将列表 用+好做连接操作,*做乘法操作
# 常见的函数有len,min,max,sum,pop,remove,insert,index,reverse,count
# 列表和元组的区别,列表是可以删除修改,而元组则是不行的,相当于java中的final
# python中的字典
print("====python中的字典数据类型====")
day01e = { #有点像java的map数据集合对象,对不对？
    "we": "我们",
    "world": "世界"
}
for k,v in day01e.items():
    print(k,"=>",v)
# 列表,字典,集合推导式也是比较重要的知识点
day01f = [x for x in range(10) if x % 2 != 0]
print(day01f)
day01g = {x: x ** 2 for n in range(5)}
print(day01g)
# 流程控制 if for 等等 java中的break和countinue在这也能用
print("====流程控制 if for 等等====")
if True: # 也可以是数字表示 0是false1是true
    print("结果为真方输出")
else:
    print("结果为家方输出这个")

if day01a > 100:
    print("1")
elif day01a > 200:
    print("2")
else:
    pass #python中的pass语句是空语句 不做任何操作

# while(True):
#     print("无限循环中~")

#python中函数的概念
print("===python中函数的概念===")
def function_hello(arg1, *arg2 , arg3=18): # arg2 为可变参数
                                           # arg3是默认值,在python中默认值只能在非默认值参数后面
    # function body
    return 0; #python的返回值,可以返回多个值 这是java所不具备的
lambda x,y: x+y #python也支持lambda表达式


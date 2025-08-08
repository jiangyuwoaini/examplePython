# python中的时间
import datetime
import time

print("=== 时间 ===")
now = time.time()
print("当前时间的时间戳:",now)
# localtime函数
print("当前时间",time.localtime())
print("0时间戳对应的当前时间",time.localtime(0))
# mktime函数 可以结构化时间,也可以是9位元组元素
t = (2019,7,17,17,3,1,1,1,0)
secs = time.mktime(t)
print("time.mktime(t) : %f" % secs)
# gmtime 函数将一个时间戳转换为utc时区的struct_time，可选的参数asc表示从1970-1-1以来的秒数,gmtime函数默认值为time.time
print("time.gmtime:",time.gmtime())
#asctime 接收元组返回一个可读的时间
print("time.asctime:",time.asctime(t))
#ctime 函数能把时间戳转化为time.asctime形式,不传参数默认为time.time
print("time.ctime: ",time.ctime())
#sleep函数推迟调用线程的运行,可通过secs指秒数
#strftime函数 用于接收时间元组,并返回可读字符串表示当地时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
#strptime能够根据指定格式将一个时间字符串转换为元组
struct_time = time.strptime("Jul 17 2018 09:03:01","%b %d %Y %H:%M:%S")
print("返回的元组:",struct_time)

# datetime模块 包含了日期,时间的所有信息
print("=== datetime ===")
print(datetime.date(2022,9,26)) #date包含了 时间的年月日
print(datetime.date.today())#返回当天年月日
print(datetime.date.today().weekday())#返回当前星期数 若是星期一则返回0 以此类推
print(datetime.date.today().isoweekday()) #返回当前星期数,如果星期一则返回1 一次类推
print(datetime.date(2022,9,26).isoformat()) #函数返回日期为ISO格式,即YYYY-MM-DD
print(datetime.date(2022,9,26).strftime("%Y-%m-%d")) #输出格式化日期
print("=== datetime的time对象 ===") #表示本地时间的时分秒
print(datetime.time()) #返回当前 时分秒
print(datetime.time(hour=8,second=7)) #指定当前 时分秒
print(datetime.time.min) #最小值 时分秒
print(datetime.time.max) #最大值 时分秒
print(datetime.time(hour=8,second=7).isoformat()) #返回时间为ISO格式,既"HH:MM:SS"的字符串
print(datetime.time(hour=8,second=7).strftime("%H:%M:%S")) #strftime方法可以格式化输出时间
# datetime对象 是date和time对象的结合体,包含了date信息和time信息
print("=== datetime对象 ===")
print(datetime.datetime(year=2022,month=9,day=26,hour=16,second=10))
print(datetime.datetime.today()) #返回当前日期和时间
print(datetime.datetime.now()) #返回当前日期和时间
print(datetime.datetime.utcnow()) #返回一个当前的utc时间的datetime对象
print(datetime.datetime.fromtimestamp(time.time()-86400)) #函数根据时间戳创建一个datetime对象,可选参数tzinfo指定时区信息
print(datetime.date) #获取当前时间年月
print(datetime.time) #获取当前时间时分秒
print(datetime.datetime.combine(datetime.date(2018,7,1),datetime.time(8,15,10))) #combine 根据date 和time创建一个datetime对象
print(datetime.datetime.combine(datetime.date(2018,7,1),datetime.time(8,15,10)).strftime("%Y-%m-%d %H:%M:%S"))
dt1 = datetime.datetime(year=2022,month=9,day=26,hour=16,second=10)
dt2 = dt1 + datetime.timedelta(weeks=-2)
print(dt1 - dt2)
# tzinfo对象是一个时区对象,datetime和time对象使用它来提供可定义的时间调整概念,例如:时区或夏令时
#    -tzinfo类不能直接使用,但是可以用datetime.timezone生成,datetime.timezone实现了UTC时区的tzinfo实例
utc_now1 = datetime.datetime.now(datetime.timezone.utc)
utc_now2 = datetime.datetime.utcnow()
print(utc_now1)
print(utc_now2)
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))) # 也可以通过datetime.timedelta来实现自己想要的时区 构造对象时，只需传入和UTC时间相隔的timedelta对象即可
# calendar模块,跟日历有关的模块好消息是,有相关操作时可以百度下,大概看了一下 没练习
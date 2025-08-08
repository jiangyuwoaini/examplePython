# 多线程 多线程共有两个模块 _thread和threading
import _thread
import datetime
import multiprocessing
import os
import queue
import subprocess
import threading
import time
from multiprocessing import Process
import multiprocessing.dummy

print("=== 多线程_thread模块 ===")
# demo1 该多线程无序执行 没有加锁
date_time_format = "%H:%m:%S"
def get_time_str():
    now = datetime.datetime.now();
    return datetime.datetime.strftime(now,date_time_format)

def thread_function(thread_id):
    print("Thread %d\t start at %s" %(thread_id, get_time_str()))
    print("thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str()))

def main():
    print("Main Thread start at %s" %get_time_str())
    for i in range(5):
      _thread.start_new_thread(thread_function,(i, )) # 启动一个新的线程返回器标识符,线程使用的参数列表args必须是元组
      time.sleep(1)
    time.sleep(6) #为了让主线程 不要立马结束,如果主线程结束了 那子线程立马就停止了
    print("Main Thread  finish at %s" %get_time_str())
# main()
# demo02 为多线程加上了锁
date_time_format1 = "%H:%m:%S"
def get_time_str1():
    now = datetime.datetime.now();
    return datetime.datetime.strftime(now,date_time_format1)

def thread_function1(thread_id,lock):
    print("Thread %d\t start at %s" %(thread_id, get_time_str1()))
    print("thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str1()))
    lock.release() # 对锁进行释放

def main1():
    print("Main Thread start at %s" % get_time_str1())
    locks = []
    for i in range(5):
        lock = _thread.allocate_lock()
        lock.acquire() #获取锁
        locks.append(lock)
    for i in range(5):
        _thread.start_new_thread(thread_function1, (i,locks[i]))  # 启动一个新的线程返回器标识符,线程使用的参数列表args必须是元组
        time.sleep(1)
    for i in range(5):
        while locks[i].locked(): #如果当前锁还在锁定中 则休眠一秒钟
            time.sleep(1)
    print("Main Thread  finish at %s" % get_time_str1())
# main1()
print("=== 多线程Threading模块 ===")
# 看书上描述 该模块不仅提供了面向对象的线程实现方式,还提供了各种有用的对象和方法方便我们创建和控制线程
# demo03
date_time_format2 = "%H:%m:%S"
def get_time_str2():
    now = datetime.datetime.now();
    return datetime.datetime.strftime(now,date_time_format2)

def thread_function2(thread_id):
    print("Thread %d\t start at %s" %(thread_id, get_time_str2()))
    print("thread %d\t sleeping" % thread_id)
    time.sleep(4)
    print("Thread %d\t finish at %s" % (thread_id, get_time_str2()))

def main2(): #thread会自动帮助我们 创建锁,管理锁,获取锁,释放锁,和检查锁等步骤
    print("Main Thread start at %s" % get_time_str2())
    threads = []
    #1、创建线程
    for i in range(5):
        thread = threading.Thread(target=thread_function2, args =(i,))  # 指定参数的创建线程
        threads.append(thread)
    # 2、启动线程
    for i in range(5):
        threads[i].start()
        time.sleep(1)
    # 3、等待线程执行完毕
    for i in range(5):
        threads[i].join()
    print("Main Thread  finish at %s" % get_time_str2())
# main2()
# demo04 threading的多线程同步功能
thread_lock = None
class MyThread(threading.Thread):
    def __init__(self,thread_id):
        super(MyThread, self).__init__()
        self.thread_id = thread_id
    def run(self) -> None:
        # 锁定
        thread_lock.acquire()
        for i in range(3):
            print("Thread %d\t printing!times: %d" %(self.thread_id,i))
        #释放
        thread_lock.release()
        time.sleep(1)

        #锁定
        thread_lock.acquire()
        for i in range(3):
            print("Thread %d\t printing!times: %d" %(self.thread_id,i))
        # 释放
        thread_lock.release()
def main3():
    print("Main Thread start")
    threads = []

    #创建线程
    for i in range(5):
        thread = MyThread(i)
        threads.append(thread)

    #启动线程
    for i in range(5):
        threads[i].start()

    #等待线程执行完毕
    for i in range(5):
        threads[i].join()
    print("Main Thread end")
thread_lock = threading.Lock() #获取锁,相当于_thread.allocate_lock()
# main3()

#队列模块 先进先出
print("=== python队列 ===")
#创建工作队列 并限制队列的最大元素是10
work_queue = queue.Queue(maxsize=10)
#创建结束队列 并限制最大元素是10
result_queue = queue.Queue(maxsize=10)

class WorkerThread(threading.Thread):
    def __init__(self,thread_id):
        super(WorkerThread, self).__init__()
        self.thread_id = thread_id

    def run(self) -> None:
        while not work_queue.empty():
            #从工作队列中获取数据
            work = work_queue.get()
            # 模拟工作耗时3秒钟
            time.sleep(3)
            out = "Thread %d\t received %s" %(self.thread_id,work)
            # 把结果放入结果队列
            result_queue.put(out)

def main4():
    #工作对象放入数据
    for i in range(10):
        work_queue.put("message id %d" %i)

    #开启两个工作线程
    for i in range(2):
        thread = WorkerThread(i)
        thread.start()

    #输出10个结果
    for i in range(10):
        result = result_queue.get()
        print(result)
# main4()


# os模块
print("=== python进程中的os模块 ===")
if os.name == "nt":# 判断是否是windows
    return_code = os.system("dir")
else:
    return_code = os.system("ls")
#判断命令返回值是否是0 0代表着运行成功
if return_code == 0:
    print("Run Success!")
else:
    print("Something wrong!")
# subprocess模块
print("=== subprocess模块 ===")

if os.name == "nt":# 判断是否是windows
    return_code = subprocess.call(["cmd","/C","dir"]) #subprocess.call和os.system有一点类似
else:
    return_code = subprocess.call(["ls","-1"])

try:
    if os.name == "nt":# 判断是否是windows
        return_code = subprocess.check_call(["cmd","/C","test command"]) # subprocess.check_call 和 subprocess.call基本相似
    else:
        return_code = subprocess.check_call(["ls","test command"])
except subprocess.CalledProcessError as e:
    print("Something wrong",e)

if os.name == "nt":# 判断是否是windows
    ping = subprocess.Popen("ping -n 5 www.baidu.com",shell=True,stdout=subprocess.PIPE) #subprocess.Popen对象提供了功能更丰富的方式调用外部命令
else:
    ping = subprocess.Popen("ping -c 5 www.baidu.com",shell=True,stdout=subprocess.PIPE)
#等待命令执行完毕
ping.wait()
#打印外部命令进程id
print(ping.pid)
#打印外部命令进程id
print(ping.returncode)
#打印外部命令的输出内容
output = ping.stdout.read()
print(output)


# 根据python代码创建进程  执行会报错的 所以注释
# class MyProcess(Process):
#     def __init__(self):
#         super(MyProcess, self).__init__()
#
#     def run(self) -> None:
#         print("module name:",__name__)
#         print("parent process:",os.getppid())
#         print("process id:",os.getpid())
#
# def main5():
#     processes = []
#
#     #创建进程
#     for i in range(5):
#         processes.append(MyProcess())
#
#     #启动进程
#     for i in range(5):
#         processes[i].start()
#
#     #等待进程结束
#     for i in range(5):
#         processes[i].join()
# main5()

#进程池 执行会报错的 所以注释
def process_func(process_id):
    print("process id %d start" % process_id)
    time.sleep(3)
    print("process id %d end" % process_id)

def main6():
    pool = multiprocessing.Pool(processes=3)
    pool.map(process_func,range(10))
    for i in range(10):
        # 向进程池中添加要执行的任务
        pool.apply_async(process_func,args=(i,))
    #先调用close关闭进程池,不能再有新任务被加入到进程池中
    pool.close()
    #join函数等待所有子进程结束
    pool.join()
# main6()

# 线程池 multiprocessing下有一个dummy模块,该是操作线程池的模块
def process_func(process_id):
    print("process id %d start"% process_id)
    time.sleep(3)
    print("process ud %d end" % process_id)

def main7():
    # 虽然参数叫process但是实际创建的是线程
    pool = multiprocessing.dummy.Pool(processes=3)
    # for i in range(5):
    #     # 向进程中添加要执行的任务
    #     pool.apply_async(process_func,args=(i, ))
    pool.map(process_func,range(10)) #效果与上面类似,只不过不用自己便利了-> map方法的第一个参数是要执行的函数,第二个参数是可迭代的对象,map会帮助我们迭代第二个对象,并把迭代的参数分批传给第一个要执行的函数并执行
    pool.close()
    pool.join()
main7()
# Python 正则表达式
import base64
import hashlib
import re
print("=== Python 正则表达式 ===") #re模块是python提供的正则表达式的搜索 及匹配
pattern = re.compile(r'\d+') # 表达式 匹配至少一个数字
m1 = pattern.match("one123") #匹配
print(m1)
m2 = pattern.match("one123",3,5) # 匹配从位置3到5的字符串
print(m2)
print(m2.group())

m3 = re.match(r'\d+',"one123") #不适用compile直接匹配,只能匹配字符串 也就是第二个参数必须是字符串
print(m3)

m4 = re.match(r'[a-z]+','Abcde',re.I) # 匹配使用忽略大小写
print(m4)
print(m4.group())

# re.search函数 该函数是查询方法,用于正则查询字符串的
print("=== re.search ===")
pattern1 = re.compile(r"\d+") #至少匹配一个数字
m11 = pattern1.search("one123")
print(m11)
print(m11.group())

m22 = pattern1.search("one123",0,4)
print(m22)
print(m22.group())

m33 = re.search(r'\d',"one123")
print(m33)
print(m33.group())

m44 = re.search(r'[a-z]+','123Abcde',re.I)
print(m44)
print(m44.group())

#re.findall 其实跟search差不多,不过这个可以匹配多个符合条件的结果集
print("=== re.findall ===")
pattern2 = re.compile(r'\d{2}') #匹配至少一个数字,默认匹配整个字符串
m111 = pattern2.findall('one1234')
print(m111)

m222 = pattern2.findall('one123',0,4)
print(m222)

#re.split 用正则字符串切分字符内容
pattern3 = re.compile(r'[\s\,\;]+') #匹配空格,和;
m1111 = pattern3.split('a,b;; c       d')
print(m1111)
#re.sub 正则表达式替换字符串的方法
s = 'hello 123 world 456'
pattern4 = re.compile(r'(\w+) (\w+)')
m11111 = pattern4.sub('hello world',s) #使用hhello world 替换hello 123和world 456
print(m11111)

m22222 = pattern4.sub('hello world',s,1)#只替换一次
print(m22222)
#re的分组匹配
p2 = re.compile('(\d)-(\d)-(\d)') #分组
mp1 = p2.match('1-2-3')
print(mp1.group())
print(mp1.groups())

#re的贪婪排序和非贪婪排序
tl1 = re.match(r'.+','Are you ok? No, Iam NoT OK.') #贪婪
print(tl1.group())
tl2 = re.match(r'.+?','Are you ok? No, Iam NoT OK.') #非贪婪
print(tl2)
#宽度断言 顾名思义就是一种零宽度的匹配,他的匹配不会保存在匹配结果中,表达式匹配的内容只是代表了一个位置而已
s = r'eating apple seeing paper watching movie'
kd1 = re.findall(r'(\b\w+?)ing',s)
print(kd1)

print("=== Python 电子邮件 ===")
# Python 电子邮件 发送用的是SMTP 接收用的是POP3和IMAP协议    (观看了一下,如果有需要的时候 在写)

print("=== Python 加密 ===")
message = "姜煜 是一个能够成为自己想成为的人"
md5 = hashlib.md5(message.encode()) #md5加密方式
print("md5的加密结果:",md5.hexdigest())
sha = hashlib.sha1(message.encode()) #sha1加密,跟md5类似 也是使用散列哈希函数进行数据加密的
print("sha1的加密结果:",sha.hexdigest())
msg = base64.b64encode(message.encode())
print("base64编码后的结果是:",msg)
print("base64解密后的结果是:",base64.b64decode(msg).decode())
#des 加密aes 和rsa加密需要引用外部包Crypto所以没写
#stock tcp 和udp 只是简单看一看
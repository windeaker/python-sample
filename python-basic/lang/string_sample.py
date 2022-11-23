
varchar="字"
# 把字符转换成编码
print(ord(varchar))
# 把编码转换成字符
print(chr(23383))
# 以16进制的方式标识字符串
print('\u4e2d\u6587')

# 字符串编码
# 将字符以字节方式表示
bstr1 = b'ABC'
print(bstr1)
bstr2= "ABC".encode('ascii')
print(bstr1 == bstr2)
# x = b'中文'   不能使用ASCII表示 需要写成 b'\xe4\xb8\xad\xe6\x96\x87'
bstr2= "中文".encode('utf-8')
print(bstr2)

# 字符串解码
bstr1= b'ABC'.decode('ascii')
bstr2= b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(bstr1)
print(bstr2)
# 忽略错误字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# print(b'\xe4\xb8\xad\xff'.decode('utf-8')) 会报错


varstr1="aaaa"
varstr2="bbbb"
varstr3=varstr1+varstr2
print(varstr3)

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 格式化整数
print('%2d-%02d' % (3, 1))

print('16进制整数:%x' % 3)

# 小数点保留两位
print('%.2f' % 3.1415926)

# 百分号转义
print('growth rate: %d %%' % 7)

# format 函数使用{0}、{1}、{2}的方式格式化
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

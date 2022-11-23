# -*- coding: utf-8 -*-
# 整数
# 一般整数
intvar1 = 1
# 是否分隔符的整数
intvar2 = 10_000_000
# 16进制的整数
intvar3 = 0xff00

print(intvar1)
print(intvar2)
print(intvar3)

#   浮点数 python浮点数依然会有精度问题
# 一般浮点数
decvar1 = 1.2
# 科学计数法浮点数 1.23*10^1
decvar2 = 1.23e1
# 科学计数法浮点数  1.23*10^-1
decvar3 = 1.23e-1

print(decvar1)
print(decvar2)
print(decvar3)

# 字符串
# ""和''完全等价，互相可以相互包含，也可以是用\ 转义
strvar1 = 'abc'
strvar2 = "abc"
print(strvar2 == strvar1)
# ""和''互相可以相互包含，也可以是用\ 转义
strvar3 = "'abc'"
strvar4 = '"abc"'
strvar5 = 'a"b\"\'c'

print(strvar3)
print(strvar4)
print(strvar5)
# 使用r'' 标识内部的字符串不转义
strvar6 = r'a"b\"\'c'
print(strvar6)
# 使用'''*''' 支持换行字符串
strvar7 = '''第一行
第二行
  第三行
'''
print(strvar7)

strvar8 = '''第一行\n
第二行
  第三行
'''
print(strvar8)
# r'''*'''依然不转义
strvar9 = r'''第一行\n
第二行
  第三行
'''
print(strvar9)

# 布尔值

boolvar1 = True;
boolvar2 = False;

print(boolvar1 and boolvar2)
print(boolvar1 and not boolvar2)
print(boolvar1 or boolvar2)
print(not boolvar1 or boolvar2)

# 空值

nullvar = None
print(nullvar)

# 常量
# python 中压根没有常量，只不过，通常情况下，使用全部大写的变量名标识常量，你别去改就行了
PI = 3.1415926
print(PI)
PI = 3.1415927
print(PI)

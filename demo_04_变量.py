# 不需要定义数据类型
qq_number = "1234567"
qq_pwd = "1234567"
print(qq_number)
print(qq_pwd)

name = "小明"
age = 18
height = 173.5
gender = True

"""type()函数 查看数据类型"""
print(type(name))
print(type(age))
print(type(height))
print(type(gender))

"""python3.x中 已经没有long型了 都是int型"""
print(type(2 ** 32))
print(type(2 ** 128))

"""数字型变量之间可以直接计算"""
# bool型: true=1  false=0
i=10
f=10.5
b=True
print(i+f+b)  # 21.5

"""字符串变量的计算"""
first_name = "三"
last_name = "张"
print((first_name+last_name) * 10)

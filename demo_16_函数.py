"""
def 函数名(参数列表):
    函数体
"""


def area(width, height):
    return height * width


print(area(3, 5))


# 传不可变对象实例
def f1(a):
    a = 10


b = 5
f1(b)
print(b)


# 默认参数 参数有默认值
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
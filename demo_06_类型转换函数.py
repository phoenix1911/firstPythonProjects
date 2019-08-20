
"""类型转换函数 不可以把int型使用float()函数强转为整数"""
a = input("请输入整数:")
print(a)
print(type(a))
print(type(int(a)))


a = input("请输入浮点数字:")
print(a)
print(type(a))
print(type(float(a)))
"""
迭代器 从集合第一个元素开始访问 只往前 不往后
"""
import sys

'''iter() next()函数'''
list = [1, 2, 3, 4]
it = iter(list)
print(it)
print(next(it))
print(next(it))

'''使用for 循环迭代 迭代器对象'''
list2 = [1, 2, 3, 4]
it2 = iter(list2)
s = ""
for i in it2:
    s += i.__str__() + ","

print(s[0:len(s) - 1])

'''使用while 遍历迭代器'''
list3 = [1, 2, 3, 4]
it3 = iter(list3)
bool = 1;
while bool:
    try:
        print(next(it3))
    except StopIteration:
        print("退出")
        bool = 0;

"""
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
"""


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)

while True:
    try:
        print(next(f), end="_")
    except StopIteration:
        sys.exit()

"""
字典是可变容器模型
key:value ,
同一个键不允许出现两次
"""
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict)

print("\n"+"访问"+"-"*100)
print(dict['Alice'])
print(dict["Beth"])

print("\n"+"修改"+"-"*100)
dict["Alice"] = 1000
print(dict["Alice"])

print("\n"+"删除"+"-"*100)
del dict["Cecil"]
print(dict)
dict.clear()
print(dict)
del dict
print(dict)
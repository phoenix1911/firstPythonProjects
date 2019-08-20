"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号
列表使用方括号
"""
tup1 = ("google", "baidu", 1, 2)

'''访问元组'''
print(tup1)
print(tup1[0])
print(tup1[1:4])  # [a:b] 左开右闭原则 a<=x<b

'''修改元组,元组不允许修改 但可以连接组合'''
tupa = ("a", "b", "c")
tupb = ("1", "2", "3")
tupc = tupa+tupb
print(tupc)

'''不允许删除元素 但可以删除整个元组'''
tup0 = ("a","b","c")
print(tup0)
del tup0
print(tup0)
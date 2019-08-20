"""
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号
列表使用方括号
"""
list1 = ["google", "baidu", 1, 2]

'''访问列表'''
print(list1)
print(list1[0])
print(list1[1:4])  # [a:b] 左开右闭原则 a<=x<b

print("-" * 100)
'''修改列表,列表不允许修改 但可以连接组合'''
lista = ["a", "b", "c"]
lista[1] = 10
print(lista)

print("-" * 100)
'''不允许删除元素 但可以删除整个列表'''
list0 = ["a", "b", "c"]
print(list0)
del list0[1]
print(list0)

print("-" * 100)
'''脚本操作符'''
print(len(list0))
print(list0 * 4)
print("a" in list0)
for x in list0: print(x, end=" ")
print("")

print("-" * 100 + "\n" + "截取与拼接")
list2 = ["1", "2", "3", "4", "5"]
print(list2[1])  # 第二个元素
print(list2[-1])  # 倒数第一个元素
print(list2[1:])  # 第二个元素之后的元素

print("-" * 100 + "\n" + "嵌套列表")
a = ["a", "b", "c"]
b = ["1", "2", "3"]
c = [a, b]
print(c)
print(c[0][1])

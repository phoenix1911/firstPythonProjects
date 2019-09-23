"""
集合（set）是一个无序的不重复元素序列。
使用{} 或者set()  创建一个空集合必须用set() 而不是{ } {}是用来创建空字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print("\n" + "添加元素" + "-" * 100)
basket.add("a")
print(basket)
'''也可以使用update(x) 参数可以是列表,元组,字典'''
basket.update({1, 3})
print(basket)

print("\n" + "移除元素: remove(x) 如果x不存在 报错, discard(x)如果x不存在 不报错 " + "-" * 100)
basket.remove(1)
basket.discard("orange")
print(basket)

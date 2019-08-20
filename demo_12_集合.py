"""
集合（set）是一个无序的不重复元素序列。
使用{} 或者set()  创建一个空集合必须用set() 而不是{ } {}是用来创建空字典
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

print("\n"+"添加元素"+"-"*100)
basket.add("a")
print(basket)


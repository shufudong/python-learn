cars = ['bmw', 'audi', 'toyota', 'subaru']

# 使用方法sort() 对列表进行永久性排序
cars.sort()
print(cars)

# 使用方法sort(reverse=True) 对列表进行永久性倒叙排序
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

# 使用函数sorted() 对列表进行临时排序
print(sorted(cars))

# 使用函数sorted() 对列表进行临时倒叙排序
print(sorted(cars, reverse=True))

# 永久性反转列表
cars.reverse()
print(cars)

# 确定列表的长度
print(len(cars))

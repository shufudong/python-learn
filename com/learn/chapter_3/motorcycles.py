motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 根据数组下标获取元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 追加元素
motorcycles.append('Harley-Davidson')
print(motorcycles)

# 插入元素
motorcycles.insert(1, 'awasaki')
print(motorcycles)

# 根据数组下标删除元素
del motorcycles[0]
print(motorcycles)

# 用pop()方法删除元素
popped_motorcycles = motorcycles.pop(0)
print(popped_motorcycles)
print(motorcycles)

# 用pop(int x)方法删除元素
popped_motorcycles = motorcycles.pop(1)
print(popped_motorcycles)
print(motorcycles)

# 根据值删除元素
motorcycles.remove('yamaha')
print(motorcycles)

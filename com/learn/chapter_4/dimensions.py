# 元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

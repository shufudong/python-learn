# 打印1-10的平方
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)

# 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('the list digits min is ' + str(min(digits)))
print('the list digits max is ' + str(max(digits)))
print('the list digits sum is ' + str(sum(digits)))

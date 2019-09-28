# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# 你可以生成列表的任何子集，例如，如果你要提取列表的第2~4个元素，可将起始索引指定为1，并将终止索引指定为4：
print(players[1:4])

# 如果你没有指定第一个索引，Python将自动从列表开头开始：
print(players[:4])

# 要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第3个元素到列表末尾的所有元素，可将起始索引指定为2，并省略终止索引：
print(players[2:])

# 如果你要输出名单上的最后三名队员，可使用切片players[-3:]：
print(players[-3:])

# 遍历切片
for player in players[:3]:
    print(player.title())

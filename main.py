numbers = [     [10, 11, 12, 13, 14],
               [20, 21, 22, 23, 24],
               [30, 31, 32, 33, 34]]

cnum = len(numbers[0])

for i in range(cnum):
    print(numbers[0][i] + numbers[1][i] + numbers[2][i])
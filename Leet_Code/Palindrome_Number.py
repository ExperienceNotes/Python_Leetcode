number = input('請輸入一個數字:')
if len(number) == 1:
    flag = 1
for i in range(len(number)//2):
    flag = 0
    if number[i] == number[-i-1]:
        flag = 1
        pass
    else:
        flag = 0
        break
if flag == 1:
    print('{}是迴文'.format(number))
else:
    print('{}是不迴文'.format(number))
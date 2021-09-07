list_d = [1,2,4]

for i in range(len(list_d)-1,-1,-1):
    if list_d[i] == 9:
        list_d[i] = 0
    else:
        list_d[i] += 1
        print('true_ans:',list_d)
        break
any_ans = [1]+list_d
print('if ALL 999999 have this ans:',any_ans)
ans = [1] * 10
ans[0] = ans[1] = 0
for i in range(2,int(10**0.5)+1):
    if ans[i] == 1:
        for j in range(i+i,10,i):
            ans[j] = 0
print(sum(ans))
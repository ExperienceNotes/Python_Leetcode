list_price = [7,1,5,3,6,4]
ans = 0
for i in range(len(list_price)-1):
    if list_price[i] < list_price[i+1]:
       ans += list_price[i+1] - list_price[i]
print('best_prices:',ans)
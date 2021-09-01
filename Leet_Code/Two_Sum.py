import numpy as np
np_array = np.array([2, 7, 11, 15])
target = eval(input('請輸入目標總和:'))
for i in range(len(np_array)):
    right_array = np_array[i+1:]
    for j in range(len(right_array)):
        if np_array[i]+right_array[j] == target:
            print(i,i+j+1)
#-------------------------------------------------------------------
k = 0
for i in np_array:
    k+=1
    if target - i in np_array[k:]:
        print(k - 1, list(np_array[k:]).index(target - i)+k)
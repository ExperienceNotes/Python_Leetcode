s = "Let's take LeetCode contest"
s = s.split(" ")
ans = []
for i in s:
    re_i = i[::-1]
    ans.append(re_i)
print(" ".join(ans))
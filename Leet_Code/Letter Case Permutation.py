s = "a1b2"
list_ans = []
list_ans.append(s)
for i in range(len(s)):
    if s[i].isalpha():
        for j in range(len(list_ans)):
            chars = list(list_ans[j])
            chars[i] = chars[i].swapcase()
            list_ans.append("".join(chars))
print(list_ans)
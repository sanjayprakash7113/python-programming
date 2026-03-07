s = "({[]})"

stack = []
p={")":"(","}":"{","]":"["}
for i in s:
    if i in "({[":
        stack.append(i)
    else:
        if not stack or stack[-1]!=p[i]:
            print(False)
            break
        stack.pop()
print(len(stack)==0)

arr = input()
digit = 0
result = []
for x in arr:
    if x.isalpha():
        result.append(x)
    else:
        digit += int(x)

result.sort()
result.append(str(digit))

print(''.join(result))

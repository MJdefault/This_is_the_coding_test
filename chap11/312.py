str_arr = list(map(int, input().split))
ans = 0

for i in str_arr:
    if str_arr[i] == 0 or str_arr[i] == 1:
        ans += str_arr[i]
    else:
        ans *= str_arr[i]

print(ans)

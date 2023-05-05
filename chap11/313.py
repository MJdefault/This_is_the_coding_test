binary_arr = list(map(int, input().split()))

m = binary_arr[0] # 문자열 초기값 확인
result = 0

for i in binary_arr:
    if i != m:
        m =i
        result += 1

if result % 2 == 0:
    print(result//2)
else:
    print((result//2) + 1)

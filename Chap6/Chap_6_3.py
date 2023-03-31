n, m = map(int, input().split())
arr = list(map(int, input().split()))

mid = (max(arr)+min(arr))//2
remain = 0
while True:
    for i in range(n):
        remain += arr[i]-mid
        print(remain, mid)
    if remain == m:
        break
    else:
        mid += 1

print(mid)

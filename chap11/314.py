n = int(input())

data = list(map(int, input().split()))
data.sort()
a = 1 # 최소값 default

for i in data:
    if a < i:
        break
    a += i
print(a)

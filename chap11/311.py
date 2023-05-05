n = int(input())

fear_score = list(map(int, input().split()))
fear_score.sort()
result = 0
count = 0 #그룹별 사람 수

for i in fear_score:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)

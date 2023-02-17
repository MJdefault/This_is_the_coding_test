#숫자 카드 게임
# n = list 행 // m = list 열
# 1. sort 하여 data[0] <= 이 부분이 최소값에 해당
# 2. list 행 비교하여 최소값 중 최대값을 산출

n, m  = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  
  min_value = min(data)
  result = max(result, min_value)
  
print(result)

n = int(input())

schedule = list(input().split()) # 행렬로 '알파벳' 저장

x,y = 1, 1 # 현재 위치 지정

for i in range(n+1): # 행렬끝까지 이동하며 해당 항목에 적합한 동작을 수행
    if schedule[i] == "L":
        y-=1
        if y==0 or y>n: #맵 크기를 벗어날 때 이전 위치로 귀환
            y+=1
        else:
            pass

    if schedule[i] == "R":
        y+=1
        if y==0 or y>n: #맵 크기를 벗어날 때 이전 위치로 귀환
            y-=1
        else:
            pass

    if schedule[i] == "U":
        x-=1
        if x==0 or x>n: #맵 크기를 벗어날 때 이전 위치로 귀환
            x+=1
        else:
            pass

    if schedule[i] == "D":
        x+=1
        if x==0 or x>n: #맵 크기를 벗어날 때 이전 위치로 귀환
            x-=1
        else:
            pass
print(x,y) # 일정대로 움직인 후에 업데이트 된 현재 위치 프린트 출력


N, M = map(int, input().split())
x,y,d = map(int, input().split())
hist_list = []

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

def move_forward(x,y,d): 
    if d == 0: # 현 방향 북쪽으로 왼쪽 이동 조건 시, 서쪽으로 이동: y축 -1 이동
        y = y-1
    if d == 3: # 현 방향 서쪽으로 왼쪽 이동 조건 시, 남쪽으로 이동: x축 +1 이동
        x = x+1
    if d == 2: # 현 방향 남쪽으로 왼쪽 이동 조건 시, 동쪽으로 이동: y축 +1 이동
        y = y+1
    if d == 1: # 현 방향 동쪽으로 왼쪽 이동 조건 시, 북쪽으로 이동: x축 -1 이동
        x = x-1
    return x,y,d
        
def move_backward(x,y,d):
    if d == 0: # 현 방향 북쪽으로 뒤로 이동 조건 시, 남쪽으로 이동: x축 +1 이동
        x = x+1
    if d == 3: # 현 방향 서쪽으로 왼쪽 이동 조건 시, 동쪽으로 이동: y축 +1 이동
        y = y+1
    if d == 2: # 현 방향 남쪽으로 왼쪽 이동 조건 시, 북쪽으로 이동: x축 -1 이동
        x = x-1
    if d == 1: # 현 방향 동쪽으로 왼쪽 이동 조건 시, 서쪽으로 이동: y축 -1 이동
        y = y-1
    return x,y,d

def turn_left(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

def predict(x,y,d):
    x,y,d = move_forward(x,y,d)
    d = turn_left(d)
    if array[x][y] != 1 and (x,y) not in hist_list:
        return True
    else:
        return False

while True:
    if (x,y) not in hist_list:
        hist_list.append((x,y))

    if predict(x,y,d) == True:
        x,y,d=move_forward(x,y,d)
        d = turn_left(d)

    if predict(x,y,d) == False:
        d = turn_left(d)
        predict(x,y,d)

    if predict(x,y,d) == False and (x,y) in hist_list:
        x,y,d = move_backward(x,y,d)

        if array[x][y] == 1:
            break

print("FINAL",hist_list)
print("FINAL",len(hist_list))


#5 5
#1 1 0 
#1 1 1 1 1
#1 0 0 0 1
#1 1 1 0 1
#1 1 1 0 1
#1 1 1 1 1
#답 : 5

#5 5
#1 2 1 
#1 1 1 1 1
#1 0 0 1 1
#1 0 0 1 1
#1 0 0 1 1
#1 1 1 1 1
#답 : 6

#5 5
#1 3 3 
#1 1 1 1 1
#1 0 0 0 1
#1 0 0 0 1
#1 0 1 0 1
#1 1 1 1 1
#답 : 7

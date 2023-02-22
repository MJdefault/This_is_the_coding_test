current = input()
y = int(current[1])
x = ord(current[0])
cnt = 0

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,2,2,-2,-2]

nx = x
ny = y

while 1 <= ny and ny <= 8 and nx >= ord('a') and nx <= ord('h'):
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        print(chr(nx), ny)
        if 1 <= ny and ny <= 8 and nx >= ord('a') and nx <= ord('h'):
            cnt += 1
    
print(cnt)

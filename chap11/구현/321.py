n = str(input())
arr = []
front, back = 0, 0
arr = list(n)

for i in range(len(arr)//2):
    front += int(arr[i])
for i in range(len(arr)//2,len(arr)):
    back += int(arr[i])
if front == back:
    print("LUCKY")
else:
    print("READY")

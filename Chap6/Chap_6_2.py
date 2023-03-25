def search_binary(arr, target, start, end):
    while start <= end:

        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            end = mid - 1
        elif arr[mid] > target:
            start = mid + 1
    return None


n = input().split()
component = list(map(int, input().split()))

m = input().split()
find = list(map(int, input().split()))
for i in range(len(find)):
    target = find[i]
    search_binary(component, target, i, len(find))
    print("yes")
else:
    print("no")

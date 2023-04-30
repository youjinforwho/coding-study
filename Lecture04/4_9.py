N = int(input())
arr = list(map(int, input().split()))
arr_up = []

if arr[0] < arr[-1]:
    arr_up.append(arr[0])
    arr.pop(0)
else:
    arr_up.append(arr[-1])
    arr.pop()
print(arr)
while arr:
    if arr[0] < arr_up[-1] and arr[-1] < arr_up[-1]:
        break
    elif arr[0] < arr[-1]:
        arr_up.append(arr[0])
        arr.pop(0)
    elif arr[-1] < arr[0]:
        arr_up.append(arr[-1])
        arr.pop()
print(arr_up)
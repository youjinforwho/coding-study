def solution(sequence, k):
    answer = []
    sum_arr = []
    total = 0
    for i in range(len(sequence)):
        total += sequence[i]
        sum_arr.append(total)
    for i in range(len(sequence)):
        j = i
        while (j < len(sequence)):
            if j == i and sum_arr[j] == k:
                return [0, j]
            elif sum_arr[j] - sum_arr[j - i] == k:
                return [j - i + 1, j]
            j += 1

print(solution([1, 2, 3, 4, 5], 7))
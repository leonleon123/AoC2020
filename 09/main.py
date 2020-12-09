def sum_to_n(arr, t, n):
    if n == 2:
        i, j = 0, len(arr)-1
        while i <= j and arr[i] + arr[j] != t:
            i += arr[i] + arr[j] < t
            j -= arr[i] + arr[j] > t
        return arr[i], arr[j]
    else:
        for c in arr:
            tmp = sum_to_n(arr, t - c, n-1)
            if sum(tmp) + c == t: return (*tmp, c)

with open("input.txt") as file:
    d = list(map(int, file.readlines()))
    ind = [1 if sum(sum_to_n(sorted(d[i:i+25]), d[i+25], 2)) == d[i+25] else 0 for i in range(0, len(d)-25)].index(0) + 25
    print(d[ind])
    print(*[min(d[i:j])+max(d[i:j]) for i in range(ind) for j in range(i+1, ind) if sum(d[i:j]) == d[ind]])

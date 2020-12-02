from math import prod


def sum_to_n(arr, year, n):
    if n == 2:
        i, j = 0, len(arr)-1
        while i <= j and arr[i] + arr[j] != year:
            i += arr[i] + arr[j] < year
            j -= arr[i] + arr[j] > year
        return arr[i], arr[j]
    else:
        for c in arr:
            tmp = sum_to_n(arr, year - c, n-1)
            if sum(tmp) + c == year: return (*tmp, c)

with open("input.txt") as file:
    nums = sorted(map(int, file.readlines()))
    print(*[prod(sum_to_n(nums, 2020, i)) for i in [2,3]], sep='\n')

import random

# 배열을 추가로 사용하지 않고 내부에서 기준에 맞춰 자리를 교환하며 퀵정렬 실행
cycle = 0
def sorting(arr, start, end):
    if end <= start:
        return
    global cycle

    low = start
    high = end
    pivot = (low+high) // 2
    while low <= high:
        while arr[low] < arr[pivot]:
            low += 1
        while arr[high] > arr[pivot]:
            high -= 1

        if low <= high:
            cycle += 1
            arr[low],arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    pivot = low
    sorting(arr, start, pivot-1)
    sorting(arr, pivot, end)
    return arr
def quick_sort2(arr):
    res = sorting(arr, 0, len(arr)-1)
    return res

if __name__ == '__main__':
    sample = [188,162,168,120,50,150,177,105] #random.sample(list(range(0, 201)), 20)
    print(sample)
    print(quick_sort2(sample),'\n{}회 반복실행'.format(cycle))



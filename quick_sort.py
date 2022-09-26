import random

# pivot을 중심으로 왼쪽은 기준보다 작은 값, 오른쪽 기준보다 큰 값으로 분류하는 작업을 재귀적으로 반복 후, 정렬된 결과물을 다시 합쳐 전체적으로 정렬하는 방식
cycle = 0
def quick_sort(arr):
    l = len(arr)
    global cycle

    if l <= 1:
        return arr

    pivot = arr[l // 2]
    small,same, big = [], [], []
    cycle +=1
    for item in arr:
        if item < pivot:
            small.append(item)
        elif item > pivot:
            big.append(item)
        else:
            same.append(item)

    left = quick_sort(small)
    right = quick_sort(big)

    res = left + same + right
    return res


if __name__ == '__main__':
    sample = random.sample(list(range(0, 201)), 20)
    print(sample)
    print(quick_sort(sample),'\n{}회 반복실행'.format(cycle))
    cycle = 0
    sample2 = [188, 50, 162, 120, 120, 168, 120, 50, 150, 177, 105, 168, 170, 120]
    print(sample2)
    print(quick_sort(sample2), '\n{}회 반복실행'.format(cycle))
#처음부터 차례대로 최솟값을 찾아 맨 앞으로 옮기는 방식
def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] <= arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx], arr[i]

    return arr

if __name__ == '__main__':
    sample = [188,162,168,120,50,150,177,105]
    print(sample)
    print(selection_sort(sample))


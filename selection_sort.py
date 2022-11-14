#현재 배열에서 최솟값을 찾아 가장 앞부분 값과 교환하는 동작을 배열의 길이를 줄여가며 반복하여 정렬하는 방식
def selection_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)-1):
        max_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i],arr[max_idx] = arr[max_idx], arr[i]

    return arr

if __name__ == '__main__':
    sample = [188,162,168,120,50,150,177,105]
    print(sample)
    print(selection_sort(sample))


# 정렬된 앞 부분에 대해 바로 앞부분과 현재 값을 반복 비교하며 알맞은 위치에 삽입하는 방식
def insert_sort(arr):
    l = len(arr)
    if l <= 1 :
        return arr

    for i in range(1,l):
        for j in range(i,0,-1):
            if arr[j-1] >= arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
            else:
                break

    return arr

if __name__ == '__main__':
    sample = [188,162,168,120,50,150,177,105]
    print(sample)
    print(insert_sort(sample))


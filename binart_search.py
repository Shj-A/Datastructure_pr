#이미 정렬된 데이터에만 적용 가능하며, 데이터를 반으로 나눠가며 착으려는 데이터가 속한 군만 다시 탐색하는 방식

def binary_search(arr,data):
    arr.sort()
    start = 0
    end = len(arr) -1
    pos = -1

    while start <= end:
        mid = (start+end)//2
        if data==arr[mid]:
            return mid
        elif data < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return pos


if __name__ == '__main__':
    sample = [168,162,120,50,150,188]
    data = 168
    res = binary_search(sample, data)
    if  res == -1 :
        print("No data")
    else:
        print("{} in index {}".format(data, res))







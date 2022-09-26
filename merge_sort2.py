#인덱스를 이용하여 분할된 배열을 표시하여 배열 사용을 최소화한 merge_sort 수행하기
def merge_sort2(arr):
    def sort(low, high):
        if high - low < 2:
            return

        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)

        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])

                print(temp)
                l += 1
            else:
                temp.append(arr[h])
                print(temp)
                h += 1

        while l < mid:
            temp.append(arr[l])
            print(temp)
            l += 1
        while h < high:
            temp.append(arr[h])
            print(temp)
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
            print(arr)
        return arr



    return sort(0, len(arr))

if __name__ == '__main__':
    sample = [188,162,168,120,50,150]
    print(sample)
    print(merge_sort2(sample))
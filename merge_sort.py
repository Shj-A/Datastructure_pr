#배열의 길이가 1이 될때까지 반으로 나눈 후 크기 순으로 정렬하며 합치는 방식
def merge_sort(arr):
    l = len(arr)
    if l< 2:
        return arr

    pivot = l//2
    # 재귀문을 이용해 연속적으로 나눈다
    low_arr = merge_sort(arr[:pivot])
    high_arr = merge_sort(arr[pivot:])

    l_idx,h_idx = 0,0
    merged = []
    #재귀문을 끝내고 돌아온 배열을 다시 합친다
    while (l_idx<len(low_arr)) and (h_idx<len(high_arr)):
        if low_arr[l_idx] < high_arr[h_idx]:
            merged.append(low_arr[l_idx])
            l_idx+=1
        else:
            merged.append(high_arr[h_idx])
            h_idx += 1

    #위 반복문에서 다 합쳐지지 못하고 남은 부분 병합
    if l_idx<len(low_arr):
        merged += low_arr[l_idx:]
    elif h_idx<len(high_arr):
        merged += high_arr[h_idx:]
    #합친 배열을 이전 step으로 반환한다
    return merged

if __name__ == '__main__':
    sample = [188,162,168,120,50,150,177,105]
    print(sample)
    print(merge_sort(sample))

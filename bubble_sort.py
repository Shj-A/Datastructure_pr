import random

# 배열의 각 요소를 바로 뒤의 요소와 반복 비교하며 가장 큰 요소를 맨 뒤로 보내는 동작을 반복하여 정렬하는 방식
# 매 반복마다 가장 상위의 값이 맨 뒤에 위치하므로 배열의 길이를 하나씩 줄이며 반복한다
# 중간에 한번도 바뀌지 않았다면 이미 정렬이 완료되었다는 뜻으로 중간에 정렬을 멈출 수 있다.
def bubble_sort(arr):
    l = len(arr)
    if l <= 1:
        return arr
    cycle = 0
    for i in range(l-1,0,-1):
        cond = False
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                cycle += 1
                cond = True
        if cond == False:
            break
    print("{}번 반복됨".format(cycle))
    return arr

if __name__ == '__main__':
    sample = random.sample(list(range(0,201)), 10)
    print(sample)
    print(bubble_sort(sample))
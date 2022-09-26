#heap sort의 특징 : root node는 자식 노드의 값보다 크거나 같으며(Max heap의 경우, Min heap은 반대) 완전 이진 트리의 구성을 가지고 있다.

def heapify(unsorted, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and unsorted[left] > unsorted[largest]:
        largest = left

    if right < heap_size and unsorted[right] > unsorted[largest]:
        largest = right

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(arr):
    l = len(arr)

    for i in range(l//2 - 1, -1, -1): #마지막 레벨 자식 노드의 부모 노드 부터 탐색 시작 , max heap 구성
        heapify(arr,i,l)
    print("max heap :",arr)
    for i in range(l - 1, 0, -1):# heap 정렬 결과 중 가장 큰 값을 뒤로 보내는 작업
        arr[0], arr[i] = arr[i], arr[0]
        print(arr)
        heapify(arr, 0, i)
        print(arr)


    return arr

if __name__ == '__main__':
    sample = [168,162,120,50,150,188]
    print(sample)
    print(heap_sort(sample))


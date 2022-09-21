import random

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
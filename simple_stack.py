SIZE = 5

stack = [None for _ in range(SIZE)]
top = -1


def push(data):
    global SIZE, stack, top

    if top >= (SIZE - 1):
        print("Any more space in stack")
        return
    else:
        top += 1
        stack[top] = data


def pop():
    global SIZE, stack, top
    if top <= -1 :
        print("Any data in stack")
        return None
    else:
        pop_data = stack[top]
        stack[top] = None
        top -= 1
        return pop_data


def peek():
    global SIZE, stack, top
    if top <= -1 :
        print("Any data in stack")
        return None
    else:
        top_data = stack[top]
        return top_data


for i in range(6):
    data = str(i) + "!"
    push(data)
    print(stack)
print('\n')
for i in range(6):
    print(pop())
    print(stack)

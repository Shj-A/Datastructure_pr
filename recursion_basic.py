# 1.재귀의 기초동작
def open_box(count):
    print(count,': 상자를 엽니다')
    count -= 1
    if count == 0:
        print(count,": 물건을 넣고 닫습니다")
        return
    open_box(count)
    print(count,": 상자를 닫습니다")
    #동작이 끝나면 이전 스텝의 재귀문 줄로 돌아감

#두 수 사이 모든 숫자 합 재귀 함수로 구현
def add_num(num1,num2):
    if num1<=num2:
        start = num1
        end = num2
    else:
        start = num2
        end = num1

    if start == end:
        return start
    return start + add_num(start+1, end)

#factorial 재귀함수 구현
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

#재귀로 pow 구현
def pow_re(base,exp):
    if exp == 0:
        return 1
    return base * pow_re(base,exp-1)

#피보나치 수열 구현
def fibo(step):
    if step == 1:
        return 0
    elif step == 2:
        return 1

    return fibo(step-2)+fibo(step-1)

#회문 판단하기
def Palindrome(sentence):
    sentence = sentence.lower().replace(' ','')
    if len(sentence) <= 1:
        print('회문')
        return
    if sentence[0] == sentence[-1]:
        return Palindrome(sentence[1:-1])
    else:
        print("회문아님")
        return False

if __name__ == '__main__':
    # 1 : open_box(5)

    # 2
    # res = add_num(2,3)
    # print(res)

    # 3 : print(pow_re(3,5))

    # 4 : print(fibo(10))
    Palindrome('주유소의 소유주')

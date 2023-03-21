### 재귀 (Recursion)
#자신을 정의할때, 자기 자신을 재참조하는 것 <br>
# 재귀의 시간복잡도 = 재귀 함수 호출 수 x (재귀 함수 하나당) 시간복잡도

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

#팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
# 시간 복잡도 = 호출 수 n * O(1) = O(n*1)
#피보나치
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)
# 시간 복잡도 = 호출 수 2^n * O(1) = O(2^n * 1)
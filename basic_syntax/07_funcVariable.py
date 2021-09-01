# 함수에 변수를 담아 사용하기
def print_something(a):
    print(a)
    
p = print_something
p(123)

p('abcd')

# 함수를 변수처럼 사용하여 순서열이나 딕셔너리도 테스트

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

flist = [plus, minus] #plus() 함수와 minus()함수를 리스트 요소로 대입
print(flist[0](1,2)) # flist[0]은 plus() 함수를 담고 있다. 따라서 plus()함수가 호출
print(flist[1](1,2)) # flist[1]은 minus()


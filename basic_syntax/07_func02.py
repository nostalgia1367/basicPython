# 함수안에 여러개의 리턴문을 배치
 
def my_abs(arg):
    if arg < 0:
        return arg * -1
    elif arg > 0:
        return arg
 
result = my_abs(-1)
 
print(result)
print(type(result))
 
 
# return문에서 아무 결과도 받지 못했기 때문에 None을 반환하게 된다.
# 즉, 아무 값도 return 받지 못했기 때문에 값이 NoneType을 반환하게된다.
result = my_abs(0)
print(result)
print(type(result))
 
 
def ogamdo(num):
    for i in range(1, num+1):
        print('제 {0}의 이해'.format(i))
        if i == 5:
            return
 
# 더이상 반환할 데이터가 없는 return문은 '함수의 종료' 를 뜻한다.
ogamdo(10)
 
 
# return문을 굳이 쓸 필요가 없이 생략할 수도 있다.
def print_something(*args):
    for i in args:
        print(i)
 
 
print_something(1,2,3,4,5)
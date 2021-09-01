
for i in range(10):
    if i % 2 == 1:
        continue
    
    print(i)
    
print()
print()


i = 0
while(True):
    i = i+1
    if i == 50:
        print('i가 {0}이 됐습니다. 반복문을 중단합니다'.format(i))
        break
    
    print(i)
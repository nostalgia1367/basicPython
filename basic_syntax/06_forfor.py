
for i in range(1,6):
    for j in range(i):
        print("*", end="")
        
    print()
    


dic = {
        '네이버' : 'www.naver.com',
        '네이트' : 'www.nate.com',
        '다음' : 'www.daum.net'
       }

for k, v in dic.items():
    print("{0} : {1}".format(k , v))
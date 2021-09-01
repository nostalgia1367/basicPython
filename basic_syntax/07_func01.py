from _ast import arg
def hello():
    print('Hello World');
    
    
hello()


def my_abs( arg ):
    if( arg < 0):
        result = arg * -1
    else:
        result = arg
        
    
    #return print(result)
    return result

#my_abs(-100)
print(my_abs(-100))
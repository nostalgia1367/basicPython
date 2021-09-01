'''
Created on 2017. 7. 3.

@author: blue
'''
class HasPrivate:
    def __init__(self):
        self.public = "Public."
        self.__private = "Private."
    
    def print_frm_internal(self):
        print(self.public)
        print(self.__private)
        

obj = HasPrivate()
obj.print_frm_internal()

print(obj.public)

print(obj.__private)
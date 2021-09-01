class ClassVar:
    text_list = []

    def add(self, text):
        self.text_list.__add__(text)
    
    def print_list(self):
        print(self.text_list)
        print(type(self.text_list))

if __name__ == '__main__':        
    a = ClassVar()
    a.add('a')
    a.print_list() # ['a'] 출력을 기대
    
    b = ClassVar()
    b.add('b')
    b.print_list() # ['b'] 출력을 기대

    

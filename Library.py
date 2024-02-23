class library :
    no_book=5
    book=["maths,physics,c++,python,chemistry"]
    
    def add(self,a):
       
        print(f"name of the book is {a}")
        self.no_book=self.no_book+1
        self.book.append(a)
    def showlib(self):
        print(f"the total no of book in library is {self.no_book} and library is {self.book}")    

a=library()
a.add("game")
a.showlib()
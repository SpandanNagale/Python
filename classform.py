class Form:
    Name=input("enter your name")
    Occupation=input("enter your Occupation")
    def show(self):
        print(f"Name of the student is {self.Name} and his occupation{self.Occupation}")

a=Form
a.Name
a.Occupation
a.show()   


     
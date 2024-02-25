class interest:
    principle=int(input("enter the principle amount:"))
    rateofinterest=int(input("enter the rate of interest:"))
    noofyear=int(input("enter the no of year:"))
    def __init__(self) -> None:
        self.principle
        self.rateofinterest
        self.noofyear
    
        amount=self.principle*(1+ self.rateofinterest/100)**self.noofyear
        print(amount)

a=interest()    

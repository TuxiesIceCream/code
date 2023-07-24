class Employee:
    def __init__(self,f,l,p):
        self.first = f
        self.last = l
        self.pay = p
        self.email = f + '.' + l + '@tuxies.com'
        
emp1=Employee("mark","baker",15)
emp2=Employee("peggy","baker",20)
print(emp2.email)

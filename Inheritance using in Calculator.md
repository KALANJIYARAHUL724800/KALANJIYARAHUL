print("\t\t\t---------------------------------------------------")

title = "***** Welcome to My Inheritance Calculator *****"
variable = title.center(100)
print(variable)
print("\t\t\t---------------------------------------------------\n")

number1 = int(input("Enter the Number 1:"))
number2 = int(input("Enter the Number 2:"))

print("1.Additon")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = int(input("Enter your choice:"))
print("------------")
class Additon:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def add(self):
        print(self.n1 + self.n2)

class Subtraction(Additon):
    def __init__(self,n1,n2):
        Additon.__init__(self,n1,n2)
        self.n1 = n1
        self.n2 = n2
    def sub(self):
        print(self.n1 - self.n2)

class Multiplication(Subtraction):
    def __init__(self,n1,n2):
        Subtraction.__init__(self,n1,n2)
        self.n1 = n1
        self.n2 = n2
    def mul(self):
        print(self.n1 * self.n2)

class Division(Multiplication):
    def __init__(self,n1,n2):
        Multiplication.__init__(self,n1,n2)
        self.n1 = n1
        self.n2 = n2
    def div(self):
        print(self.n1 / self.n2)
        
obj = Division(number1,number2)
if choice ==1:
    obj.add()
if choice==2:
    obj.sub()
if choice==3:
    obj.mul()
if choice==4:
    obj.div()
print("------------")

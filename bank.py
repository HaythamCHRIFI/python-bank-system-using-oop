from abc import ABC,abstractmethod
#Parent class : User
#Holds details about an user
#Has a function to show user details
#Child class : Account
#Stores details about the account balance
#Stores details about the amount
#Allows for deposits,withdraw,view_blanace

print("**Hello Welcome to the bank system**\n\n")

class User(ABC):
    def __init__(self,name,age,gender) :
        self.__name = name
        self.__age = age
        self.__gender = gender

    @abstractmethod
    def view_blanace(self):
        pass

    def getName(self):
        return self.__name
    def setName(self,protectname):
        self.__name = protectname

    def getAge(self):
        return self.__age
    def setAge(self,protectage):
        self.__age = protectage

    def getGender(self):
        return self.__gender
    def setGender(self,protectgender):
        self.__gender = protectgender

    name = property(getName,setName)
    age = property(getAge,setAge)
    gender = property(getGender,setGender)




class UserAccount(User):
    
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.__amount = amount
        self.balance += amount

    def withdraw(self,amount):
        self.__amount = amount
        if(self.balance < amount):
            print("you can't withdraw this amount\n")
        else:
            self.balance -= amount

    def getAmount(self):
        return self.__amount
    def setAmount(self,amount):
        self.__amount = amount

    amount = property(getAmount,setAmount)

    def view_blanace(self):
        return f"## {self.name} Account ##\n\n===============\n Name : {self.name} \n Age : {self.age} \n Aender : {self.gender} \n Amount : {self.balance}$ \n ==============="


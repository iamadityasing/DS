import re
'''str1="emma luck numbers are 2514 7617 2319 4501"
stringpattern=r"\d{4}"
regex_pattern=re.compile(stringpattern)
result=regex_pattern.findall(str1)
print(result)'''
# str="emma is a basketball player who was born ion june 17"
# result=re.findall(r"\w{4}",str)
# # print("Match.object:",result)
# # print("Match value:",result.group())
# 
# print(result)

#w is used for words and W is used for special characters
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        if len(str(accountNumber))!=10 or str(accountNumber)[0]!="1":
            print("Invalid account number")
        else:
            self.accountNumber=accountNumber
            self.name=name
            self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
    def withdrawl(self,amount):
        if amount>self.balance:
            print("Issuficient Balance")
        else:
            self.balance-=amount
    def bankFees(self):
        self.balance=0.95*self.balance
    def display(self):
        print("ACCOUNT NUMBER:",self.accountNumber)
        print("ACCOUNT HOLDER NAME",self.name)
        print("ACCOUNT BALANCE",self.balance) 

obj1=BankAccount(1234567890,"rahul",50000)
print(obj1)
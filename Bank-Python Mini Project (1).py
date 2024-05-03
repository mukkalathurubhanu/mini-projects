class Account():
     def __init__(self,accName,accNo,accType,accBal):
         self.__accName=accName
         self.___accNo=accNo
         self.__accType=accType
         self.__accBal=accBal
     def getAccName(self):
           return self.__accName
     def getAccNo(self):
          return self.__accNo
     def getAccType(self):
           return self.__accType
     def getAccBal(self):
          return self.__accBal
     def withdraw(self):
           amount=int(input("\nEnter amount to be withdrawn:"))
           if self.__accBal-500 >= amount:
              self.__accBal -= amount
              print("Amount withdrawn successfully")
              print("updated Account balance : ",self.getAccBal())
           else:
              print("Insufficient Balance, Try again.")
     def  deposit(self):
            amount= int(input("\nEnter amount to be deposited : "))
            self.__accBal += amount
            print("updated Account Balance :",self.getAccBal())
     def dispAccDetails(self):
        print("\nAccount Name : ",self.__accName)
        print("\nAccount No : ",self.__accNo)
        print("\nAccount Type : ",self.__accType)
        print("\nAccount Balance : ",self.__accBal)
        print() 

#main code

accName=input("Enter Account Name:")
accNo=input("Enter Account Number:")
print("Enter 1 for SAVING Account")
print("Enter 2 for CURRENT Account")
option=int(input("Enter Account Type:"))
accType='Saving' if option==1 else 'Current'
accBal=float(input("Enter Initial Balance: $"))

acc=Account(accName,accNo,accType,accBal)

print("\n\nPress 1 for Account Name")
print("Press 2 for Account Number")
print("Press 3 for Account Type")
print("Press 4 for Account Balance")
print("Press 5 for Account Details")
print("Press 6 for Cash Withdrawl")
print("Press 7 for Cash Deposit")

while True:
     option=int(input("\nSelect your option"))
     if option == 1:
         print("\nAccount Name : ",acc.getAccName())
     elif option == 2:
         print("\nAccount Number :" ,acc.getAccNo())
     elif option == 3:
         print("\nAccount Type :",acc.getAccType())
     elif option == 4:
         print("\nUpdated Account Balance : ",acc.getAccBal())
     elif option == 5:
         acc.dispAccDetails()
     elif option == 6:
          acc.withdraw()
     elif option == 7:
          acc.deposit()
     else:
         print("\nInvalid Option")
     print("\nDo you wish to continue...")
     trnx=input("Y/N : ")  
     if trnx.lower() == "n" : break
print("\nThank you...Visit Again!") 
        

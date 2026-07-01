# Bank Management System

class BankAccount:
    
    next_account_number = 1001;
    
    def __init__(self,customer_name,balance,pin):
        self.account_number=BankAccount.next_account_number;
        BankAccount.next_account_number+=1;
        self.customer_name=customer_name;
        self.__balance=balance;
        self.__pin=pin
        self.transaction=[];
        
    def displayDetails(self):
        print(f"The name of the customer is {self.customer_name} and the account number is {self.account_number}")
    
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount;
            self.transaction.append(f"The {amount} has been deposited")
        else:
            print("Invalid Amount");
        # print("The money has been deposited");
    
    def withdraw(self,amount):
        
        if amount > 0 and amount <= self.__balance:
            self.__balance-=amount;
            self.transaction.append(f"The {amount} has been withdraw")
        else:
            print("Insufficent balance");
        # print("Money has been withdraw from the back account")
    
    def checkBalance(self,pin):
        
        if pin ==self.__pin:
            print(f"The balance of the customer is :{self.__balance}")
        else:
            print("Invalid Pin");
            
    def changePin(self,old_pin,new_pin):
        if old_pin==self.__pin:
            self.__pin=new_pin;
            print("Pin changed successfully!!")
        else:
            print("Invalid old pin")
    
    def updateName(self,name):
        self.customer_name=name;
        print("Customer name updated successfully.")
        
    def transfermoney(self,recevier,amount):
        
        if amount> 0 and amount<=self.__balance:
            recevier.__balance+=amount;
            self.__balance-=amount;
            print(f"The balance of the recevier is : {recevier.__balance}")
            print(f"The balance of the sender is : {self.__balance}")
            self.transaction.append(f"Transferred ₹{amount} to {recevier.customer_name}")
            recevier.transaction.append(f"Received ₹{amount} from {self.customer_name}")
        else:
            print("Invalid amount or insufficient balance")
            
    def showTranscationHistory(self):
        for i in range(len(self.transaction)):
            print(self.transaction[i]);
        

c1=BankAccount("Priya Lodha",240000,1290);
c2=BankAccount("Rahul Sharma",900000,1900);
c1.transfermoney(c2,60000);
c1.deposit(2000);
c1.withdraw(4000);
c1.showTranscationHistory()
c1.displayDetails()
c1.deposit(4000);
c1.withdraw(300);
c1.checkBalance(1290);
c2.displayDetails()
# c1.changePin(1290,98254);
# c1.updateName("Rahul");
# c1.displayDetails()
# print(c1.__balance);
class ATM(object):

    def __init__(self, name, age, gender,cardNo,phone,cardPin,balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.cardNo = cardNo
        self.phone = phone
        self.cardPin = cardPin
        self.balance= balance


    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender) 
        print("cardNo:",self.cardNo) 
        print("cardPin:",self.cardPin) 
        print("phone:",self.phone) 

    

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit of rupees ',str(amount)," was successful")


    def withdraw(self,amount):
        self.balance=self.balance-amount
        print('Withdrawal of rupees ',str(amount)," was successful")

        
    def balanceEnquiry(self):
        print("Your total balance is:",str(self.balance))

    

    def main():
        ATM1=ATM("Fahim","16","Male","1234567890","9830017113","234","1000000000")
        ATM1.display()
        print("Enter a number from list to perform a task")
        print("1.To Deposit Money")
        print("2.To Withdraw Money")
        print("3.To See Your Balance")
        task=input("Enter your Choice")

        choice(task)

        def choice(task):
            switcher={
                1:
                    ATM1.deposit(input("Enter Deposit Amount ")),
                2:
                    ATM1.withdraw(input("Enter Withdrawal Amount ")),
                3:
                    ATM1.balanceEnquiry(),
            }

ATM.main()




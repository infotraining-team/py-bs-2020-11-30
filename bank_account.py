class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if (self.__balance + amount > 0):
            self.__balance += amount
        else:
            print("Insufficient funds")

    def show(self):
        print("Owner: ", self.__owner, " balance =", self.__balance)


user1 = BankAccount("Leszek", 100)
user2 = BankAccount("Ola", 200)

user1.show()
user2.show()

user1.deposit(100)
user1.show()

user1.deposit(-300)
#print(user1.__balance)
user1.show()

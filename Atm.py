class Atm(object):
      def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
      def cashWidrawal(self,amount):
         newAmount = 50000-amount
         print(newAmount)
      def checkBalance(self):
         print('Your balance is 50000')
def main():
   cardNumber = input('Insert Your Card Number')
   pinNumber = input('Insert Your Pin Number')
   newUser = Atm(cardNumber,pinNumber)
   print('Choose Your Activity')
   print('1.Balance Enquiry, 2.Withdrawal')
   activity = int(input('Enter Your Activity Number'))
   if(activity == 1):
      newUser.checkBalance()
   elif(activity == 2):
      amount = int(input('Enter The Amount'))
      newUser.cashWidrawal(amount)
   else:
      print('Enter A Valid Number')
main()

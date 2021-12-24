from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program")

continue_auc = True
bidder = []

def addBidder(addName, addAmount):
  new_bidder = {}
  new_bidder['bidname'] = addName
  new_bidder['amount'] = addAmount
  bidder.append(new_bidder)

while continue_auc:
  name = input("What is your name?: ")
  amount = int(input("What's your bid?: $ "))
  more = input("Are There any other bidders? Type 'yes' or 'no' ")
  addBidder(name, amount)

  if (more == 'no'):
    continue_auc = False
  else:
    clear()
    continue_auc = True

highamount = 0
highname = ''
highindex = 0
for i in range(0, len(bidder)):
  if int(bidder[i]['amount']) > highamount:
    highamount = bidder[i]['amount']
    highname = bidder[i]['bidname']
    highindex = i

print(f"Highest bid is from {highname} for amount ${highamount}")
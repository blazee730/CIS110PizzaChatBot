# Name: Johnathan Jeanty
# Course: CIS110
# Lab Title: Pizza Ordering Chatbot

print("Hello, my name is Alex your virtual assistant. I will help  you order a pizza!")
print("I am going to ask you a few questions. After typing an answer, press enter.")
userName = input("\nEnter your name:  ")
while len(userName) == 0:
    userName = input("Name cannot be blank! Please enter your name: ")
if userName.lower() == "professor quigley":
    print(f"\nMy creator, {userName}. What a pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")    
size = input("\nWhat size do you want? Enter small, medium, or large")
while size.lower() not in ["small", "medium", "large"]:
    size= input("Invalid value! Please enter small, medium, or large:")
flavor = input("\nEnter the flavor of pizza:  ")
while len(flavor) == 0:
    flavor = input("Flavor cannot be blank! Please enter a flavor: ")
crustType = input("\nWhat type of crust do you want:  ")
while len(crustType) == 0:
    crustType = input("Crust type cannot be blank! Please enter a crust type: ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
while not quantity.isdigit():
    quantity = input("Value not recognized. Please enter a numeric value: ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery:  ")
while method not in ["carry out", "delivery"]:
    method = input("Invalid Value! Please enter carry out or delivery: ")


if method.lower() == "delivery":
    deliveryFee = 5
else:
    deliveryFee = 0
salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99

total = (pizzaCost * quantity) * salesTax + deliveryFee
print("-" * 10)
print(f"Thank you, {userName}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust cost ${total:,.2f}.")

if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrders over $50 will receive a free $10 Off coupon!")
print("-" * 10)
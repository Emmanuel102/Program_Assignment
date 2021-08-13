print("Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client their name and save it to a variable.
name = input("Hello, what's your name?")
print("name")
# TODO: Write code to ask the client their savings and save it to another variable.
savings = input("How much do you have in your savings?")
print("savings")
# TODO: Write code to ask the client the stock they is interested in and save it to another variable, as shown below.
stock = input("How much do you have in your savings?")
print("savings")
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print("stock")

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:
if stock == "amzn":
    ...
elif ...
else ...
'''

if stock == "amazn" :
    result = savings/amazon

elif stock == "apple" :
    result = savings/apple
elif stock == "fb" :
    result = savings/fb
elif stock == "google" :
    result = savings/google
elif stock == msft :
    result = savings/msft
else:
    print("That is not one of the stocks listed above")

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and they can buy 50 shares of Apple.

print()
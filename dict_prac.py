# step 2

from typing import Counter


groceries = {'Chicken': 1.59, 'Beef': 1.99, 'Cheese': 1.00, 'Milk': 2.5 }
# printgroceries

chicken_price = groceries['Chicken']
Beef_price = groceries['Beef']


# step 3
anime = {'Naruto': 2005, 
        'Fullmetal Alchemist': 2004, 
        'One Piece': 2003, 
        'Jujitsu Kaisen': 2018}

Naruto = anime ['Naruto']
Fullmetal_Alchemist = anime['Fullmetal Alchemist']
anime['Naruto'] = 2008

print(anime)
del anime['Naruto']
print(anime)

def total_price(item_1, item_2):
        price_1 = groceries[item_1]
        price_2 = groceries[item_2]

        return price_1 + price_2

print(total_price("Beef", "Chicken"))

print("Price of cheese and beef:" + str(total_price("Beef", "Chicken")))

def price_difference(item_2, item_3):
        price_2 = groceries[item_2]
        price_3 = groceries[item_3]

        if price_3 > price_2:
                difference = price_3 - price_2
        else:
                difference = price_2 - price_3
        return difference

print(price_difference("Milk", "Cheese"))
print(price_difference("Cheese", "Chicken"))

shoes = {"Jordan 13": 1, "Yeezy": 8, "Foamposite": 10, "Air Max": 5, "SB Dunk": 20}

def restock(shoe_type, count):
        shoes[shoe_type] = shoes[shoe_type] * count
        return shoes[shoe_type]

print(restock("Yeezy", 3))

def clearance_sale(shoes_dic, shoe_type, num):
        shoes_dic[shoe_type] = shoes_dic[shoe_type] / num
        return shoes_dic

print(shoes)
print("Updated shoes: ")
print(clearance_sale(shoes, "SB Dunk", 10))






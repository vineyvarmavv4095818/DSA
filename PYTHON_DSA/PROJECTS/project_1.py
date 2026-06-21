menu = {
    'Coffee':60,
    'Pizza':150,
    'Tea':10,
    'Burger':80,
    'Sendwich':60,
}
print("<-<-WELCOME TO PYHTON RESTAURANT->->")
print("<<MENU>>\nCoffee: Rs60\nPizza: Rs150\nTea: Rs10\nBurger: Rs80\nSendwich: Rs60")

order_total = 0

item_1 = input("Please enter the name of your order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} is added to your order.") 
else:
    print("The item is not available yet.")

another_order = input("Do you want to order another item(Yes/No):")
if (another_order == "Yes"):
    item_2 = input("Please enter your order:")
    order_total += menu[item_2]
    print(f"Your item {item_2} is added to your order.")
    

print(f"The total amonut of your order to pay is Rs{order_total}")

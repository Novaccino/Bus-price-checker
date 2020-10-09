#bus tickets

Tickets = int(input("Enter the amount of tickets you'd like to buy?: "))
Price = float(input("Enter the price of a single ticket?: "))
Total = (Tickets * Price)
print ("The price is %f euro" %Total)
Money_offered = float(input("How much money do you offer?: "))
Change = Money_offered - Total
print ("You get %f euro change" %Change)
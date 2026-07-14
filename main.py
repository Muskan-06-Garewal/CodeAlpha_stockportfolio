print("***WELCOME TO STOCK PORTFOLIO TRACKER***") 

user_name = input("Enter your name :")


portfolio = []

add_stocks = "yes"

while add_stocks == "yes":

   stock_name = input("Stock Name :")

   stock_quantity = int(input("Enter Quantity:"))

   stock_price = int(input("Enter the price of stock : "))

#calculating the investment of the user 

   calculate_investment = (stock_quantity * stock_price)
   print("Total investment:",calculate_investment)

#creating the empty list to store the information for the stocks of the user

   stock = { 
    "Stock Name": stock_name,
    "Quantity": stock_quantity,
    "Price": stock_price,
    "Investment": calculate_investment
     }

   portfolio.append(stock)
   add_stocks = input("Do you want to add another stock? (yes/no): ").lower()
 
print("\n========== PORTFOLIO ==========")

total_investment = 0

for stock in portfolio:
    print(stock)
    total_investment = total_investment + stock["Investment"]

print("\nTotal Portfolio Investment :", total_investment)

print("Thank you for using stock portfolio tracker")
   
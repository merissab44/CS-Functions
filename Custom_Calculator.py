#gathers the price of house or (Cost of goods).
price = input("What is your total cost to produce your product?")
#gathers the minimum profit margin you want to receive.
desired_profit = input(
    "what is the profit margin you would like to achieve?(enter whole number)")
#type casts the input into a integer and converts that number (desired_profit into a decimal.
profit_margin = int(desired_profit) / 100
#calculates the price you must sell at in order to gain that profit margin.(net sales)
sell_price = int(price) / (1 - profit_margin)
#prints the result of the sell price to gain the profit margin you inputted.
print(f"To get a profit margin of {desired_profit}%, you must sell your product for ${round(sell_price)}")

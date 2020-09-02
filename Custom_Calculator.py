while True:
#gathers the cost to produce your product or (Cost of goods).
        price = input("What is your total cost to produce your product? ")
#gathers the markup profit margin you want to achieve.
        desired_profit = input("what is the profit margin you would like to achieve?(enter whole number) ")
        while int(desired_profit) < 0 or int(price) < 0:
                print("Sorry, your response must not be negative.")
                price = input("What is your total cost to produce your product?")
                desired_profit = input("what is the profit margin you would like to achieve?(enter whole number)")
                continue
        while int(desired_profit) > 100:
                print("Sorry, I can't calculate that.")
                price = input("What is your total cost to produce your product?")
                desired_profit = input("what is the profit margin you would like to achieve?(enter whole number)")
                break              
#desired_profit was successfully parsed, meaning the value is a whole positive number.
#type casts the input into a float and converts that number (desired_profit into a decimal.
        profit_margin = int(desired_profit) / 100
#calculates the price you must sell at in order to gain that markup profit margin.(net sales)
        sell_price = int(price)/ (1- profit_margin)
#prints the result of the sell price to gain the markup profit margin you inputted.
        print(f"To get a profit margin of {desired_profit}%, you must sell your product for ${round(sell_price,2)}")
#I used stack overflow to understand the while loop and programiz.com to understand the round function.
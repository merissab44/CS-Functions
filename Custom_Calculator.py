#from my understanding, this means run forever.
while True:
#gathers the cost to produce your product or (Cost of goods).
        price = input("What is your total cost to produce your product? ")

        while int(price) < 0:
                print("sorry, the number can't be a negative")
                price = input("What is your total cost to produce your product? ")
                continue
#gathers the markup profit margin you want to achieve. if it is negative, it will
#notify you that a negative is not valid and to give another input.
        desired_profit = input("what is the profit margin you would like to achieve?(enter whole number) ")
        while int(desired_profit) < 0:
                print("sorry, the number can't be a negative")
                desired_profit = input("what is the profit margin you would like to achieve?(enter whole number) ")
                #this continue keyword, prompts python to move to the next iteration
                continue
        while int(desired_profit) > 100:
                print("Sorry I can't calculate that. please enter a value between 0 and 100")
                desired_profit = input("what is the profit margin you would like to achieve?(enter whole number) ")
#desired_profit was successfully parsed, meaning the value is a whole positive number.

#type casts the input into a int and converts that number (desired_profit into a decimal.
        profit_margin = int(desired_profit) / 100
#calculates the price you must sell at in order to gain that markup profit margin.( required net sales)
        sell_price = int(price)/ (1- profit_margin)
#prints the result of the sell price to gain the markup profit margin you inputted.
        print(f"To get a profit margin of {desired_profit}%, you must sell your product for ${round(sell_price,2)}")
#I used stack overflow to understand the while loop and programiz.com to understand the round function.
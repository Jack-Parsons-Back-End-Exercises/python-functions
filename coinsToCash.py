def calc_dollars(**coins):
    dollarAmount = 0

    for coin, amount in coins.items():
        
        if coin == "pennies":
            dollarAmount += amount * .01
        elif coin == "nickels":
            dollarAmount += amount * .05
        elif coin == "dimes":
            dollarAmount += amount * .1
        elif coin == "quarters":
            dollarAmount += amount * .25

    print(format(dollarAmount, '.2f'))

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
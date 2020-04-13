import math

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def calc_coins(dollarAmount, **piggyBank):
    for coins, amount in piggyBank.items():
        dollarsX100 = dollarAmount * 100
        remainingMoney = 0

        if coins == "quarters":
            piggyBank["quarters"] = int(dollarsX100 / 25)
            remainingMoney += dollarsX100 % 25
            
            if remainingMoney != 0:
                piggyBank["dimes"] = int(remainingMoney / 10)
                remainingMoney = remainingMoney % 10
               
                if remainingMoney != 0:
                   piggyBank["nickels"] = int(remainingMoney / 5)
                   remainingMoney = remainingMoney % 5
            
                   if remainingMoney != 0:
                       piggyBank["pennies"] = int(remainingMoney)
        
    print(piggyBank)


calc_coins(dollarAmount, **piggyBank)
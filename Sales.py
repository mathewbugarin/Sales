#Simple program to demosnstrate functions in python
#Program calculates sales, and determines bonuses

def main():
    monthlySales = getSales()
    salesIncrease = getIncrease()
    storeAmount = storeBonus(monthlySales)
    empAmount = empBonus(salesIncrease)
    printBonus(storeAmount, empAmount)

def getSales():
    monthlySales = input("Enter the amount of monthly sales: ")
    monthlySales = float(monthlySales)
    return monthlySales

def getIncrease():
    salesIncrease = input("Enter the percent of sales increase: ")
    salesIncrease = float(salesIncrease)
    return salesIncrease

def storeBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

def empBonus(salesIncrease):
    if salesIncrease >= 5:
        empAmount = 75
    elif salesIncrease >= 4:
        empAmount = 50
    elif salesIncrease >= 3:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

def printBonus(storeAmount, empAmount):
    print ("The store bonus amount is: $", storeAmount)
    print ("The employee bonus amount is: $", empAmount)
    if storeAmount == 6000 and empAmount == 75:
        print ("Congrats! You have reached the highest bonus points possible!")

main()
    

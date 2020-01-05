def monthly():
    loanPayment = float(input('Enter the monthly cost of loan payment: '))
    insurance = float(input('Enter the monthly cost of insurance: '))
    gas = float(input('Enter the monthly cost of gas: '))
    oil = float(input('Enter the monthly cost of oil: '))
    tires = float(input('Enter the monthly cost of tires: '))
    maintenance = float(input('Enter the monthly cost of maintenance: '))
    return loanPayment, insurance, gas, oil, tires, maintenance
            
def totalMonthly():
    total = loanPayment + insurance + gas + oil + tires + maintenance
    print('The total monthly cost of your expenses is', total)
    return total

def totalAnnual():
    annual = total * 12
    print('Your total annual cost is', annual)

def main():
    import time
    monthly()
    totalMonthly()
    totalAnnual()
    time.sleep(3)

main()

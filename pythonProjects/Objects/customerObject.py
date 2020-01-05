import customer

def createObject():
    customerOne = customer.Customer('Tyrell Brantley', '123 Finnangle Road', '123-456-7890', customerMailingChoice())
    
def main():
    import time
    creatObject()
    time.sleep(3)
    
main()
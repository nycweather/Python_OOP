from items import Item
from phone import Phone
    
if __name__ == "__main__":
    #Printing Stuff

    #Item.read_from_csv()
    #print(Item.whole_list)


    phone1 = Phone("jscPhonevi10", 500, 5, 1)
    #phone1.__name = 'Test'
    print(Phone.whole_list)
    #phone1.price = 600
    print(phone1.price)
    phone1.increment_price(0.46)
    print(phone1.price)
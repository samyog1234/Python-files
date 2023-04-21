inventory={}

def adding_product():
    code=input("Enter an code to add product:")
    name=input("Enter name to you product:")
    quantity=int(input("Enter an quantoty "))
    price=float(input("Enter a price to your product:"))
    inventory[code]={"name":name,"quantity":quantity,"price":price}

def del_product():
    code=input("Enter a code to delete product")
    if code in inventory:
        del inventory[code]
        print("The product has been removed")
    else:
        print("product not found")

def search_product():
    code=input("Enter code to search your product:")
    if code in inventory:
        print(inventory[code])
    else:
        print("product not found")

def list_product():
    code=input("Enter code to make a list:")
    if code in inventory:
        product=inventory[code]
        print(product["name"],product["quantity"],product["price"])
    else:
        print("Product not found")

while True:
    print("1. Add product")
    print("2. Delete product")
    print("3. Search product")
    print("4. make list of product")
    print("5. quit")
    guess=int(input("Enter what do you want to do today:"))
    if guess == 1:
        adding_product()
    elif guess == 2:
        del_product()
    elif guess == 3:
        search_product()
    elif guess ==4:
        list_product()
    elif guess ==5:
        print("Thankyou for your visit")
        break
    else:
        print("Wrong input")



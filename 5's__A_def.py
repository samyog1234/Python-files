inventory = {}

def add_product():
    code = input("Enter product code: ")
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price = float(input("Enter product price: "))
    inventory[code] = {"name": name, "quantity": quantity, "price": price}

def remove_product():
    code = input("Enter product code: ")
    if code in inventory:
        del inventory[code]
        print("Product removed.")
    else:
        print("Product not found.")

def search_product():
    code = input("Enter product code: ")
    if code in inventory:
        print(inventory[code])
    else:
        print("Product not found.")

def list_products():
    for code, product in inventory.items():
        print(code, product["name"], product["quantity"], product["price"])

while True:
    print("1. Add product")
    print("2. Remove product")
    print("3. Search product with product code")
    print("4. List all the products")
    print("5. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        search_product()
    elif choice == 4:
        list_products()
    elif choice == 5:
        print("thankyou for visiting")
        break
    else:
        print("Invalid choice. Please try again.")
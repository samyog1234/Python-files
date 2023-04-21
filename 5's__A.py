inventory = {}

while True:
    print("Inventory Management System")
    print("1. Add product")
    print("2. Remove product")
    print("3. Search product with product code")
    print("4. List all the products")
    print("5. Quit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        code, name, quantity, price = input("Enter the product code, name, quantity, and price, separated by commas: ").split(",")
        inventory[code] = {"name": name, "quantity": int(quantity), "price": float(price)}
        print(f"{name} has been added to the inventory.")

    elif choice == "2":
        code = input("Enter the product code: ")
        if code in inventory:
            del inventory[code]
            print(f"The product with code {code} has been removed from the inventory.")
        else:
            print(f"The product with code {code} is not in the inventory.")

    elif choice == "3":
        code = input("Enter the product code: ")
        if code in inventory:
            product = inventory[code]
            print(f"Product code: {code}")
            print(f"Product name: {product['name']}")
            print(f"Product quantity: {product['quantity']}")
            print(f"Product price: {product['price']}")
        else:
            print(f"The product with code {code} is not in the inventory.")

    elif choice == "4":
        if inventory:
            print("Product code\tProduct name\tQuantity\tPrice")
            for code, product in inventory.items():
                print(f"{code}\t{product['name']}\t{product['quantity']}\t{product['price']}")
        else:
            print("The inventory is empty.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

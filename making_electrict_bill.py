def electricity_bill():
    unit_count = int(input("Enter you electric unit to calculate its bill:"))
    if unit_count <= 100:
        print("No Charge!")
    elif unit_count < 200:
        print("It is rs 5 per unit and that is",unit_count*5)
    else:
        print("It is rs 10 per unit and that is",unit_count*10)
electricity_bill()
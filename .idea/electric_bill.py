"""The python code to find electricity bill
            first 100 units = no charge
            next 100 units = Rs 5 per unit
            after 200 units = Rs 10 per unit"""
def electricity_bill():
    unit_count = int(input("Enter you electric unit to calculate its bill:"))
    if unit_count <= 100:
        print("No Charge!")
    elif unit_count <200:
        unit_count = (unit_count-100)*5
        print(unit_count)
    else:
        unit_count = (100*5)+10*(unit_count-200)
        print(unit_count)
electricity_bill()
 
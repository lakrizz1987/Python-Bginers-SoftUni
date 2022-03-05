number_of_joinery = int(input())
joinery_style = input()
kind_of_delivery = input()
price = 0
delivery = 0
invalid = False
if number_of_joinery < 10:
    invalid = True
else:
    if joinery_style == "90X130":
        price = 110
        if 60 >= number_of_joinery > 30:
            price = price * 0.95
        elif number_of_joinery > 60:
            price = price * 0.92
    elif joinery_style == "100X150":
        price = 140
        if 80 >= number_of_joinery > 40:
            price = price * 0.94
        elif number_of_joinery > 80:
            price = price * 0.9
    elif joinery_style == "130X180":
        price = 190
        if 50 >= number_of_joinery > 20:
            price = price * 0.93
        elif number_of_joinery > 50:
            price = price * 0.88
    elif joinery_style == "200X300":
        price = 250
        if 50 >= number_of_joinery > 25:
            price = price * 0.91
        elif number_of_joinery > 50:
            price = price * 0.86
if kind_of_delivery == "With delivery":
    delivery = 60
elif kind_of_delivery == "Without delivery":
    delivery = 0
all_price = (number_of_joinery * price) + delivery
if number_of_joinery > 99:
    all_price = all_price * 0.96
if invalid:
    print("Invalid order")
else:
    print(f"{all_price:.2f} BGN")

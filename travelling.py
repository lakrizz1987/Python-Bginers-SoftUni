destination = input()
price = float(input())
save_money = 0

while True:

    while save_money < price:
        money = float(input())
        save_money += money
        if save_money >= price:
            save_money = 0
            print(f"Going to {destination}!")
            destination = input()

            if destination == "End":
                break
            price = float(input())
    if destination:
        break

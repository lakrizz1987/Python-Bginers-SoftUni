year_tax = int(input())
basket_shoes_percent = 40/100
basket_shoes = year_tax -( basket_shoes_percent*year_tax)
basket_equip_percent = 20/100
basket_equip = basket_shoes - (basket_shoes*basket_equip_percent)
basket_ball_price = basket_equip / 4
basket_accesoary = basket_ball_price / 5
all_sum_need = basket_shoes+basket_equip+basket_ball_price+basket_accesoary+year_tax
print(all_sum_need)
import math

balls = int(input())
red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
black_counter = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
other_counter = 0
total_points = 0
for x in range(balls):
    color = input()
    if color == "red":
        total_points += 5
        red_counter +=1
    elif color == "orange":
        total_points += 10
        orange_counter +=1
    elif color == "yellow":
        total_points += 15
        yellow_counter += 1
    elif color == "white":
        total_points += 20
        white_counter += 1
    elif color == "black":
        black_counter += 1
        total_points = math.floor(total_points / 2)
    else:
        other_counter += 1
print(f"Total points: {total_points}")
print(f"Points from red balls: {red_counter}")
print(f"Points from orange balls: {orange_counter}")
print(f"Points from yellow balls: {yellow_counter}")
print(f"Points from white balls: {white_counter}")
print(f"Other colors picked: {other_counter}")
print(f"Divides from black balls: {black_counter}")




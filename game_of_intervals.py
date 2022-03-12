number_turns = int(input())
points = 0
all_points = 0
counter_0_to_9 = 0
counter_10_to_19 = 0
counter_20_to_29 = 0
counter_30_to_39 = 0
counter_40_to_50 = 0
counter_invalid_numbers = 0

for x in range(number_turns):
    number = int(input())
    if 0 <= number <= 9:
        points = number * 0.2
        counter_0_to_9 += 1
    elif 10 <= number <= 19:
        points = number * 0.3
        counter_10_to_19 += 1
    elif 20 <= number <= 29:
        points = number * 0.4
        counter_20_to_29 += 1
    elif 30 <= number <= 39:
        points = 50
        counter_30_to_39 += 1
    elif 40 <= number <= 50:
        points = 100
        counter_40_to_50 += 1
    else:
        points = 0
        all_points = all_points / 2
        counter_invalid_numbers += 1

    all_points += points

print(f"{all_points:.2f}")
print(f"From 0 to 9: {counter_0_to_9 / number_turns * 100:.2f}%")
print(f"From 10 to 19: {counter_10_to_19 / number_turns * 100:.2f}%")
print(f"From 20 to 29: {counter_20_to_29 / number_turns * 100:.2f}%")
print(f"From 30 to 39: {counter_30_to_39 / number_turns * 100:.2f}%")
print(f"From 40 to 50: {counter_40_to_50 / number_turns * 100:.2f}%")
print(f"Invalid numbers: {counter_invalid_numbers / number_turns * 100:.2f}%")

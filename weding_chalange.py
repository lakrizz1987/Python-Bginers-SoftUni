man_numbers = int(input())
woman_numbers = int(input())
number_of_tables = int(input())
counter = 0
tables_are_over = False

for x in range(1, man_numbers + 1):
    for y in range(1, woman_numbers + 1):
        print(f"({x} <-> {y})", end=" ")
        counter += 1
        if counter == number_of_tables:
            tables_are_over = True
            break
    if tables_are_over:
        break

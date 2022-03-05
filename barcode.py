start_range = int(input())
stop_range = int(input())
odd_number = ""
counter = 0
for number in range(start_range, stop_range + 1):
    for x, y in enumerate(str(number)):
        if int(y) % 2 != 0:
            counter += 1
            odd_number += str(y)
        else:
            counter = 0
            odd_number = ""
            break
        if counter == 4:
            print(odd_number, end=' ')
            counter = 0
            odd_number = ""

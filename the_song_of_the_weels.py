control_number = int(input())
counter = 0
password_is_found = False
password = ""
for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num1 < num2 and num3 > num4:
                    if (num1 * num2) + (num3 * num4) == control_number:
                        print(f"{num1}{num2}{num3}{num4}", end=" ")
                        counter += 1
                        if counter == 4:
                            password = f"{num1}{num2}{num3}{num4}"
                            password_is_found = True

print()

if password_is_found:
    print(f"Password: {password}")
else:
    print("No!")

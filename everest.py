counter = 1
peak = 5364
command = input()
peak_is_climbed = False
while command != "END":
    if command == "Yes":
        counter += 1
        meters = int(input())
        peak += meters
        if counter > 5:
            peak -= meters
            break
    else:
        counter += 0
        meters = int(input())
        peak += meters
    if peak >= 8848:
        peak_is_climbed = True
        break
    command = input()
if peak_is_climbed:
    print(f"Goal reached for {counter} days!")
else:
    print(f"Failed!\n{peak}")

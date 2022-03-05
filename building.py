floors = int(input())
rooms = int(input())
room_numbers = " "
for i in range(floors,0,-1):
    for j in range(rooms):
        curent_room = i*10+j
        if i == floors:
            print(f"L{curent_room}",end=" ")
        elif i % 2 != 0:
            room_numbers += f"A{curent_room} "
        else:
            room_numbers += f"O{curent_room } "
    print(room_numbers)
    room_numbers = ""


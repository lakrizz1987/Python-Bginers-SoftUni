start_num = input()
stop_num = input()
for i in range(int(start_num[0]), int(stop_num[0]) + 1):
    for j in range(int(start_num[1]), int(stop_num[1]) + 1):
        for x in range(int(start_num[2]), int(stop_num[2]) + 1):
            for y in range(int(start_num[3]), int(stop_num[3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and x % 2 != 0 and y % 2 != 0:
                    print(f"{i}{j}{x}{y}",end=" ")

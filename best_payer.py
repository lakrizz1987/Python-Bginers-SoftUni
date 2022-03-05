name = input()
goal_counter = 0
best_payer = ""
hatrik = False
while True:
    if name == "END":
        break
    score = int(input())
    if score >= 10:
        best_payer = name
        goal_counter = score
        hatrik = True
        break
    elif score > goal_counter:
        goal_counter = score
        best_payer = name
    if score >= 3:
        hatrik = True
    name = input()
print(f"{best_payer} is the best player!")
if hatrik:
    print(f"He has scored {goal_counter} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goal_counter} goals.")

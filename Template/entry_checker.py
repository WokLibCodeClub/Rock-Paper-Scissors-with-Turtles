ask_for_input = True
while ask_for_input:
    player = input("Enter r, p or s: ")
    if player in ["r", "p", "s"]:
        ask_for_input = False

print("Go to next bit...")

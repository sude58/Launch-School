# Loop keeps running because while loop condition is always true, so it will always continue while loop.

condition = True
while condition:
    print("and on")
    condition = False # This change will make while loop stop after one iteration since it will change while loop condition to be false.
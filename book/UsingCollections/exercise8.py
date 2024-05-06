text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# line 3 and 4 have different values since rfind returns index of subsequence if it ran on the subsequence.
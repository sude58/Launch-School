sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# Will print 3.99 since not sale will be False since sale is True (not reverses True and False).
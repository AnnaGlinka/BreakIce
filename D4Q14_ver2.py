message = "Hello43DD world!"

upper_no = sum(1 for char in message if char.isupper())
lower_no = sum(1 for char in message if char.islower())
print(f"UPPER CASE {upper_no}\nLOWER CASE {lower_no}")
message = "Hello world!"
upper_no, lower_no = 0, 0

for ch in message:
    if ch.isupper():
        upper_no += 1
    elif ch.islower():
        lower_no += 1

print(f"UPPER CASE {upper_no}\nLOWER CASE {lower_no}")

#hello world! 123
#ord() function returns an integer representing the Unicode character

message = "azAZ $@&&09"
no_letters, no_digits = 0, 0

for ch in message:
    n = ord(ch)
    if n in range(97, 123) or n in range(65,91):
        no_letters += 1
    if n in range(48,58):
        no_digits += 1

print(f"LETTERS {no_letters}\nDIGITS {no_digits}")
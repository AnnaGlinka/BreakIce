#hello world! 123

message = input("add your message: ")
no_letters, no_digits = 0, 0

for ch in message:
    if ch.isdigit():
        no_digits += 1
    if ch.isalpha():
        no_letters += 1

print("LETTERS", no_letters)
print("DIGITS", no_digits)
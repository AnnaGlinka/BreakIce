

print("Add your lines: ")
lines = []
while True:
    line = input()
    if line:
        lines.append(line.upper())
    else:
        break

print("\n".join(lines))

# Hello world
# Practice makes perfect
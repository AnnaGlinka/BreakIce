#ABd1234@1,a F1#,2w3E*,2We3345,A$d14

def valid(pw) -> bool:

    if len(pw) < 6 or len(pw) > 12:
        return False
    rules = [0, 0, 0, 0] # lower, upper, char, number
    for c in pw:
        if 'a' <= c <= 'z':
            rules[0] +=1
        elif 'A' <= c <= 'Z':
            rules[1] +=1
        elif c in "$#@":
            rules[2] +=1
        elif '0' <= c <= '9':
            rules[3] +=1

    if all(x > 0 for x in rules):
        return True
    return False



passwords = input("add passwords list:").split(',')
correct = list(filter(valid, passwords))

print(",".join(correct))
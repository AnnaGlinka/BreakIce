#ABd1234@1,a F1#,2w3E*,2We3345

passwords = input("add passwords list:").split(',')

def valide(pw) -> bool:
    if len(pw) < 6 or len(pw) > 12:
        return False
    rules = [0, 0, 0, 0] # lower, upper, char, number
    for c in pw:
        if c 
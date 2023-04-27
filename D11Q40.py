# "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

inp = input()
if inp in ("yes", "YES", "Yes"):
    print("Yes")
else:
    print("No")

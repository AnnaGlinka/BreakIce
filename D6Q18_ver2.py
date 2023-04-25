#ABd1234@1,a F1#,2w3E*,2We3345,A$d14
import re
"""
fullmatch - Match the regular expression pattern to the entire string from the first to the last character
https://pynative.com/python/regex/
"""

passwords = input("add passwords list:").split(',')
pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")

print(",".join([pw for pw in passwords if pattern.fullmatch(pw)]))

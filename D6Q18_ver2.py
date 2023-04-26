#ABd1234@1,a F1#,2w3E*,2We3345,A$d14
import re
"""
fullmatch - Match the regular expression pattern to the entire string from the first to the last character
https://docs.python.org/3/library/re.html
^ - matches the start of the string
$ - matches the end of the string
* - zero or more repetitions, ab* will match ‘a’, ‘ab’, or ‘a’ followed by any number of ‘b’s.
. - (Dot.) In the default mode, this matches any character except a newline
? - Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. ab? will match either ‘a’ or ‘ab’.

(?=...)
Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.

"""

passwords = input("add passwords list:").split(',')
pattern = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")

print(",".join([pw for pw in passwords if pattern.fullmatch(pw)]))



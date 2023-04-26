"""
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
"""

text = input().split(" ")
frequency = {}

for word in text:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

sorted_result = dict(sorted(frequency.items()))
for key, value in sorted_result.items():
    print(f"{key}:{value}")
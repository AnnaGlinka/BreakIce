#hello world and practice makes perfect and hello world again

words = input("add words: ").split()
[words.remove(word) for word in words if words.count(word) > 1]
print(" ".join(sorted(words)))
#hello world and practice makes perfect and hello world again

words = input("add words: ").split(" ")
words = sorted(list(set(words)))
print(" ".join(words))
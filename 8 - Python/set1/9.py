
lines = 0
words = 0
chars = 0

f = open("testing.txt", "r")

for x in f:
    lines += 1

    word = x.split()
    words += len(word)

    chars += len(x)

print('Lines:', lines)
print('Words:', words)
print('Chars:', chars)

f.close()

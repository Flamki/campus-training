# Patterns
# Pattern 1:
# 1 1 1
# 2 2 2
# 3 3 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, end=" ")
    print()

# Pattern 2:
# AAAAA
# BBBBB
# CCCCC
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(chr(64 + i), end="")
    print()

# Pattern 3:
# 54321
# 54321
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(n + 1 - i, end="")
    print()

# Pattern 4:
# A
# AB
# ABC
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end="")
    print()
















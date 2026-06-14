print("Pattern 1")
for i in range(1, 6):
    print("*" * i)

print("\nPattern 2")
for i in range(5, 0, -1):
    print("*" * i)

print("\nPattern 3")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
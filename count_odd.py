
n = 12345
count = 0

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        count += 1

    n = n // 10

print(count)

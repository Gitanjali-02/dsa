
n = 121
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n == rev:
    print(True)
else:
    print(False)

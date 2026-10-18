
def isPerfectNumber(n):
    if n <= 1:
        return False

    divi_sum = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divi_sum += i

            if i * i != n:
                divi_sum += n // i

    divi_sum -= n

    return divi_sum == n


n = int(input("Enter a number: "))

if isPerfectNumber(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")

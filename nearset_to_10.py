def roundToNearest(s: str) -> str:
    last_digit = int(s[-1])

    if last_digit <= 5:
        return str(int(s) - last_digit)
    else:
        return str(int(s) + (10 - last_digit))


s = input("Enter a number: ")
result = roundToNearest(s)
print(result)
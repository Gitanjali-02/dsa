
def second_largest(arr):
    unique = list(set(arr))

    if len(unique) < 2:
        return "Second largest does not exist"

    unique.sort(reverse=True)
    return unique[1]


numbers = [10, 25, 8, 40, 30]
print("Second Largest:", second_largest(numbers))

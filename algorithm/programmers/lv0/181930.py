def solution(a, b, c):
    numberSet = set([a, b, c])

    numberSetLen = len(numberSet)

    if numberSetLen == 3:
        return (a + b + c)

    if numberSetLen == 2:
        return (a + b + c) * (a**2 + b**2 + c**2)

    return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)

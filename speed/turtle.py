def turtle(n):
    result = 0
    for i in range(n):
        result += (-1) ** i * 4 / (1 + 2 * i)
    return result
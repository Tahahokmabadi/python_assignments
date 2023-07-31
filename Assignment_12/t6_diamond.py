def get_n ():
    n = int(input("Enter n: "))
    return n

def diamond (n):
    if n % 2 == 0:
        n -= 1
    for i in range(1, n + 1, 2):
        print((((n - i) // 2) * " "),(i * "*"))
    for i in range(n - 2, 0, -2):
        print((((n - i) // 2) * " "),(i * "*"))
n = get_n()
diamond(n)
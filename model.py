def fibo(n):
    global number, file

    file = open('fibs.txt', 'w')
    number = [0, 1]
    a, b = 0, 1
    for i in range(n - 2):
        a, b = b, a + b
        number.append(b)


def append_number():
    fibo(10000)
    for num in number:
        file.write(str(num) + '\n')

    file.close()
n = int(input())

if n < 2:
    print('no')
else:
    i = 2
    is_prime = True
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    print('yes' if is_prime else 'no')
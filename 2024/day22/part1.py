def mix(secret_number, value):
    return secret_number ^ value


def prune(secret_number):
    return secret_number % 16777216


def next_secret_number(secret_number):
    secret_number = prune(mix(secret_number, secret_number * 64))
    secret_number = prune(mix(secret_number, secret_number // 32))
    secret_number = prune(mix(secret_number, secret_number * 2048))
    return secret_number


with open('input0.txt') as f:
    secret_numbers = [int(line) for line in f]

sum = 0
for index, secret_number in enumerate(secret_numbers):
    for _ in range(2000):
        secret_number = next_secret_number(secret_number)
    sum += secret_number
print(sum)

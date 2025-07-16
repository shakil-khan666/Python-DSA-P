num = 12345
digit = []

while num != 0:
    last_number = num % 10
    digit.append(last_number)
    num = num // 10

digit.reverse()
print(digit) 
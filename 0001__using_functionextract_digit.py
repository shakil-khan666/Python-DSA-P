def extract_number(num):
    digit = []
    while num != 0:
        last_number=num%10
        digit.append(last_number)
        num = num//10
    digit.reverse()
    return digit
result= extract_number(1234)
print(result)

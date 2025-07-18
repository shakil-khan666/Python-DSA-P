def count_digit(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count


if __name__ == "__main__":
    number = 12345
    result = count_digit(number)
    print("Count:", result)


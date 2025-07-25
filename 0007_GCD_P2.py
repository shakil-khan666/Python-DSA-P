def Greatest_Common_Divisor(x1, x2):
    gcd = 1  
    for i in range(1, min(x1, x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            gcd = i  
    return gcd


print(Greatest_Common_Divisor(12, 18))  # Output: 6
print(Greatest_Common_Divisor(10, 13))  # Output: 1

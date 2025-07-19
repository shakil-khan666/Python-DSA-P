import math
def amostong_number(n: int)-> bool:
    given_number = n
    sum = 0
    while n>0:
        last_digit = int(math.fmod(n,10))**3 # power
        sum = sum+last_digit
        n= int(n//10)
    return given_number == sum

if __name__=="__main__":
    result = amostong_number(370)
    print(result)
        
    
    
def Sum_divisor(n: int)-> int:
    sum = 0
    divisor = []
    
    for i in range (1,n):
        if n%i==0:
            divisor.append(i)
            sum= sum+i 
    return divisor,sum

if __name__=="__main__":
    
    a=int(input("enter the number = "))
    divisor,sum = Sum_divisor(a)
    print(divisor)
    print(sum)
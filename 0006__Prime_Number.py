import math

def Prime_number(number):
    count=0
    pivot = int(math.sqrt(number))
    for i in range(1,pivot+1):
        if number%i==0:
            fact2=number//i
            if fact2!=i:
                count = count+2
            else:
                count=count+1
    return count ==2

if __name__ =="__main__":
    num = int(input("enter the number : "))
    result = Prime_number(num)
    print(result)
            
    
import math

def reverse_number(num:int)->int:
    result = 0
    while num :#ei khane num!=0 jei kotha num: mane same kotha
        last_number = int(math.fmod(num,10))
        result = result*10+last_number
        num = int(num//10)
    return result

if __name__ =="__main__":
    
    rev = reverse_number(1234)
    print(rev)

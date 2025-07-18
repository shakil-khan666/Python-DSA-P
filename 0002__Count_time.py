import math

def Count_digit(n:int)->int:
    power = int(math.log10(n))
    return power+1

if __name__ == "__main__":
    print(Count_digit(7486512))
    
    
    
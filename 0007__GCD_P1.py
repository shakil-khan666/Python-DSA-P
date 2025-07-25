import math

def Greatest_Common_Divisor(x1,x2):
    for i in range (min(x1,x2),0,-1): #eikhne high value theke low value t gase
        if x1%i == 0 and x2%i == 0:
            return i  

if __name__=="__main__":
    result = Greatest_Common_Divisor(15,9)
    print(Greatest_Common_Divisor(12, 18))  # Output: 6
    print(Greatest_Common_Divisor(10, 13)) 
    print(result)
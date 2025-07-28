def  eucledian_Algorithm(x,y)-> int:
    while x>0 and y>0:
        if x>y:
            x= x%y
        else:
            y=y%x
    if x == 0:
        return y
    else:
        return x

if __name__=="__main__":
    print(eucledian_Algorithm(18,9))

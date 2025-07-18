def count_digit(num):
    count = 0
    while num>0:
        num= int(num//10)
        count = count+1
    return count

result = count_digit(12345)
print("count ",result)

#time complicity=log(n) karon ei khane loop ase n pojonto 
        
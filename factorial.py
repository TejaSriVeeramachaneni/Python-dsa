def factorial(num):
    if(num==0) or (num==1):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
print(factorial(6))
print(factorial(10))



#iterative
num = 6
if(num==0 or num==1):
    print("1")
else:
    product = 1
    for i in range(1,num+1):
        product = product*i
print(product)


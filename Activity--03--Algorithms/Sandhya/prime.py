def is_prime(number):
    if(number<=1):
        return False
    for i in range(2,number):
        if(number%i)==0:
            return False
    return True
number=int(input("enter the number"))
if(is_prime(number)):
    print("number is prime",number)
else:
    print("number is not a prime",number)

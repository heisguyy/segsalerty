#1. Multiplication table
def multiplicationTable(a):
    for i in range(1,13):
        print(f"{a} x {i} = {a*i}")
number = int(input("Input a number: "))
multiplicationTable(number)

#2. twin primes
def is_prime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
for a in range(2,1000):
    if is_prime(a) and is_prime(a+2):
        print(f"{a} and {a+2} are twin primes.")

#3. list of prime factors
listOfPrime = []
def isPrime(a):
    for i in range(2,a):
        if a % i == 0:
            return False
    return True 
number = int(input("Input a number: "))
for i in range(2,number):
    if isPrime(i):
        while number % i == 0:
            print(i)
            number = number/i

#4. Filter Odd numbers out
def checkEven(a):
    if int(a) % 2 == 0:
        return True
    else:
        return False
listOfNumbers = input("Enter number with spaces in between: ")
listOfNumbers = listOfNumbers.split(" ")
filteredList = list(filter(checkEven,listOfNumbers))
print(list(map(int,filteredList)))

# 5. product of digits in a number
def prodDigits(a):
    product = 1
    for i in str(a):
        product*=int(i)
    return product
number = int(input('Enter a number: '))
print(prodDigits(number))

import numpy as np

#1. list to one dimensional array
listOfNumbers = input("Enter the numbers with space in between: ")
listOfNumbers = list(map(int,listOfNumbers.split(" ")))
print(f"list of numbers: {listOfNumbers}")
arrayOfNumbers = np.array(listOfNumbers)
print(f"Array of numbers: {arrayOfNumbers}")

#2. Creat a three dimensional array
array = np.arange(2,11)
array = array.reshape(3,3)
print(array)

#3. Update empty array
array = np.zeros(10)
print(array)
array[5] = 11
print(array)
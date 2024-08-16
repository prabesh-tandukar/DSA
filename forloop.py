import time
time.time()

timestamp1 = time.time()

#Python program to find sum of N Natrual numbers
number = 100
total = 0

for value in range (1, number + 1):
    total = total + value

print ("The sum is ", total)

#Program completed

timestamp2 = time.time()
print(timestamp2 - timestamp1)
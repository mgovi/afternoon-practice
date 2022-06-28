#Generator Excercises

#Problem 1
#Create a generator, primes_gen that generates prime numbers starting from 2.


# Expected output
# 2 3 5 7 11 13 17 19 23 29
from tkinter import N


def prime_gen():
    x = 1
    while True:
        x += 1
        for prime in range (2, x+1):
            if x == prime:
                yield x
            if x % prime == 0:
                break

gen = prime_gen()
for x in range(10):
  print(next(gen), end = ' ')

#----------------------------------------------------------------------------

#Problem 2
#Create a generator, unique_letters that generates unique letters from
#the input string. It should generate the letters in the same order as
#from the input string.

word = "hello"

unique_letters = ""

for letter in word:
    if letter not in unique_letters:
        unique_letters += letter.lower()

print(unique_letters)


# Expected output
# h e l o
for letter in unique_letters('hello'):
    print(letter, end=' ')
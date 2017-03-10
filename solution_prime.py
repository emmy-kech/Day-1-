def prime_number():
   result = []
#this iterates in the range checking for numbers that are greater than 1
   for n in range(1, 100):
       if n > 1:
#if iterates in i checking for a number that when divided by any other number returns a modulus result of 0
           for i in range(1, n+1):
               if i % n == 0:
                   result.append(n)
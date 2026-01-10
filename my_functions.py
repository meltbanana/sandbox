##03.01.2016
##get_primes(num) -> list of primes less than num
##get_factors(num) -> list of prime factors of num
##get_divisors(num) -> list of all divisors of num
##product(lst) -> get product of elements of list

from itertools import combinations

def get_primes(max):
#Sieve of Eratosthenes
	indx = [i for i in range(max+1)]

	for i in range(len(indx)):
		if i>1 and indx[i]>0:
			count = 2
			while count*i <= max: 
				indx[count*i] = 0
				count += 1
		
		#progress bar
		#if i%(max//10) == 0:
		#	print(i)
	primes = []		
	for i in indx:
		if i>1: primes.append(i)
	
	return primes

def get_factors(x):
    i = 2
    n = x
    factors = []

    while i*i <= n:
        if n%i:
             i+= 1
        else:
            n //= i
            factors.append(i)
    if n>1:
        factors.append(n)

    return(factors)

def product(lst):
    result = 1
    for n in lst:
        result *= n
    return result

def get_divisors(num):
    divisors = set()
    factors = get_factors(num)
    for c in range(1, len(factors)+1):
        for f in combinations(factors, c):
            divisors.add(product(f))
    return sorted(list(divisors))

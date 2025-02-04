def prime_factors(n):
 factors = []
 
 while n % 2 == 0:
     factors.append(2)
     n //= 2
 
 divisor = 3
 while divisor * divisor <= n:
     while n % divisor == 0:
         factors.append(divisor)
         n //= divisor
     divisor += 2
 
 if n > 2:
     factors.append(n)
 
 return factors

number = 84
result = prime_factors(number)
print(f"{number} = {', '.join(map(str, result))}")

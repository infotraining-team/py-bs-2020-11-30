# wypisz liczby pierwsze 1-100
# print(9 % 3) # modulo - reszta z dzielenia 

real_primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

primes = [1, 2]

for num in range(3, 100, 2):    
    is_prime = True           # zakładam że liczba jest pierwsza
    for i in range(2, num):   # range - prawostronnie otwarty
        if num % i == 0:      # dzielenie bez reszty
            is_prime = False
            break
    if is_prime:
        primes.append(num)

# simple testing
print("Prime testing:")
if primes == real_primes:
    print("Working ok")
else:
    print("not ok")
    

def primes(n):
    """Returns primes from 0 to n, n including"""
    primes = []
    for num in range(1, n+1):
        if is_prime(num):
            primes.append(num)            
    return primes

def is_prime(num):
    """Check if num is prime"""
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    #testing is_prime:
    real_primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    not_primes = [4, 9, 25, 81]

    for i in real_primes:
        if is_prime(i) == False:
            print(i, "is prime!!")
            raise ArithmeticError

    for i in not_primes:
        if is_prime(i) == True:
            print(i, "is not prime!!")
            raise ArithmeticError
    print("tests passed")
    print(primes(101))

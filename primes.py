# wypisz liczby pierwsze 1-100
# print(9 % 3) # modulo - reszta z dzielenia 

for num in range(2, 100):    
    if_rest_is_zero = 0
    for i in range(2, num):   # range - prawostronnie otwarty
        if num % i == 0:   # dzielenie bez reszty
            if_rest_is_zero += 1
    if if_rest_is_zero == 0:
        print(num)
    

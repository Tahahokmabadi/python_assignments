def is_prime(input_number):
    if input_number < 2:
        status = "your number is smaller than 2. a prime number is equal to or bigger than 2. so your number is not prime."
    elif input_number == 2:
        status = "number is prime."
    if input_number >= 2:
        for i in range(2,input_number):
            if (input_number % i) != 0:
                status = "number is prime."
            elif (input_number % i) == 0:
                status = "number is not prime."
                break
    return status

input_number = int(input("Enter a number: "))
print(is_prime(input_number))

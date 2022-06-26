print()
number = int(input("digit a number please: "))
print()
timer = 2
have_joined = 0
prime_factors = 0

while  number > 1000000:
    print()
    number = int(input("please, digit a number less than 1000000:  "))
    print()

first_number = number


while number !=1:
    number = number/timer
    number_float_test = int(number+1)
    last_number = number_float_test - number
    if last_number < 1:
            number = first_number
            timer = timer + 1
            have_joined = 0
    elif last_number == 1:
        have_joined = have_joined+1
        if have_joined < 2:
            prime_factors = prime_factors + 1

    first_number = number

print()
print("the total of prime factors of this number is: ", prime_factors)

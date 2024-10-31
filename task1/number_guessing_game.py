#number guessing game
secret_number = 21

while True:
    try:
        number = int(input("Between 1 and 100 guess the secret number: "))

        if 1<=number<=100:
            if number == secret_number:
                print("Yes You guessed it right, BRAVO!!")
                break
            elif 11<=number<=20:
                print("Almost, nut not correct :) TRY HARDER")
            elif 22<=number<=30:
                print("Not really, TRY AGAIN")
            else:
                print("Dont give up, Try again")
        else:
            print("Number is out of range!!")
    except ValueError:
        print("Please enter a valid number.")

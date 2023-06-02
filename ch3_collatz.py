# Creating the Collatz sequence as per the practice project in chapter 3

# Implementing the Collatz logic for a single step
def collatz(number: int):
    collatz_even = number // 2
    collatz_odd = 3 * number + 1
    if (number % 2) == 0:
        print(collatz_even)
        return collatz_even
    else:
        print(collatz_odd)
        return collatz_odd


# Requesting user input and performing the Collatz sequence. Combined steps here to also do input validation.23
def user_input(message: str, error_message: str):
    print(message)
    try:
        response = int(input())
        step = 0
        while response != 1:
            response = collatz(response)
            step += 1
        print(f"\nAcheived the Collatz sequence in {step} steps")
    except ValueError:
        print(error_message)


# Calling the function
user_input(
    "Enter a number:",
    "Error: Please enter a number."
)






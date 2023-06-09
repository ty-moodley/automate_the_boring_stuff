import random


def magic_ball() -> None:
    """
    Simulates the response from a magic 8-ball. Requests that the user enter in their question and provides answer
    :return: String response from a list of 9 possible options
    """
    input("\nWhat is your question?\n")

    messages = ['It is certain',
                'It is decidedly so',
                'Yes definitely',
                'Reply hazy try again',
                'Ask again later',
                'Concentrate and ask again',
                'My reply is no',
                'Outlook not so good',
                'Very doubtful']

    print(f"\n{random.choice(messages)}")


# Calling the function will run the game
magic_ball()

import prompt


def welcome_user():
    name = prompt.string(
        'Greetings, mysterious stranger, what is your name?: '
    )
    print(f'\nWelcome to the Brain Games {name}! Mu-ha-ha!\
            \nThere is no way out of here. Literally.')


__all__ = {
    "welcome_user",
}

import time
import random


def print_pause(s):
    print(s)
    time.sleep(2)


def intro(character):
    print_pause(
        "You find yourself standing in an open field,"
        " filled with grass and pink wild flowers."
    )
    print_pause(
        f"Rumor has it that a wicked {character} is somewhere around here,"
        "and has been terrifying the nearby village."
    )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger. \n")


def valid_input(message, options):
    while True:
        userinput = input(message).lower()
        for option in options:
            if option in userinput:
                return option
        print("Sorry, Enter a valid input from the choices laid out for you")


def field(item, character, tool):
    print_pause("Enter 1 to knock on the door of the house. \n"
                "Enter 2 to peer into the cave.\n")
    field_choice = valid_input(
        "\nWhat would you like to do? \n (Please enter 1 or 2)\n",
        ["1", "2"],
    )

    if field_choice == "2":
        cave(item, character, tool)

    else:
        print_pause("You bravely enter into the house")
        house(item, character, tool)


def cave(item, character, tool):
    print_pause("You peer into the cave.")
    if tool in item:
        print_pause(
            "You've been here before and gotten all the good stuff. "
            "It's just an empty cave now."
        )
    else:
        print_pause("It turns out to be a small cave.")
        print_pause(f"There's a magical {tool} of Ogoroth!")
        print_pause(f"You discard your silly old dagger"
                    f" and take the {tool} with you.")
        item.append(tool)
    print_pause("You walk back out to the field.")
    field(item, character, tool)


def house(item, character, tool):
    print_pause("You approach the door of the house.")
    print_pause(
        f"You are about to knock when the door opens"
        f" and out steps a {character}."
    )
    print_pause(f"Eep! This is the {character}'s house!")
    if tool in item:
        print_pause(f"The {character} attacks you!")
        fight(item, character, tool)
    else:
        print_pause(
            "You feel a bit under-prepared for this,"
            " what with only having a tiny dagger."
        )
        fight(item, character, tool)


def fight(item, character, tool):
    fight_status = valid_input(
        "Would you like to (1) fight or (2) run away? \n", ["1", "2"]
    )
    if "1" in fight_status:
        if tool in item:
            print_pause(
                f"As the {character} moves to attack,"
                f" you unsheath your new {tool}."
            )
            print_pause(f"The new {tool} shines as you brace yourself"
                        " for the attack")
            print_pause(
                f"But the {character} takes one look at your"
                " shiny new toy and runs away!"
            )
            print_pause(
                f"You have rid the town of the {character}."
                " You are victorious!"
            )
        else:
            print_pause("You do your best...")
            print_pause(f"but your dannger is no match for the {character}")
            print_pause("You have been defeated!")
        play_again()
    else:
        print_pause(
            "You run back into the field."
            " Luckily, you don't seem to have been followed"
        )
        field(item, character, tool)


def play_again():
    repeat = valid_input("Would you like to play again? (y/n)", ["y", "n"])
    if "y" in repeat:
        print_pause("Excellent! Restarting the game ...")
        main()
    else:
        print_pause("Thanks for playing! See you next time.")


def main():
    item = []
    character = random.choice(["pirate", "panda", "gorgon"])
    if character == "gorgon":
        tool = "sword"
    elif character == "panda":
        tool = "bamboo stick"
    else:
        tool = "spear"
    intro(character)
    field(item, character, tool)


main()

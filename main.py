import tabulate
from asciistuff import Lolcat, Banner
from termcolor import colored


def display_greet():
    print(Lolcat(Banner("recon tool")))
    print(colored("Made by:", "blue"), colored("@ngevorkyan & @DarkLordGeo", "yellow"))
    print(
        colored("Libraries: ", "blue"),
        colored("[colored , tabulate, asciistuff]", "yellow"),
    )
    print(
        colored("Version: ", "blue"),
        colored("1.0.0", "yellow"),
    )

    print(
        colored("Github:", "blue"),
        colored("https://github.com/ngevorkyan/Python_recon_tool.git", "cyan"),
    )
    print("\n")

    print(colored("Welcome to the python recon tool.", "yellow"))
    print(
        colored("Choose available options to get started.", "yellow"),
    )
    print("\n")


def display_menu():
    print(colored("[1]", "green"), colored("Scan website", "dark_grey"))
    print(colored("[2]", "green"), colored("Check saved scans", "dark_grey"))
    print(colored("[3]", "green"), colored("Manual", "dark_grey"))
    print(colored("[4]", "green"), colored("Exit", "dark_grey"))
    print("\n")


def user_inputs():
    user_input = input(colored("> ", "yellow"))
    print(user_input)


display_greet()
display_menu()
user_inputs()

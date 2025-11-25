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
    while True:
        user_input = input(colored("> ", "yellow"))
        print(user_input)

        if user_input == '1':
            scan_website()
            
        elif user_input == '2':
            check_saved_scans()
            
        elif user_input == '3':
            display_manual()
            
        elif user_input == '4':
            print(colored('\nExiting the program... Goodbye!', 'red'))
            
        else:
            print(colored('Try Again', 'red'))  
            
        display_menu()
        
def scan_website():
    pass

def check_saved_scans():
    pass

def display_manual():
    print(colored("\n========== RECON TOOL MANUAL ==========\n", "cyan"))

    print(colored("1. Scan website", "yellow"))
    print("   • Perform basic reconnaissance on a target URL.")
    print("   • Examples: HTTP headers, status code, IP lookup, etc.")
    print()

    print(colored("2. Check saved scans", "yellow"))
    print("   • View previously saved scan results.")
    print("   • Stored in a JSON or text file (your choice).")
    print()

    print(colored("3. Manual", "yellow"))
    print("   • Shows the help page. (You are on it right now!)")
    print()

    print(colored("4. Exit", "yellow"))
    print("   • Quit the tool.")
    print()

    print(colored("========================================\n", "cyan"))



display_greet()
display_menu()
user_inputs()



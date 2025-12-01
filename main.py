from tabulate import tabulate
from asciistuff import Lolcat, Banner
from termcolor import colored
import socket
import requests
import json
from datetime import datetime


def display_greet():
    print(Lolcat(Banner("recon tool")))
    print(colored("Made by:", "blue"), colored("@ngevorkyan & @DarkLordGeo", "yellow"))
    print(
        colored("Libraries: ", "blue"),
        colored("[colored , tabulate, asciistuff, datetime, json, requests, socket ]", "yellow"),
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
            break
            
        else:
            print(colored('Try Again', 'red'))  
            
        display_menu()
        
def scan_website():
    url = input('Input the url: ')
    
    if not url.startswith('https'):
        'https://' + url
        
    print(colored("\n[+] Scanning... Please wait...\n", "cyan"))

    try:
        #send therequest
        response = requests.get(url, timeout=10)
        #get the status
        status = response.status_code
        #find domain
        domain = url.replace('http://', '').replace('https://', '').split('/')[0]
        #find ip adress
        ip_adress = socket.gethostbyname(domain)
        #scan time
        scan_time = datetime.now()
        #data to scan
        scan_data = {
            'url':url,
            'status':status,
            'ip_address':ip_adress,
            'scan_time': scan_time.strftime("%Y-%m-%d %H:%M:%S"),
            'header':dict(response.headers),
        }
        
        #results
        print(colored("========= Scan Results =========\n", "green"))
        
        table = [
            ['URL', url],
            ['Status Code', status],
            ['Domain', domain],
            ['IP Adrress', ip_adress],
            ['Server', response.headers.get("Server", "Unknown")],
            ['Content Type', response.headers.get("Content-Type", "Unknown")],
            ['X-Powered-By', 'Unknown'],
            ['scan_time', scan_time.strftime("%Y-%m-%d %H:%M:%S")]
        ]
        
        print(tabulate(table, headers=["Field", "Value"], tablefmt="grid"))
        
        save_scan_result(scan_data)
        
    
    except Exception as e:
        print(colored(f"Error: {e}", 'red'))

def save_scan_result(data):
    try:
        with open('saved_scans.json', 'r') as file:
            saved_data = json.load(file)       
    except FileNotFoundError:
        saved_data = []
        
    saved_data.append(data)
            
    with open('saved_scans.json', 'w') as file:
        json.dump(saved_data, file, indent = 4)
        
    print(colored("[+] Scan saved to saved_scans.json\n", "green"))
            
def check_saved_scans():
    try:
        with open("saved_scans.json", 'r') as file:
            data = json.load(file)
            
        if not data:
            print(colored("No saved scans found.\n", "red")) 
            
        print(colored("\n===== SAVED SCANS =====\n", "cyan"))
        rows = []
        for entry in data:
            rows.append(
                [
                entry["url"],
                entry["status"],
                entry["ip_address"],
                entry["scan_time"]
            ]
            )
            
        print(tabulate(rows, headers=["URL", "Status Code", "IP", "Scan Time"], tablefmt="grid"))

    except FileNotFoundError:
        print(colored("No saved scans file found.\n", "red"))

def display_manual():
    print(colored("\n========== RECON TOOL MANUAL ==========\n", "cyan"))

    print(colored("1. Scan website", "yellow"))
    print("   - Perform basic reconnaissance on a target URL.")
    print("   - Examples: HTTP headers, status code, IP lookup, etc.")
    print()

    print(colored("2. Check saved scans", "yellow"))
    print("   - View previously saved scan results, stored in a JSON file.")
    print()

    print(colored("3. Manual", "yellow"))
    print("   - See the help page. (You are on it right now!)")
    print()

    print(colored("4. Exit", "yellow"))
    print("   - Quit the tool.")
    print()

    print(colored("========================================\n", "cyan"))


display_greet()
display_menu()
user_inputs()



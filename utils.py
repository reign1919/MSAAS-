# ============================================================
# MSAAS - Utilities Module
# Contains helper/utility functions
# ============================================================

import os  


def get_valid_input(prompt, min_val, max_val):
 
    while True:
        try:
            value = input(prompt)
            value = int(value)  
            
            # Range check using logical operator
            if value >= min_val and value <= max_val:
                return value
            else:
                print(f"   ⚠ Enter a number between {min_val} and {max_val}")
                
        except ValueError:
            print("   ⚠ Invalid input! Please enter a valid number.")


def get_valid_choice(prompt, min_val, max_val):

    while True:
        try:
            choice = int(input(prompt))
            
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"   ⚠ Choose between {min_val} and {max_val}")
                
        except ValueError:
            print("   ⚠ Please enter a valid number")


def pause_screen():
    input("\nPress Enter to continue...")


def clear_screen():

    
    if os.name == 'nt':
        os.system('cls')  # Windows command
    else:
        os.system('clear')  # Unix/Linux/Mac command


def get_yes_no(prompt):

    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("   ⚠ Please enter 'y' or 'n'")


def format_percentage(value):
    return f"{value:.2f}%"

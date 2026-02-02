# ============================================================
# MSAAS - Utilities Module
# Contains helper/utility functions
# ============================================================

import os  # For clear screen functionality


def get_valid_input(prompt, min_val, max_val):
    """
    Get validated integer input within a range
    Parameters:
        prompt (str): Input prompt message
        min_val (int): Minimum allowed value
        max_val (int): Maximum allowed value
    Returns:
        int: Validated integer input
    """
    while True:
        try:
            value = input(prompt)
            value = int(value)  # Type conversion
            
            # Range check using logical operator
            if value >= min_val and value <= max_val:
                return value
            else:
                print(f"   ⚠ Enter a number between {min_val} and {max_val}")
                
        except ValueError:
            print("   ⚠ Invalid input! Please enter a valid number.")


def get_valid_choice(prompt, min_val, max_val):
    """
    Get validated menu choice
    Same as get_valid_input but with different error message
    """
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
    """Pause and wait for user to press Enter"""
    input("\nPress Enter to continue...")


def clear_screen():
    """
    Clear the console screen
    Works on both Windows and Unix-based systems
    """
    # Using os.name to check operating system
    # 'nt' is Windows, 'posix' is Linux/Mac
    
    if os.name == 'nt':
        os.system('cls')  # Windows command
    else:
        os.system('clear')  # Unix/Linux/Mac command


def get_yes_no(prompt):
    """
    Get yes/no input from user
    Parameters:
        prompt (str): Question to ask
    Returns:
        bool: True for yes, False for no
    """
    while True:
        response = input(prompt + " (y/n): ").strip().lower()
        
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("   ⚠ Please enter 'y' or 'n'")


def format_percentage(value):
    """
    Format a percentage value to 2 decimal places
    Parameters:
        value (float): Percentage value
    Returns:
        str: Formatted percentage string
    """
    return f"{value:.2f}%"

# ============================================================
# MONTHLY SCHOOL ATTENDANCE AWARENESS SYSTEM (MSAAS)
# Main Program Entry Point
# Developer: Trishaan Saha (XI A)
# ============================================================

# Importing required modules
from menu import display_welcome, display_menu, display_goodbye
from attendance import enter_attendance, enter_quick_attendance
from calculator import calculate_days_needed, calculate_safe_leaves
from display import view_summary, view_daily_record, check_status, view_monthly_report
from file_handler import save_data, load_data
from utils import get_valid_choice, pause_screen, clear_screen

def main():
    """
    Main function - Entry point of the MSAAS program
    Controls the main program loop and menu navigation
    """
    # Display welcome message
    display_welcome()
    pause_screen()
    
    # Try to load existing data from file
    attendance_data = load_data()
    
    if attendance_data is not None:
        print("\n✓ Previous attendance data loaded successfully!")
    else:
        print("\n○ No previous data found. Start fresh!")
        attendance_data = None
    
    # Main program loop
    running = True
    
    while running:
        clear_screen()
        display_menu()
        
        choice = get_valid_choice("Enter your choice (1-10): ", 1, 10)
        
        # Menu option handling using if-elif-else
        if choice == 1:
            # Enter detailed attendance
            attendance_data = enter_attendance()
            if attendance_data is not None:
                save_data(attendance_data)
                
        elif choice == 2:
            # Quick attendance entry
            attendance_data = enter_quick_attendance()
            if attendance_data is not None:
                save_data(attendance_data)
                
        elif choice == 3:
            # View summary
            view_summary(attendance_data)
            
        elif choice == 4:
            # Check status against 75%
            check_status(attendance_data)
            
        elif choice == 5:
            # View day-wise record
            view_daily_record(attendance_data)
            
        elif choice == 6:
            # Calculate days needed
            calculate_days_needed(attendance_data)
            
        elif choice == 7:
            # Calculate safe leaves
            calculate_safe_leaves(attendance_data)
            
        elif choice == 8:
            # View monthly report
            view_monthly_report(attendance_data)
            
        elif choice == 9:
            # Save data manually
            if attendance_data is not None:
                save_data(attendance_data)
                print("\n✓ Data saved successfully!")
            else:
                print("\n⚠ No data to save!")
                
        elif choice == 10:
            # Exit program
            if attendance_data is not None:
                save_data(attendance_data)
            display_goodbye()
            running = False
            continue
        
        pause_screen()
    
    # End of program


# Program execution starts here
if __name__ == "__main__":
    main()

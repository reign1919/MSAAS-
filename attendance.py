# ============================================================
# MSAAS - Attendance Module
# Contains attendance entry functions
# ============================================================

from utils import get_valid_input, get_valid_choice
from menu import display_section_header

# Tuple of valid month names (immutable)
MONTH_NAMES = (
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
)

# Tuple of typical working days per month
TYPICAL_WORKING_DAYS = (22, 20, 23, 21, 22, 20, 23, 22, 21, 23, 21, 18)


def get_month_name():
    """
    Get and validate month name from user
    Returns: validated month name string
    """
    print("\nAvailable months:")
    
    # Using for loop with range
    for i in range(len(MONTH_NAMES)):
        print(f"  {i + 1}. {MONTH_NAMES[i]}")
    
    choice = get_valid_choice("\nSelect month (1-12): ", 1, 12)
    return MONTH_NAMES[choice - 1]


def enter_attendance():
    """
    Enter detailed day-wise attendance
    Returns: dictionary containing attendance data
    """
    display_section_header("ENTER DAY-WISE ATTENDANCE")
    
    # Get month name
    month_name = get_month_name()
    month_index = MONTH_NAMES.index(month_name)
    
    # Get total working days
    suggested_days = TYPICAL_WORKING_DAYS[month_index]
    print(f"\nTypical working days for {month_name}: {suggested_days}")
    
    total_days = get_valid_input(
        "Enter actual working days this month: ", 
        1, 31
    )
    
    # Initialize list to store daily attendance
    daily_record = []
    days_present = 0
    days_absent = 0
    
    print("\n" + "─" * 40)
    print("Mark attendance for each day:")
    print("  P = Present")
    print("  A = Absent")
    print("  H = Holiday (will be skipped)")
    print("─" * 40)
    
    day_number = 1
    
    # Using while loop for day entry
    while day_number <= total_days:
        valid_input = False
        
        while not valid_input:
            status = input(f"Day {day_number:2d}: ").strip().upper()
            
            # Validate input using membership operator
            if status in ['P', 'A', 'H']:
                valid_input = True
            else:
                print("   ⚠ Invalid! Enter P, A, or H")
        
        # Process based on status
        if status == 'P':
            daily_record.append('P')
            days_present += 1
            day_number += 1
        elif status == 'A':
            daily_record.append('A')
            days_absent += 1
            day_number += 1
        else:  # Holiday - skip
            print("   (Holiday - skipped)")
            total_days -= 1  # Reduce total working days
    
    # Create attendance data dictionary
    attendance_data = {
        "month": month_name,
        "total_days": total_days,
        "days_present": days_present,
        "days_absent": days_absent,
        "daily_record": daily_record,
        "entry_type": "detailed"
    }
    
    print("\n" + "═" * 40)
    print(f"✓ Attendance for {month_name} recorded!")
    print(f"  Present: {days_present} days")
    print(f"  Absent: {days_absent} days")
    print("═" * 40)
    
    return attendance_data


def enter_quick_attendance():
    """
    Quick attendance entry - just enter totals
    Returns: dictionary containing attendance data
    """
    display_section_header("QUICK ATTENDANCE ENTRY")
    
    # Get month name
    month_name = get_month_name()
    
    # Get total working days
    total_days = get_valid_input(
        "\nEnter total working days: ", 
        1, 31
    )
    
    # Get days present
    days_present = get_valid_input(
        "Enter days present: ", 
        0, total_days
    )
    
    # Calculate days absent
    days_absent = total_days - days_present
    
    # Create empty daily record (not tracked in quick mode)
    daily_record = []
    
    # Create attendance data dictionary
    attendance_data = {
        "month": month_name,
        "total_days": total_days,
        "days_present": days_present,
        "days_absent": days_absent,
        "daily_record": daily_record,
        "entry_type": "quick"
    }
    
    print("\n" + "═" * 40)
    print(f"✓ Quick entry for {month_name} recorded!")
    print(f"  Present: {days_present} / {total_days} days")
    print("═" * 40)
    
    return attendance_data

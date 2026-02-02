# ============================================================
# MSAAS - Calculator Module
# Contains all calculation functions
# ============================================================

from utils import get_valid_input
from menu import display_section_header, display_divider
import math  # Using math module

# Constants
MINIMUM_ATTENDANCE_PERCENT = 75
WARNING_THRESHOLD = 80
SAFE_THRESHOLD = 85


def calculate_percentage(days_present, total_days):
    """
    Calculate attendance percentage
    Parameters:
        days_present (int): Number of days present
        total_days (int): Total working days
    Returns:
        float: Attendance percentage rounded to 2 decimals
    """
    if total_days == 0:
        return 0.0
    
    percentage = (days_present / total_days) * 100
    return round(percentage, 2)


def calculate_required_days(target_percent, total_days):
    """
    Calculate days required to achieve target percentage
    Parameters:
        target_percent (float): Target attendance percentage
        total_days (int): Total working days
    Returns:
        int: Number of days required (rounded up)
    """
    required = (target_percent / 100) * total_days
    return math.ceil(required)  # Using math.ceil


def calculate_days_needed(data):
    """
    Calculate how many more days needed to reach 75%
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    display_section_header("DAYS NEEDED CALCULATOR")
    
    current_present = data['days_present']
    current_total = data['total_days']
    current_percent = calculate_percentage(current_present, current_total)
    
    print(f"\nCurrent Status:")
    print(f"  Present: {current_present} / {current_total} days")
    print(f"  Current %: {current_percent}%")
    
    display_divider()
    
    # Get remaining days
    remaining_days = get_valid_input(
        "Enter remaining working days in month: ", 
        0, 31
    )
    
    if remaining_days == 0:
        print("\n○ No remaining days to calculate.")
        return
    
    # Calculate projections
    new_total = current_total + remaining_days
    required_for_75 = calculate_required_days(75, new_total)
    required_for_80 = calculate_required_days(80, new_total)
    required_for_85 = calculate_required_days(85, new_total)
    
    days_needed_75 = required_for_75 - current_present
    days_needed_80 = required_for_80 - current_present
    days_needed_85 = required_for_85 - current_present
    
    # Display projections
    print("\n┌" + "─" * 46 + "┐")
    print("│" + "         ATTENDANCE PROJECTION".center(46) + "│")
    print("├" + "─" * 46 + "┤")
    print(f"│  New Total Days: {new_total}".ljust(47) + "│")
    print("├" + "─" * 46 + "┤")
    print("│  Target     │  Days Needed  │  Leaves OK   │".ljust(47) + "")
    print("├" + "─" * 46 + "┤")
    
    # For 75%
    leaves_ok_75 = remaining_days - max(0, days_needed_75)
    status_75 = "✓" if days_needed_75 <= remaining_days else "✗"
    print(f"│  75% (Min)  │  {max(0, days_needed_75):^11}  │  {max(0, leaves_ok_75):^10}  │ {status_75}")
    
    # For 80%
    leaves_ok_80 = remaining_days - max(0, days_needed_80)
    status_80 = "✓" if days_needed_80 <= remaining_days else "✗"
    print(f"│  80% (Safe) │  {max(0, days_needed_80):^11}  │  {max(0, leaves_ok_80):^10}  │ {status_80}")
    
    # For 85%
    leaves_ok_85 = remaining_days - max(0, days_needed_85)
    status_85 = "✓" if days_needed_85 <= remaining_days else "✗"
    print(f"│  85% (Good) │  {max(0, days_needed_85):^11}  │  {max(0, leaves_ok_85):^10}  │ {status_85}")
    
    print("└" + "─" * 46 + "┘")
    
    # Recommendations
    print("\n📋 Recommendation:")
    if days_needed_75 <= 0:
        print(f"   You already qualify for 75%!")
        print(f"   You can take up to {remaining_days + abs(days_needed_75)} more leaves.")
    elif days_needed_75 <= remaining_days:
        print(f"   Be present for at least {days_needed_75} of the next {remaining_days} days.")
    else:
        shortfall = days_needed_75 - remaining_days
        print(f"   ⚠ Cannot reach 75% even with full attendance.")
        print(f"   Shortfall: {shortfall} days")


def calculate_safe_leaves(data):
    """
    Calculate how many leaves can be safely taken
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    display_section_header("SAFE LEAVES CALCULATOR")
    
    current_present = data['days_present']
    current_total = data['total_days']
    
    # Get remaining days
    remaining_days = get_valid_input(
        "Enter remaining working days in month: ", 
        0, 31
    )
    
    # Get target percentage
    print("\nSelect target percentage to maintain:")
    print("  1. 75% (Minimum requirement)")
    print("  2. 80% (Safe zone)")
    print("  3. 85% (Comfortable)")
    print("  4. 90% (Excellent)")
    
    choice = get_valid_input("Your choice (1-4): ", 1, 4)
    
    # Map choice to percentage using dictionary
    target_map = {
        1: 75,
        2: 80,
        3: 85,
        4: 90
    }
    target_percent = target_map[choice]
    
    # Calculate safe leaves
    new_total = current_total + remaining_days
    required_present = calculate_required_days(target_percent, new_total)
    additional_needed = required_present - current_present
    
    safe_leaves = remaining_days - additional_needed
    
    # Display results
    print("\n┌" + "─" * 40 + "┐")
    print("│" + "     SAFE LEAVES CALCULATION".center(40) + "│")
    print("├" + "─" * 40 + "┤")
    print(f"│  Target: {target_percent}%".ljust(41) + "│")
    print(f"│  Total Days (projected): {new_total}".ljust(41) + "│")
    print(f"│  Required Present: {required_present}".ljust(41) + "│")
    print(f"│  Currently Present: {current_present}".ljust(41) + "│")
    print("├" + "─" * 40 + "┤")
    
    if safe_leaves >= 0:
        print(f"│  ✓ Safe Leaves Available: {safe_leaves}".ljust(41) + "│")
    else:
        print(f"│  ✗ No leaves available".ljust(41) + "│")
        print(f"│    Need {abs(safe_leaves)} more present days".ljust(41) + "│")
    
    print("└" + "─" * 40 + "┘")

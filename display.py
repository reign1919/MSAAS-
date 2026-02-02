# ============================================================
# MSAAS - Display Module
# Contains all display/output functions
# ============================================================

from calculator import calculate_percentage, MINIMUM_ATTENDANCE_PERCENT
from menu import display_section_header, display_divider

def view_summary(data):
    """
    Display attendance summary
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    percentage = calculate_percentage(data['days_present'], data['total_days'])
    
    display_section_header("ATTENDANCE SUMMARY")
    
    print()
    print("┌" + "─" * 40 + "┐")
    print(f"│  Month: {data['month']}".ljust(41) + "│")
    print("├" + "─" * 40 + "┤")
    print(f"│  Total Working Days  : {data['total_days']:>10}".ljust(41) + "│")
    print(f"│  Days Present        : {data['days_present']:>10}".ljust(41) + "│")
    print(f"│  Days Absent         : {data['days_absent']:>10}".ljust(41) + "│")
    print("├" + "─" * 40 + "┤")
    print(f"│  Attendance %        : {percentage:>9}%".ljust(41) + "│")
    print(f"│  Entry Type          : {data['entry_type'].title():>10}".ljust(41) + "│")
    print("└" + "─" * 40 + "┘")
    
    # Visual bar representation
    bar_length = 30
    filled = int((percentage / 100) * bar_length)
    empty = bar_length - filled
    
    print()
    print("  Progress: [" + "█" * filled + "░" * empty + f"] {percentage}%")


def check_status(data):
    """
    Check if attendance meets 75% requirement
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    percentage = calculate_percentage(data['days_present'], data['total_days'])
    
    display_section_header("75% STATUS CHECK")
    
    print()
    print("┌" + "─" * 44 + "┐")
    print(f"│  Your Attendance    : {percentage:>8}%".ljust(45) + "│")
    print(f"│  Required Minimum   : {MINIMUM_ATTENDANCE_PERCENT:>8}%".ljust(45) + "│")
    print("├" + "─" * 44 + "┤")
    
    # Status check using conditional statements
    if percentage >= 90:
        status = "EXCELLENT"
        message = "Outstanding attendance! Keep it up!"
        symbol = "★★★"
    elif percentage >= 85:
        status = "VERY GOOD"
        message = "Great attendance record!"
        symbol = "★★☆"
    elif percentage >= 80:
        status = "GOOD"
        message = "Good, but aim higher!"
        symbol = "★☆☆"
    elif percentage >= 75:
        status = "SATISFACTORY"
        message = "Just meeting the requirement."
        symbol = "✓"
    else:
        status = "CRITICAL"
        message = "Below minimum! Take action now!"
        symbol = "⚠"
    
    print(f"│  Status: {status} {symbol}".ljust(45) + "│")
    print(f"│  {message}".ljust(45) + "│")
    print("├" + "─" * 44 + "┤")
    
    # Difference from 75%
    diff = percentage - 75
    
    if diff >= 0:
        print(f"│  ✓ You are {diff:.2f}% ABOVE the minimum".ljust(45) + "│")
    else:
        print(f"│  ✗ You are {abs(diff):.2f}% BELOW the minimum".ljust(45) + "│")
    
    print("└" + "─" * 44 + "┘")


def view_daily_record(data):
    """
    Display day-wise attendance record
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    # Check if daily record exists
    if len(data['daily_record']) == 0:
        print("\n⚠ No day-wise record available!")
        print("  (Use 'Day-wise Entry' for detailed tracking)")
        return
    
    display_section_header(f"DAY-WISE RECORD - {data['month'].upper()}")
    
    record = data['daily_record']
    total_days = len(record)
    
    print()
    print("┌" + "─" * 44 + "┐")
    
    # Display in rows of 7 days (like a week)
    row_count = 0
    line = "│  "
    
    # Using nested loop concept
    for i in range(total_days):
        day_num = i + 1
        status = record[i]
        
        if status == 'P':
            line += f"D{day_num:02d}:✓ "
        else:
            line += f"D{day_num:02d}:✗ "
        
        row_count += 1
        
        # New line after every 5 days
        if row_count == 5 or i == total_days - 1:
            line = line.ljust(45) + "│"
            print(line)
            line = "│  "
            row_count = 0
    
    print("├" + "─" * 44 + "┤")
    print(f"│  ✓ Present: {data['days_present']} days".ljust(45) + "│")
    print(f"│  ✗ Absent:  {data['days_absent']} days".ljust(45) + "│")
    print("└" + "─" * 44 + "┘")
    
    # Legend
    print("\n  Legend: ✓ = Present, ✗ = Absent")


def view_monthly_report(data):
    """
    Display comprehensive monthly report
    Parameters:
        data (dict): Attendance data dictionary
    """
    if data is None:
        print("\n⚠ No attendance data found! Please enter data first.")
        return
    
    percentage = calculate_percentage(data['days_present'], data['total_days'])
    
    display_section_header("MONTHLY ATTENDANCE REPORT")
    
    print()
    print("╔" + "═" * 50 + "╗")
    print("║" + f"  ATTENDANCE REPORT - {data['month'].upper()}".ljust(50) + "║")
    print("╠" + "═" * 50 + "╣")
    print("║" + " " * 50 + "║")
    print("║" + "  STATISTICS".ljust(50) + "║")
    print("║" + f"  ├─ Total Working Days  : {data['total_days']}".ljust(50) + "║")
    print("║" + f"  ├─ Days Present        : {data['days_present']}".ljust(50) + "║")
    print("║" + f"  ├─ Days Absent         : {data['days_absent']}".ljust(50) + "║")
    print("║" + f"  └─ Attendance          : {percentage}%".ljust(50) + "║")
    print("║" + " " * 50 + "║")
    print("╠" + "═" * 50 + "╣")
    
    # Status determination
    if percentage >= 75:
        status_line = "  STATUS: ✓ ELIGIBLE (Meets 75% requirement)"
    else:
        status_line = "  STATUS: ✗ NOT ELIGIBLE (Below 75%)"
    
    print("║" + status_line.ljust(50) + "║")
    print("║" + " " * 50 + "║")
    
    # Recommendations using list
    recommendations = []
    
    if percentage < 75:
        recommendations.append("Improve attendance immediately")
        recommendations.append("Avoid taking any more leaves")
    elif percentage < 80:
        recommendations.append("Maintain current attendance")
        recommendations.append("Limit leaves to emergencies only")
    elif percentage < 90:
        recommendations.append("Good job! Keep it up")
        recommendations.append("You have some buffer for leaves")
    else:
        recommendations.append("Excellent attendance!")
        recommendations.append("You're setting a great example")
    
    print("╠" + "═" * 50 + "╣")
    print("║" + "  RECOMMENDATIONS".ljust(50) + "║")
    
    # Using for loop to iterate through list
    for i in range(len(recommendations)):
        print("║" + f"  • {recommendations[i]}".ljust(50) + "║")
    
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")

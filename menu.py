# ============================================================
# MSAAS - Menu Module
# Contains all menu display functions
# ============================================================

def display_welcome():
    """Display the welcome screen with project information"""
    print()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "   MONTHLY SCHOOL ATTENDANCE AWARENESS SYSTEM (MSAAS)".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " " * 58 + "║")
    print("║" + "   Developed By: Trishaan Saha".center(58) + "║")
    print("║" + "   Class: XI A".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║" + " " * 58 + "║")
    print("║" + "   A tool to track and analyze your school attendance".center(58) + "║")
    print("║" + "   Stay informed. Stay regular. Stay successful.".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "═" * 58 + "╝")


def display_menu():
    """Display the main menu options"""
    print()
    print("┌" + "─" * 50 + "┐")
    print("│" + "          MAIN MENU".center(50) + "│")
    print("├" + "─" * 50 + "┤")
    print("│  1. Enter Attendance (Day-wise)".ljust(51) + "│")
    print("│  2. Quick Entry (Total Days)".ljust(51) + "│")
    print("│  3. View Attendance Summary".ljust(51) + "│")
    print("│  4. Check 75% Status".ljust(51) + "│")
    print("│  5. View Day-wise Record".ljust(51) + "│")
    print("│  6. Calculate Days Needed".ljust(51) + "│")
    print("│  7. Calculate Safe Leaves".ljust(51) + "│")
    print("│  8. View Monthly Report".ljust(51) + "│")
    print("│  9. Save Data".ljust(51) + "│")
    print("│  10. Exit".ljust(51) + "│")
    print("└" + "─" * 50 + "┘")


def display_goodbye():
    """Display goodbye message when exiting"""
    print()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 50 + "║")
    print("║" + "   Thank you for using MSAAS!".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("║" + "   Remember:".center(50) + "║")
    print("║" + "   • Regular attendance = Academic success".center(50) + "║")
    print("║" + "   • Plan your leaves wisely".center(50) + "║")
    print("║" + "   • Stay above 75% always".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("║" + "   Goodbye! See you next time.".center(50) + "║")
    print("║" + " " * 50 + "║")
    print("╚" + "═" * 50 + "╝")
    print()


def display_section_header(title):
    """Display a section header with given title"""
    print()
    print("┌" + "─" * 48 + "┐")
    print("│" + title.center(48) + "│")
    print("└" + "─" * 48 + "┘")


def display_divider():
    """Display a simple divider line"""
    print("─" * 50)

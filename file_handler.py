# ============================================================
# MSAAS - File Handler Module
# Contains file reading and writing functions
# ============================================================

# File name constant
DATA_FILE = "attendance_data.txt"


def save_data(data):
    """
    Save attendance data to a text file
    Parameters:
        data (dict): Attendance data dictionary
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open file in write mode
        file = open(DATA_FILE, "w")
        
        # Write each piece of data on a new line
        file.write(data['month'] + "\n")
        file.write(str(data['total_days']) + "\n")
        file.write(str(data['days_present']) + "\n")
        file.write(str(data['days_absent']) + "\n")
        file.write(data['entry_type'] + "\n")
        
        # Write daily record as comma-separated string
        daily_str = ",".join(data['daily_record'])
        file.write(daily_str + "\n")
        
        # Close the file
        file.close()
        
        return True
        
    except Exception as e:
        print(f"\n⚠ Error saving data: {e}")
        return False


def load_data():
    """
    Load attendance data from text file
    Returns:
        dict: Attendance data dictionary, or None if file doesn't exist
    """
    try:
        # Open file in read mode
        file = open(DATA_FILE, "r")
        
        # Read all lines
        lines = file.readlines()
        
        # Close the file
        file.close()
        
        # Check if file has enough data
        if len(lines) < 6:
            return None
        
        # Parse data from lines
        month = lines[0].strip()
        total_days = int(lines[1].strip())
        days_present = int(lines[2].strip())
        days_absent = int(lines[3].strip())
        entry_type = lines[4].strip()
        
        # Parse daily record
        daily_str = lines[5].strip()
        if daily_str:
            daily_record = daily_str.split(",")
        else:
            daily_record = []
        
        # Create and return dictionary
        attendance_data = {
            "month": month,
            "total_days": total_days,
            "days_present": days_present,
            "days_absent": days_absent,
            "daily_record": daily_record,
            "entry_type": entry_type
        }
        
        return attendance_data
        
    except FileNotFoundError:
        # File doesn't exist yet
        return None
    except Exception as e:
        print(f"\n⚠ Error loading data: {e}")
        return None


def delete_data():
    """
    Delete the saved data file
    Returns:
        bool: True if successful, False otherwise
    """
    import os  # Import os module for file operations
    
    try:
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)
            return True
        return False
    except Exception as e:
        print(f"\n⚠ Error deleting data: {e}")
        return False

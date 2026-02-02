# MSAAS - Monthly School Attendance Awareness System
A Python-based console application to track student attendance and ensure 75% minimum attendance compliance.


**The following code file has not been altered logically; it has only been formatted using AI for better readability and compliance with the teacher’s guidelines.**


## Project Structure
```
MSAAS_Python_Project/
├── main.py          # Entry point - run this file
├── menu.py          # Menu display functions
├── attendance.py    # Attendance data entry
├── calculator.py    # Percentage & projection calculations
├── display.py       # Summary & report display
├── file_handler.py  # Save/load data to file
├── utils.py         # Input validation utilities
└── attendance_data.txt  # Auto-generated data file
```
## How to Run (manual, non-git)
1. Click on GREEN "CODE" button
2. Click download zip folder
3. Extract folder
4. Open terminal in the folder
5. Run:
   python main.py
## Features
- **Enter Attendance**: Day-wise (P/A/H) or quick totals entry
- **View Summary**: See current percentage and 75% eligibility status
- **Projections**: Calculate days needed to reach target percentage
- **Safe Leaves**: Know how many leaves you can take and stay above 75%
- **Data Persistence**: Saves attendance to file for future sessions
## Concepts Used
| Concept | Usage |
|---------|-------|
| Functions | 15+ user-defined functions across modules |
| Lists | Daily attendance tracking ('P', 'A', 'H') |
| Dictionaries | Session data storage |
| Tuples | Month metadata (days per month) |
| Loops | Menu navigation, data entry |
| File I/O | Save/load attendance records |
| Modules | math, os (standard library) |
## Sample Output
```
╔══════════════════════════════════════╗
║   ATTENDANCE AWARENESS SYSTEM        ║
╠══════════════════════════════════════╣
║  Current: 18/25 days (72.0%)         ║
║  Status: ⚠ BELOW 75% TARGET          ║
║  Days needed: 3 more present days    ║
╚══════════════════════════════════════╝
```
## Authors
School Project - Trishaan Saha 
```

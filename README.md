# Car Parking Management System

A simple console-based parking lot manager written in Python. Built as a first-semester Python project.

## Overview

The program helps a parking attendant manage a small parking lot with a fixed number of slots. It records which cars are parked and who owns them, prevents overbooking and duplicate entries, and calculates the parking bill when a car leaves. All data is stored in memory using a Python dictionary (car number -> owner name).

## Features

- Park a car (car number and owner name)
- Remove a car and generate the bill automatically (hours x rate)
- Show all currently parked cars
- Search for a car by its number
- Check total, filled and empty slots
- Blocks parking when the lot is full (10 slots)
- Detects duplicate car numbers (case-insensitive, e.g. `mh12ab1234` = `MH12AB1234`)
- Simple numbered menu that repeats until the user exits

## Technologies / Tools Used

- Python 3
- Built-in features only: dictionaries, functions, loops, conditionals, `input()` / `print()`
- No external libraries
- Any editor or IDE (IDLE, VS Code, PyCharm)

## Steps to Install and Run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.
2. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd <repository-folder>
   ```
3. Run the program:
   ```bash
   python parking.py
   ```
   (On some systems use `python3 parking.py`.)
4. Choose options 1 to 6 from the menu. Choose `6` to exit.

## Configuration

Two values at the top of `parking.py` can be changed:

| Variable | Default | Meaning |
|----------|---------|---------|
| `total_slots` | 10 | Maximum number of cars |
| `rate_per_hour` | 20 | Charge in Rs per hour |

## Instructions for Testing

Testing is manual. Run the program and try the cases below.

| # | Test | Steps | Expected result |
|---|------|-------|-----------------|
| 1 | Park a car | Option 1, enter `MH12AB1234`, `Rahul` | "Car parked successfully!" and slots left = 9 |
| 2 | Duplicate car | Park `mh12ab1234` again | "This car is already parked!" |
| 3 | Lot full | Park 10 different cars, then try an 11th | "Sorry, parking is full!" |
| 4 | Show cars | Option 3 | Numbered list of parked cars and owners |
| 5 | Search (found) | Option 4, enter a parked car number | "Car is parked. Owner is ..." |
| 6 | Search (not found) | Option 4, enter an unknown number | "Car is not in the parking." |
| 7 | Check slots | Option 5 | Total, filled and empty slot counts |
| 8 | Remove and bill | Option 2, enter a parked car, `3` hours | Owner shown, "Total bill: Rs 60", car removed |
| 9 | Remove missing car | Option 2, enter an unknown number | "Car not found!" |
| 10 | Invalid menu choice | Enter `9` | "Wrong choice, try again." |

## Screenshots

_Add screenshots of the program running here (optional but recommended), for example:_

```
![Main menu](screenshots/menu.png)
![Parking a car](screenshots/park.png)
![Bill generation](screenshots/bill.png)
```

### Sample run

```
===== CAR PARKING MANAGEMENT =====

1. Park a car
2. Remove a car
3. Show all cars
4. Search a car
5. Check empty slots
6. Exit
Enter your choice: 1
Enter car number: mh12ab1234
Enter owner name: Rahul
Car parked successfully!
Slots left: 9
```

## Known Limitations

- Data is lost when the program closes (no file or database storage).
- Non-numeric or negative hours are not validated when removing a car.
- Empty car numbers or owner names are accepted.

## Future Improvements

- Input validation with `try/except`
- Automatic time tracking using the `datetime` module
- Saving records to a file or database
- Different rates for different vehicle types

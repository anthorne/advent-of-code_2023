# Advent of Code 2023 - Day 1
import os
import time
import colorama
from colorama import Fore, Back, Style, Cursor

# Initialization
colorama.init(autoreset=True)
os.system('cls')    # Clear terminal window - Windows only
calibration_values = []


def print_row(row, y):
    # Locate digits and the position in the row
    first_digit = [-1, -1]    # [digit, position]
    last_digit = [-1, -1]
    pos = 0
    for c in row:
        if c.isdigit() and first_digit[0] == -1:
            first_digit[0] = int(c)
            first_digit[1] = pos
        if c.isdigit():
            last_digit[0] = int(c)
            last_digit[1] = pos
        print(Fore.GREEN + Style.BRIGHT + str(c), end='', flush=True)
        time.sleep(0.01)
        pos += 1

    # Light up the calibration values
    counter = 0
    left = 1
    right = len(row)
    for p in range(len(row)):
        if counter % 2 == 0:
            if (left-1) == first_digit[1] or (left-1) == last_digit[1]:
                print(Fore.WHITE + Back.BLACK + Cursor.POS(left, y) + row[left-1], end='', flush=False)
            else:
                print(Fore.GREEN + Back.BLACK + Style.DIM + Cursor.POS(left, y) + row[left-1], end='', flush=False)
            left += 1
        else:
            if (right-1) == first_digit[1] or (right-1) == last_digit[1]:
                print(Fore.WHITE + Back.BLACK + Cursor.POS(right, y) + row[right-1], end='', flush=True)
            else:
                print(Fore.GREEN + Back.BLACK + Style.DIM + Cursor.POS(right, y) + row[right-1], end='', flush=True)
            right -= 1
        counter += 1
        time.sleep(0.01)

    # Move the values to the right
    frame = '(    )'
    print(Cursor.POS(60, y), end='', flush=True)
    for c in frame:
        print(Fore.GREEN + Back.BLACK + Style.DIM + c, end='', flush=True)
        time.sleep(0.01)
    print(Cursor.POS(62, y), end='', flush=True)
    print(Fore.WHITE + Back.BLACK + str(first_digit[0]), end='', flush=True)
    time.sleep(0.05)
    print(Fore.WHITE + Back.BLACK + str(last_digit[0]), end='', flush=True)
    time.sleep(0.05)
    print('')
    calibration_value = int(str(first_digit[0]) + str(last_digit[0]))
    return first_digit, last_digit, calibration_value


def main():
    # Read input
    data = []
    file = open('d1_input.txt')
    for row in file:
        data.append(row.strip())
    file.close()
    # data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]  # Example data

    # Parse lines and locate calibration values
    row_count = 1
    for r in data:
        # print row one char at a time and get the calibration values
        first, last, calibration_value = print_row(r, row_count)
        calibration_values.append(calibration_value)
        row_count += 1

    # Sum the calibration values
    part_1 = 0
    for cal in calibration_values:
        part_1 += cal
    part_one_text = '\n Part one - The sum of all calibration values: ' + str(part_1)
    for c in part_one_text:
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + c, end='', flush=True)
        time.sleep(0.01)
    print('')


if __name__ == '__main__':
    main()

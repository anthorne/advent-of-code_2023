# Advent of Code 2023 - Day 1 - Part Two
import os
import time
import colorama
from colorama import Fore, Back, Style, Cursor
import re

# Initialization
colorama.init(autoreset=True)
os.system('cls')    # Clear terminal window - Windows only
calibration_values = []
timer = True


def identify_numbers(text):
    # Define a regular expression pattern to match numbers
    pattern = re.compile(fr"(?=(one|two|three|four|five|six|seven|eight|nine|\+))", flags=re.IGNORECASE)

    # Find all matches in the text along with their starting positions
    match_pos = [match.start() for match in pattern.finditer(text)]     # [0, 4, 7]
    match_text = pattern.findall(text)                                  # ['eight', 'two', 'three']
    result = []
    for i in range(len(match_pos)):
        result.append([match_pos[i], match_text[i]])
    return result                                                       # [[0, 'eight'], [4, 'two'], [7, 'three']]


def get_digit(written):
    text_numbers = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9]]
    for n in text_numbers:
        if written == n[0]:
            return n[1]
    return -1


def print_row(row, y):
    # Identify numbers written in text
    text_numbers = identify_numbers(row)

    # Print out the row
    pos = 0
    for c in row:
        print(Fore.GREEN + Style.BRIGHT + str(c), end='', flush=True)
        if timer:
            time.sleep(0.01)
        pos += 1

    # Highlight the written numbers
    for w in text_numbers:          # w = [0, 'eight']
        print(Cursor.POS(w[0]+1, y), end='', flush=False)
        for l in w[1]:
            print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + str(l), end='', flush=False)
            if timer:
                time.sleep(0.1)

    # Exchange written numbers with actual digits
    # new_row = str(row)
    for w in text_numbers:  # w = [0, 'eight']
        print(Cursor.POS(w[0] + 1, y), end='', flush=False)
        digit = get_digit(w[1])
        row = str(row[:w[0]]) + str(digit) + str(row[w[0] + 1:])
        first = True
        for l in w[1]:
            if first:
                print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + str(digit), end='', flush=False)
                first = False
                if timer:
                    time.sleep(0.05)
            else:
                print(Fore.GREEN + Back.BLACK + Style.DIM + str(l), end='', flush=False)
                if timer:
                    time.sleep(0.05)

    # Locate digits and the position in the row
    first_digit = [-1, -1]    # [digit, position]
    last_digit = [-1, -1]
    pos = 0
    print(Cursor.POS(0, y), end='', flush=True)
    for c in row:
        if c.isdigit() and first_digit[0] == -1:
            first_digit[0] = int(c)
            first_digit[1] = pos
        if c.isdigit():
            last_digit[0] = int(c)
            last_digit[1] = pos
        print(Fore.GREEN + Style.BRIGHT + str(c), end='', flush=True)
        if timer:
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
        if timer:
            time.sleep(0.01)

    # Move the values to the right
    frame = '(    )'
    print(Cursor.POS(60, y), end='', flush=True)
    for c in frame:
        print(Fore.GREEN + Back.BLACK + Style.DIM + c, end='', flush=True)
        if timer:
            time.sleep(0.01)
    print(Cursor.POS(62, y), end='', flush=True)
    print(Fore.WHITE + Back.BLACK + str(first_digit[0]), end='', flush=True)
    if timer:
        time.sleep(0.05)
    print(Fore.WHITE + Back.BLACK + str(last_digit[0]), end='', flush=True)
    if timer:
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
    # data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]     # Example data

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
    part_one_text = '\n Part two - The sum of all calibration values: ' + str(part_1)
    for c in part_one_text:
        print(Fore.YELLOW + Back.BLACK + Style.BRIGHT + c, end='', flush=True)
        if timer:
            time.sleep(0.01)
    print('')


if __name__ == '__main__':
    main()

import re

def sum_calibration_values(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            digits = re.findall('\d', line)
            if digits:
                total += int(digits[0] + digits[-1])
    return total

print(sum_calibration_values('input.txt'))
#!/usr/bin/env python3
def is_leap_year(y):
    if not isinstance(y, int):
        raise TypeError("is_leap_year only handles integers")
    if y < 0:
        raise ValueError("is_leap_year only handles positive integers")
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    return y % 400 == 0

def main():
    year = None
    while year is None:
        try:
            year = int(input("Enter a year: "))
        except Exception as e:
            print("Please input an integer year")

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()

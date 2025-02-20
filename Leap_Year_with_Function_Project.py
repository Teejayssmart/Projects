# define a function
year = int(input("Enter year: "))


def leap_year_detector():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return " This is leap year"
            else:
                return "This is not a leap year"
        else:
            return "This is leap year"

    else:
        return "not a leap year"



print(leap_year_detector())

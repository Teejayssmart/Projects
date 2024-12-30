
def leap_year_detector(year):

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

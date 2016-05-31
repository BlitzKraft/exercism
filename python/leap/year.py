
def is_leap_year(num):
    if num % 4 == 0:
        if num % 100 != 0 or num % 400 == 0:
            return True
    return False

def run(year: int) -> bool:
    is_leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    return is_leap_year


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)

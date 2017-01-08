from blacklist import load_blacklist
import re


def check_register(password):
    # the use of both upper-case and lower-case letters (case sensitivity)
    if not password.isupper() and not password.islower():
        return 1
    else:
        return 0


def check_numbers(password):
    # inclusion of one or more numerical digits
    if not password.isdigit():
        unicnumber_of_digit = len(set([x for x in password if x.isdigit()]))
        if unicnumber_of_digit >= 3:
            return 2
        else:
            return 1
    return 0


def check_special_characters(password):
    # inclusion of special characters, such as @, #, $
    if not password.isalnum():
        return 2
    else:
        return 0


def find_in_blacklist(password, blacklist):
    # prohibition of words found in a password blacklist
    if password in blacklist:
        return 0
    else:
        return 1


def check_len_and_uniqueness(password):
    if len(password) >= 12 and len(set(password)) >= 6:
        return 2
    elif len(password) >= 6 and len(set(password)) >= 3:
        return 1
    else:
        return 0


def check_letters(password):
    if not password.isalpha() and len(set([x for x in password if x.isdigit()])) > 1:
        return 1
    else:
        return 0


def check_personal_info(password):
    """ prohibition of words found in the user's personal information,
    prohibition of passwords that match the format of calendar dates,
    license plate numbers, telephone numbers, or other common numbers """
    formats = {'date': '([0-9]{1,4}[\\/.\s]?){3}',
               'license plate': '[A-z]{1}[0-9]{3}[A-z]{2}[0-9]{0,3}',
               'phone': '\+?[0-9\-()\s]+',
               'email': '\w+\@\w+\.\w+'}
    for name, pattern in formats.items():
        if re.compile(pattern).fullmatch(password):
            return 0
    return 1


def get_password_strength(password):
    strength = 0
    strength += check_register(password)
    strength += check_numbers(password)
    strength += check_special_characters(password)
    strength += find_in_blacklist(password, load_blacklist())
    strength += check_len_and_uniqueness(password)
    strength += check_letters(password)
    strength += check_personal_info(password)
    return strength

if __name__ == '__main__':
    user_password = input("Input your password :  ")
    if user_password:
        print("strength:", get_password_strength(user_password))
    else:
        print("you have not entered a password")
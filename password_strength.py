from blacklist import load_blacklist
from easygui import passwordbox, msgbox
import re


def check_register(password):
    if not password.isupper() and not password.islower():
        return 1
    else:
        return 0


def check_numbers_and_uniqueness(password, unique_number_of_digit=3):
    if not password.isdigit():
        real_unicnumber_of_digit = len(set([x for x in password if x.isdigit()]))
        if real_unicnumber_of_digit >= unique_number_of_digit:
            return 2
        else:
            return 1
    return 0


def check_special_characters(password):
    if not password.isalnum():
        return 2
    else:
        return 0


def find_in_blacklist(password, blacklist):
    if password in blacklist:
        return 0
    else:
        return 1


def check_len_and_uniqueness(password, best_len=12):
    if len(password) >= best_len and len(set(password)) >= best_len/2:
        return 2
    elif len(password) >= best_len/2 and len(set(password)) >= best_len/4:
        return 1
    else:
        return 0


def check_letters_and_uniqueness(password, unique_number_of_letter=1):
    if not password.isalpha() and len(set([x for x in password if x.isalpha()])) > unique_number_of_letter:
        return 1
    else:
        return 0


def check_personal_info(password):
    formats = {'date': '([0-9]{1,4}[\\/.\s]?){3}',
               'license plate': '[A-z]{1}[0-9]{3}[A-z]{2}[0-9]{0,3}',
               'phone': '\+?[0-9\-()\s]+',
               'email': '\w+\@\w+\.\w+',
               'repetition': '(\S)\\1{2,}',
               'to_small': '\S{1,3}',
               }
    for name, pattern in formats.items():
        if re.compile(pattern).fullmatch(password):
            return 0
    return 1


def get_password_strength(password):
    strength = 0
    strength += check_register(password)
    strength += check_numbers_and_uniqueness(password, 3)
    strength += check_special_characters(password)
    strength += find_in_blacklist(password, load_blacklist())
    strength += check_len_and_uniqueness(password, 12)
    strength += check_letters_and_uniqueness(password, 1)
    strength += check_personal_info(password)
    return strength

if __name__ == '__main__':
    user_password = passwordbox("Input your password :")
    print(get_password_strength(user_password))
    if user_password:
        msgbox("Ваш пароль оценивается на:" + str(get_password_strength(user_password)),
               "Оценка пароля по 10 бальной системе", "OK", '')
    else:
        msgbox("Пароль не был введен",
               "Оценка пароля по 10 бальной системе", 'OK', '')
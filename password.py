#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:33:45 2018

@author: michaelcasper
"""

# Strong password detector to check if following conditions are met:
#    Quantity Condition: At least 8 characters
#    Case Condition: Contains both uppercase and lowercase letters
#    Digit Condition: Contains at least one digit

# User is prompted to input their desired password, which will be checked
# against the above three conditions.

To use, call create_strong_password() function

import re


def create_strong_password():
    """ Ask user to create a password, which will then be checked against
    the three conditions.
    """
    password = input('Create a password: ')
    print()
    if is_password_strong(password) is True:
        print('Congratulations, "{0}" is a strong password indeed.'
              .format(password))
        return password
    else:
        yes_no = input('Try again? (Y/N) ')
        if yes_no == 'Y' or yes_no == 'y':
            create_strong_password()
        else:
            print('O.K.')
            return None


def is_password_strong(password):
    """ Checks if the three conditions are True. """
    false_count = 0
    if pass_quantity_condition(password) is False:
        false_count += 1
        print('Pssword must be at least 8 characters long.')
    if pass_case_condition(password) is False:
        false_count += 1
        print('Password must contain uppercase and lowercase letters.')
    if pass_digit_condition(password) is False:
        false_count += 1
        print('Password must contain at least one digit.')
    if false_count != 0:
        return False
    else:
        return True


def pass_quantity_condition(password):
    """ Checks if password contains at least 8 characters. """
    quantityRegex = re.compile(r'.{8,}')
    try:
        quantityRegex.search(password).group()
        return True
    except AttributeError:
        return False


def pass_case_condition(password):
    """ Checks if password contains both upper and lowercase letter. """
    onlyletters = re.sub(r'\W|\d', '', password)
    lowercaseRegex = re.compile(r'.*[a-z]+.*')
    uppercaseRegex = re.compile(r'.*[A-Z]+.*')
    try:
        lowercaseRegex.search(onlyletters).group()
        uppercaseRegex.search(onlyletters).group()
        return True
    except AttributeError:
        return False


def pass_digit_condition(password):
    """ Checks if password contains at least one digit. """
    digitRegex = re.compile(r'.*\d+.*')
    try:
        digitRegex.search(password).group()
        return True
    except AttributeError:
        return False

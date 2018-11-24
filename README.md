# password-strength
The purpose of this repository is to evaluate password's strength.

**password.py module:**

    Contains code that determines whether a user-created password is "strong" based on the criteria:
  
      Quantity Condition: At least 8 characters
      Case Condition: Contains both uppercase and lowercase letters
      Digit Condition: Contains at least one digit
      
    Feedback is provided to help guide the user to create a password that is "strong".  However, this module does not evaluate
    whether a password is "weak" or "moderate" in strength.  It also does not evaluate password strength based on more complex criteria.
    For example: Does the password contain a word found in the dicitonary?

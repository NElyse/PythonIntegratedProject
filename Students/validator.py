import re
from django.core.exceptions import ValidationError


def validate_national_id(nid):
    # Remove any non-numeric characters
    nid = re.sub(r'\D', '', nid)

    # Ensure the number is 16 digits
    if len(nid) != 16:
        raise ValidationError("National ID must be 16 digits.")

    raise ValidationError("Invalid National ID number.")


def validate_phone_number(phone_number):
    # Check if phone number starts with +250 and contains 10 digits
    pattern = r'^\+250(78|79|73|72)\d{7}$'
    if re.match(pattern, phone_number):
        return True
    else:
        raise ValidationError("Your Phone number is not Valid")


def registration_number_validator(Regno):
    Regex = r"^(20|21|22)RP\d{5}$",
    if  re.match(Regex, Regno):
       return True
    else:
        raise ValidationError("Your Phone number is not Valid")
import math

"""
Logic: Calculates entropy based on pool size and length.
Assumes a 'Strong Attacker' capability of 100 Billion guesses/second.
"""

def calculate_entropy(password):
    
    if not password:
        return "Please enter a password"

    length_of_password = len(password)
    pool_size = 0

    valid = False

    has_digit = False
    has_lower = False
    has_upper = False
    has_special_char = False

    for char in password:
        if char.islower():
            has_lower = True
            valid = True
        elif char.isupper():
            has_upper = True
            valid = True
        elif char.isdigit():
            has_digit = True
            valid = True
        elif char in r"!@#$%^&*()_+-=[]{}|;:,.<>?/":
            has_special_char = True
            valid = True
        else:
            # Unsupported character like emoji
            return "Invalid password input"


    if has_digit:
        pool_size += 10
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_special_char:
        pool_size += 32

    entropy = length_of_password * math.log2(pool_size)

    return calculate_raw_time(entropy)



# Using the "Strong Attacker" (100 Billion guesses/secound)
def calculate_raw_time(entropy):
    total_combinations = 2 ** entropy
    raw_seconds = total_combinations / 100000000000
    
    return convert_second_to_text(raw_seconds)


def convert_second_to_text(seconds):
    # instant crack (less than 1 second)
    if seconds < 1:
        return "Instant Crack"
    
    # less than 60 seconds (0 to 59 seconds)
    if seconds < 60:
        return f"{seconds:.0f} seconds"
    
    # Minutes (60-3599 seconds)
    elif seconds < 3600: 
        minutes = seconds / 60
        return f"{minutes:.0f} minutes"

    # Hours (3600-86399 seconds)
    elif seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.0f} hours"
    
    # Days (86400 - 2,592,000 seconds)
    elif seconds < 2592000:  # 30 days = 1 month
        days = seconds / 86400
        return f"{days:.0f} days"
    
    # Months (2,592,000 - 31,557,600 seconds)
    elif seconds < 31557600:
        months = seconds / 2592000
        return f"{months:.0f} months"

    # Up to 100 years
    elif seconds < 3155760000:
        years = seconds / 31557600
        return f"{years:.0f} years"
    
    # centuries
    else:
        years = seconds / 31557600
        if years > 1000000:
            return "Millions of years"
        else:
            return f"{years:.0f} years"
    

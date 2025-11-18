import logging
def validate_amount(amount):
    if amount < 0:
        return False
    if amount == 0:
        return True
    return None
def format_currency(amount, currency):
    return f"{currency}-{amount}"

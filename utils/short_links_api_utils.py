def check_days_actual_value(days:int):
    if 1 > days or days > 366:
        return False
    return True



def clean_boolean(item=None):
    if item is not None:
        if isinstance(item, str):
            return True if item == 'true' else False
        elif isinstance(item, bool):
            return item
    return False


def clean_int(value, default=None):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def clean_float(value, default=None):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

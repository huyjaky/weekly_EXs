

def calc(x, is_int = False):
    try:
        if (is_int == False): float(x)
        else: int(x)

    except ValueError:    
        return False
    return True

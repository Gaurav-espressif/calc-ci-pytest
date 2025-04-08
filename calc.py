def _validate_operands(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")

def add(a, b):
    _validate_operands(a, b)
    return a + b

def sub(a, b):
    _validate_operands(a, b)
    return a - b

def mul(a, b):
    _validate_operands(a, b)
    return a * b

def div(a, b):
    _validate_operands(a, b)
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def power(a, b):
    _validate_operands(a, b)
    return a ** b


"""
def add(a,b):
    if a is None or b is None:
        return None
    return a+b

def sub(a,b):
    if a is None or b is None:
        return None
    return a-b

def mul(a,b):
    if a is None or b is None:
        return None
    return a*b

def div(a, b):
    if a is None or b is None:
        return None
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def power(a,b):
    if a is None or b is None:
        return None
    return a**b

"""
"""
def add(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")
    return a + b

def sub(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")
    return a - b

def mul(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")
    return a * b

def div(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def power(a, b):
    if a is None or b is None:
        return None
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")
    return a ** b

"""
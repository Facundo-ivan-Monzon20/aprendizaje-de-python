def square(value):
    """Return the square of a value."""

    return value ** 2

result = square(4)

print(result)

def raise_to_power(value1,value2):
    """Raise value1 to the power of value2."""
    
    return value1 ** value2

def raise_both(value1,value2):
    
    """Raise value1 to the power of value2 and vice versa.
    """
    
    return value1 ** value2, value2 ** value1


result2 = raise_both(2,3)

print(result2)
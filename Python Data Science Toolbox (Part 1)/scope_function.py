def mod2plus5(x1,x2,x3):
    """Returns the remainder plus 5 of three values.

    Args:
        x1 (_type_): _description_
        x2 (_type_): _description_
        x3 (_type_): _description_
    """
    
    def inner(x):
        return x % 2 + 5
    
    return (inner(x1),inner(x2),inner(x3))


print(mod2plus5(1,2,3))

def raise_val(x):
    """Return the inner function."""
    
    def inner(n):
        """Returns la potencia n de cualquier numero x
        """
        raised = x ** n
        return raised
    
    return inner

square = raise_val(2)
cube = raise_val(3)

print((square(2),cube(3)))

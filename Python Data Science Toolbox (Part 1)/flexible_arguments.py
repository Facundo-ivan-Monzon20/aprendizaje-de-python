
# recibe la cantidad de argumentos que se quiera y los tranforma en una tupla
from pickletools import int4


def add_all(*args):
    """sum all"""
    
    
    sum_all = 0
    
    for sum in args:
        
        sum_all += sum
    
    return sum_all


print(add_all(10,10))
print(add_all(10))
print(add_all(10,10,10,10,10))


#imprimimos clave-valor
#recibe las claves y argumentos que se quiera
def print_all(**kwargs):
    """print the key-value"""
    
    for key,value in kwargs.items():
        
        if(type(value) == int):
            value = str(value)
            
        print(key +': '+ value)



print_all(name="Facundo",last_name="Monzón", years=23)
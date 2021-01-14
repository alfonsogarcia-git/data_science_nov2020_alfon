"""
__name__:
1) Tiene el valor del string "__main__" si se ejecuta ese fichero
2) Tiene el valor del nombre del fichero si se esta importando

"""

from a import x
import numpy as np

#Code
x()

# Main es una variable que existe por defecto en python

print("-----------")
print("Ejecución de 'name_main'")
if __name__ == "__main__":
    print("name de 'name_main':")
    print(__name__)
    print("EQ")
print("Fin de ejecución de 'name_main'")
print("----------")
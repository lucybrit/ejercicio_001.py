

from math import pi


class Cilindro:

    def __init__ (self, radio, altura):
        self.radio=radio
        self.altura=altura

    def __str__ (self):
        return f"El area del cilindro es igual a {((pi*self.radio)**2 * self.altura)}"

c1=(Cilindro(10,20))

print  (c1)






    




class Polynomial:
  # method to initialize the object with some values
  def __init__(self, *coefs):
    self.coefs = coefs

  # function to represent the object (print) 
  # similar to __str__ but for debuging purposes
  # it will be used if no __str__ method 
  def __repr__(self):
    return 'Polynomial(*{!r})'.format(self.coefs)
  
  # method to add two objects of this class
  def __add__(self,other):
    return Polynomial(*(x+y for x,y in zip(self.coefs,other.coefs)))

  # method to evaluate the Polynomial
  # can be used to implement a funcion based on the class
  def __call__(self, number):
    v = 0 
    for expo in self.coefs:
      v+= number**expo
    return v


p1 = Polynomial( 1, 2, 3)
p2 = Polynomial(3, 4, 3)
print(p1+p2)
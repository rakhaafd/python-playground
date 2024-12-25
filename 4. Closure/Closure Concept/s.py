def closure_calc():
  a = 2
  def mult(x):
    return a * x
  return mult
  
c = closure_calc()
print(c(1),c(2),c(3))
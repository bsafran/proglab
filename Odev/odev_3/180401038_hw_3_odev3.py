"""
@author : Berat Safran
Numara : 180401038
180401038 % 4 Değerinin Sonucu = 2
Kullanılan olasılık : 2. Poisson Distribution
"""
from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

x = Symbol('x')
lam =Symbol('lambda' )

"""
# Lambda bir olayın kaç kez gerçekleştiğinin ortalamasıdır. Bu değere bakarak başka bir olayın 
olma olasılığını çıkartıldığı grafiktir.
"""
value1 = ((lam**x)*sym.exp(-lam))
value2 = sym.factorial(x)

possibility = value1/value2 #Olasılığın hesaplanması
pprint(possibility)

syp.plot(possibility.subs({lam:5}),(x,0,10),title="Poisson Distribution")
plt.show() # Sympy Grafiği

x_value=[]
y_value=[]
for value in range(12):
    y=possibility.subs({lam:5,x:value}).evalf()
    y_value.append(y)
    x_value.append(value)
plt.plot(x_value,y_value)
plt.show() #Matplotlib Grafiği
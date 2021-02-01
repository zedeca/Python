import math

i1=input(str('Enter a (Coefficient of x²): ') )
i2=input(str('Enter b (Coefficient of x) : ') )
i3=input(str('Enter c (Constant Term)    : ') )

try:
    a=float(i1)
    b=float(i2)
    c=float(i3)
except:
    print('Error: Please Enter Numbers as Coefficients Only!')
    quit()
    
D = (b*b)-(4*a*c)
FD=math.sqrt(D)
PD= (-(math.sqrt(D)))
Alpha =(FD/2*a)-(b/2*a)
Beta = (PD/2*a)-(b/2*a)

def Sol():
    print('\nQuadratic Polynomial/Equation:', str(i1)+'x² +', str(i2)+'x +', str(i3))
    print('\nFirst Zero/Root of Quadratic Equation is:', Alpha)
    print('Second Zero/Root of Quadratic Equation is:', Beta)

if D>0:
    print('\nNature Of Roots/Zeroes: Real and Distinct')
    Sol()

elif D==0:
    print('\nNature Of Roots: Real and Equal')
    Sol()

elif D<0:
    print('\nNature Of Roots: Imaginary and Complex')

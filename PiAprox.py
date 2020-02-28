import random
import numpy as np
import matplotlib.pyplot as plt
import math
import time

def CalculatePi(n):
    numTotalPoints = 0
    numCirclePoints = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if((x**2 + y**2) < 1):
            numCirclePoints+=1
            plt.scatter(x,y,s=10,c='blue')
        else:
            plt.scatter(x,y,s=10,c='red')    
        numTotalPoints+=1
        
    return 4*(numCirclePoints/numTotalPoints)         

x = np.linspace(0.0, 1.0, 20)
y = np.linspace(0.0, 1.0, 20)
X, Y = np.meshgrid(x,y)
F = X**2 + Y**2 - 1.0
fig, ax = plt.subplots()
ax.contour(X,Y,F,[0])
ax.set_aspect(1)
plt.xlim(0,1)
plt.ylim(0,1)
plt.grid(linestyle='--')
plt.suptitle('Pi aproximation using random points ratio', fontsize=8)

k = int(input("Introduce un numero de iteraciones "))
piAprox = CalculatePi(k)
relaviteError = (abs(piAprox - math.pi)/math.pi)*100
print("El valor aproximado de pi es " + str(piAprox) + " se ha cometido un error de " + str(relaviteError) + " %")
plt.title("Pi obtained value: " + str(piAprox) +" Error: " + str(float("{0:.2f}".format(relaviteError))) + " %" )
plt.show()
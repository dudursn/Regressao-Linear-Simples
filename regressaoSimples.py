'''
Regressão Linear Simples
'''
from math import sqrt

def valorDeTeta1(x, y):
    sxy = somatorio_x_y(x,y)
    sxx = somatorio_x_x(x)
    sx = somatorio(x)
    sy = somatorio(y)
    n = len(x)
    return (n*sxy - sx*sy)/ (n*sxx - sx**2)

def valorDeTeta0(teta1):
    sx = somatorio(x)
    sy = somatorio(y)
  
    return (sy - teta1*sx)/len(x)

def expressaoDaFuncaoDeHipotese(teta1,teta0):
    print ("y(x) = %.2f * x + %.2f" % (teta1, teta0))

def funcaoHipotese(x, teta1,teta0):
    return teta0+teta1*x

#Quanto mais próximo de 1 ou de -1 mais forte a relação
def correlacaoLinearEntreAsVariaveis(x, y):
    sxy = somatorio_x_y(x,y)
    sxx = somatorio_x_x(x)
    syy = somatorio_x_x(y)
    sx = somatorio(x)
    sy = somatorio(y)
   
    n = len(x)
    r = (n*sxy - sx*sy)/ sqrt((n*sxx - sx**2)*(n*syy - sy**2))
    return r

def somatorio(valores):
    soma = 0.0
    for e in valores:
        soma += e

    return soma

def somatorio_x_y(x, y):
    soma = 0.0
    for i in range(len(x)):
        soma += x[i]*y[i]
    return soma

def somatorio_x_x(x):
    soma = 0.0
    for i in range(len(x)):
        soma += x[i]**2 
    return soma
    
'''
x = [1,2,3,4,5,6]
y = [2,4,6,8,10,12]
x_teste = 15
'''
x = [71.0,64.0,43.0,67.0,56.0,73.0,68.0,56.0,76.0,65.0,45.0,58.0,45.0,53.0,49.0,78.0,73.0,68.0]
y = [82.0,91.0,100.0,68.0,87.0,73.0,78.0,80.0,61.0,84.0,116.0,76.0,97.0,100.0,105.0,77.0,73.0,78.0]


x_med = somatorio(x)/len(x)
y_med = somatorio(y)/len(y)


teta1 = valorDeTeta1(x,y)
teta0 = valorDeTeta0(teta1)
expressaoDaFuncaoDeHipotese(teta1, teta0)

x_teste = 60
print("Teste: x =",str(x_teste))
print(funcaoHipotese(x_teste, teta1,teta0))

print("Correlacao linear")
print(correlacaoLinearEntreAsVariaveis(x,y))

import matplotlib.pyplot as plt
import numpy as np
x_np = np.array(x)
y_np = np.array(y)
plt.plot(x_np, y_np, 'ro')
plt.xlabel('Idade')
plt.ylabel('Massa Muscular')
plt.title('Diagrama de dispersão')
plt.grid(True)
plt.savefig("test.png")
plt.show()

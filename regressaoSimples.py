'''
Regressão Linear Simples
'''
from math import sqrt

def valorDeTeta1(x, y, x_med, y_med):
    sxy = somatorio_x_y(x,y)
    sxx = somatorio_x_x(x)
    n = len(x)
    return (sxy - n*x_med*y_med)/ (sxx - n*(x_med**2))

def valorDeTeta0(teta1, x_med, y_med):
    return y_med - teta1*x_med

def expressaoDaFuncaoDeHipotese(teta1,teta0):
    print ("h(x) = %.2f * x + %.2f" % (teta1, teta0))

def funcaoHipotese(x, teta1,teta0):
    return teta0+teta1*x

#Quanto mais próximo de 1 ou de -1 mais forte a relação
def correlacaoLinearEntreAsVariaveis(x, y, x_med, y_med):
    sxy = somatorio_x_y(x,y)
    sxx = somatorio_x_x(x)
    syy = somatorio_x_x(y)
    n = len(x)
    r = (sxy - n*x_med*y_med)/ sqrt((sxx - n*x_med**2)*(syy - n*y_med**2))
    return r

def media(valores):
    soma = 0.0
    for e in valores:
        soma += e

    return soma/len(valores)

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
y = [82.0,91.0,100.0,68.0,87.0,73.0,78.0,80.0,65.0,84.0,116.0,76.0,97.0,100.0,105.0,77.0,73.0,78.0]


x_med = media(x)
y_med = media(y)

teta1 = valorDeTeta1(x,y,x_med,y_med)
teta0 = valorDeTeta0(teta1, x_med, y_med)
expressaoDaFuncaoDeHipotese(teta1, teta0)

x_teste = 50
print("Teste: x =",str(x_teste))
print(funcaoHipotese(x_teste, teta1,teta0))

print("Correção linear")
print(correlacaoLinearEntreAsVariaveis(x,y, x_med, y_med))
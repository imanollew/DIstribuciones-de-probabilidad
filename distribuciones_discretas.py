import matplotlib.pyplot as plt
import numpy as np



def ObtenerBernoulli(P,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Bernoulli(P)
		listaResultado.append(valor)
	return listaResultado



def Bernoulli(P):
	n=np.random.rand(1,1)
	lista=n[0]
	if(lista[0]>=P):
		return 1
	else:
		return 0

def ObtenerGeometrica(P,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Geometrica(P)
		listaResultado.append(valor)
	return listaResultado

def Geometrica(P):
	contador=0
	exito=0
	while(exito==0):
		exito=Bernoulli(P)
		contador=contador+1
	return contador

def ObtenerBinomial(N,P,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Binomial(N,P)
		listaResultado.append(valor)
	print(listaResultado)
	return listaResultado

def Binomial(N,P):
	cantidadExitos=0
	for indice in range(N):
		valor=Bernoulli(P)
		if (valor==1):
			cantidadExitos=cantidadExitos+1
	return cantidadExitos

def ObtenerPascal(M,P,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Pascal(M,P)
		listaResultado.append(valor)
	return listaResultado

#cuantas veces se tiro la moneda hasta M exitos
def Pascal(M,P):
	contadorExitos=0
	exito=1
	intentos=0
	while(contadorExitos!=M):
		if(exito==Bernoulli(P)):
			contadorExitos=contadorExitos+1
		intentos=intentos+1
	return intentos

def ObtenerHipergeometrica(B,R,K,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Hipergeometrica(B,R,K)
		listaResultado.append(valor)
	return listaResultado

def Hipergeometrica(B,R,K):
	contadorBolasRetiradas=0
	exito=1
	cantidadExitos=0
	while(contadorBolasRetiradas!=K):
		if(exito==Bernoulli(B/(B+R))):
			B=B-1
			cantidadExitos=cantidadExitos+1
		else:
			R=R-1
		contadorBolasRetiradas=contadorBolasRetiradas+1
	return cantidadExitos
	
cantidadValores=1000
listaResultado=[]
P=0.5
N=10 #se usa en la geometrica
M=3 #se usa en la pascal
B=7 #se considera exito si sale B
R=15
K=10

#listaResultado=ObtenerBernoulli(P,cantidadValores)
#listaResultado=ObtenerGeometrica(P,cantidadValores)
#listaResultado=ObtenerBinomial(N,P,cantidadValores)
#listaResultado=ObtenerPascal(M,P,cantidadValores)
listaResultado=ObtenerHipergeometrica(B,R,K,cantidadValores) #blue, red, k=cantidad de bolitas que sacas
plt.hist(listaResultado, normed=True, bins=50)
plt.show()

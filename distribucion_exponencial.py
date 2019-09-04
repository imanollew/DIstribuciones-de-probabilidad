import numpy as np
import matplotlib.pyplot as plt

def Exponencial(lambd):
	n=np.random.rand(1,1)
	lista=n[0]
	y=lista[0]
	return (-((np.log(1-y)))/lambd)

def ObtenerExponencial(lambd,cantidadValores):
	listaResultado=[]
	for indice in range(cantidadValores):
		valor=Exponencial(lambd)
		listaResultado.append(valor)
	return listaResultado


cantidadValores=1000
lambd=1
listaResultado=ObtenerExponencial(lambd,cantidadValores)
plt.hist(listaResultado, normed=True, bins=50)
plt.show()
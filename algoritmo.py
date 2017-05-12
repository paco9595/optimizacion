global datos;
global cap;
global pesos;
global prom_pesos;
global prom_cap;
global pre_mochila;
pre_mochila=[]
prom_cap=[]
datos=[]
cap=0
prom_pesos=[]
def prom(lista):
    promedio=0.0
    aux=0.0
    for x in range(len(lista)):
        aux+=lista[x]
    #print aux
    promedio=aux/len(datos)
    return promedio
def suma():
    global sumas
    sumas=[]
    aux=0
    for x in range(len(datos)):
        for y in range(len(datos[x])):
            aux+=datos[x][y]
        sumas.append(aux)
        aux=0
    print sumas
def leerDatos():
    line=0;
    aux=[]
    suma=""
    cap=0
    archivo = open("1000_25/1000_25_1.txt", "r")
    for linea in archivo.readlines():
        for x in linea:
        	if x!= " " and x!="\n":
                    if line>=1:
                        suma+=x;
                    else:
                        line+=1
                        
        	else:
                    if line>=1 and (len(suma)>0):
                        aux.append(int(suma))
                        suma=""
        if(len(aux)>0):
            if len(datos)<1000:
            	#print aux
            	datos.append(aux)
            	aux=[]
            else:
                if cap==0:
                    cap=aux[0]
                    aux=[]
                else:
                    pesos=aux
                    aux=[]
    return pesos
def rellenar():
    for x in range(len(datos)):
        for y in range(len(datos[x])):
            if len(datos[x])<1000:
                datos[x].append(0)
            else:
                break
    #print len(datos[500])


def pre(lista):
    disponibles=[0]*len(datos)
    prom_pesos=prom(lista)
    for x in range(len(datos)-1):
        #print datos[x]
        prom_cap.append(prom(datos[x+1]))
        if(prom_cap[x]!=0):
            disponibles[x]=1
    #print prom_cap
    #print len(prom_cap)
    #print disponibles
    #while cap<:
     #   pass


pesos=leerDatos()
rellenar()
suma()
pre(pesos)
global datos;
global cap;
global pesos;
global prom_pesos;
global prom_cap;
global pre_mochila;
global disponibles;
pre_mochila=[]
prom_cap=[]
datos=[]
cap=0
prom_pesos=[]
disponibles=[]
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
    #print sumas
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
def validar(objeto):
    if objeto+100<=cap:
        return True
    else:
        return False
def mejores(lista):
    print disponibles
    i=0
    aux=[]
    valido=True
    for x in range(10):
        while valido:
            i=lista.index(max(lista))
            if disponibles[i]==0:
                lista[i]=0
                aux.append(i)
                valido=False
    print aux
        
def pre(lista):
    prePeso=0
    sinCambios=0
    disponibles=[0]*len(datos)
    prom_pesos=prom(lista)
    for x in range(len(datos)-1):
        prom_cap.append(prom(datos[x+1]))
    mejores(lista)
    #while prePeso<cap and sinCambios<10:
     #   for x in range():
      #      pass

pesos=leerDatos()
rellenar()
suma()
pre(pesos)
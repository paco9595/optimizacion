global datos;
global cap;
global pesos;
global prom_pesos;
global prom_cap;
global pre_mochila;
global disponibles;
global pesos_Selecionados;
pesos_Selecionados=[]
pre_mochila=[]
prom_cap=[]
datos=[]
cap=0
prom_pesos=[]
disponibles=[]
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
def prom(lista):
    promedio=0.0
    aux=0.0
    for x in range(len(lista)):
        aux+=lista[x]
    #print aux
    promedio=aux/len(datos)
    return promedio
def mejores(lista,disponibles):
    #print disponibles
    i=0
    aux=[]
    #print disponibles
    for x in range(10):
        #print max(lista)
        i=lista.index(max(lista))
        if disponibles[i]==0:
            aux.append(i)
            pesos_Selecionados.append(lista[i])
            disponibles[i]=1    
        lista[i]=0 
    print aux
    return aux
def validar(objeto):
    if objeto+100<=cap:
        return True
    else:
        return False
def convertir(lista,selecionados):
    aux=[]
    print lista
    print pesos_Selecionados
    print lista[16]
    for x in range(len(selecionados)):
        aux.append(lista[selecionados[x]])
    print aux 
    return aux
def meter(selecionados,lista):
    #print 'hola',lista
    aux=[]
    alfa=0.4
    valores=convertir(lista,selecionados)
    num_max=max(valores)
    num_min=min(valores) 
    #print num_max,num_min  
    criterio= num_min+ (alfa*(num_max-num_min))
    print criterio 
    #print lista
    for x in range(len(selecionados)):
        print selecionados[x], lista[selecionados[x]]
        if lista[selecionados[x]]<=criterio:
            #print selecionados[x]
            aux.append(lista[selecionados[x]+1])
    #print aux
def constructor(lista):
    #print lista
    prePeso=0
    sinCambios=0
    disponibles=[0]*len(datos)
    prom_pesos=prom(lista)
    for x in range(len(datos)-1):
        prom_cap.append(prom(datos[x+1]))
    selecionados=mejores(lista,disponibles)
    meter(selecionados,lista)
pesos=leerDatos()
rellenar()
suma()
constructor(pesos)
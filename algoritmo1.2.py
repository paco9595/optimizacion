global beneficio
global pesos
global beneficio_individaules
global mochila
global ceros
ceros=[]
mochila=[0]*1000
beneficio=[]
pesos=[]
beneficio_individaules=[]
def leerdatos(): 
    global pesos
    global beneficio
    global count
    count=0
    line=0
    aux=[]
    suma=""
    cap=0
    datos=[]
    cunt=0
    archivo = open("prueba.txt", "r")
    for linea in archivo.readlines():
        for x in linea:
            if x!= " " and x!="\n":
                    if line>=1:
                        suma+=x
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
            else:
                if cap==0:
                    cap=aux[0]
                else:
                    pesos=aux
        aux=[]
    aux=[]
    #print datos
    pesos=datos.pop()
    cap= datos.pop()
    datos.pop()
    datos.pop(0)
    for x in range(len(datos)):
        print datos[x]
    #print 'cap',cap
    #print 'pesos',pesos
    aux=[]
    
    for x in range(len(datos)):
        for y in range(x):
            datos[x].insert(0,0)
        print datos[x],len(datos[x])
    for x in range(len(datos)): 
        for y in range(len(datos[x])):
             if x==y:
                 print 'cor',x,y
                 aux.append(datos[x][y])
             if y<x:
                 print 'cor',y,x
                 aux.append(datos[y][x])
             if x<y:
                 print 'cor',x,y
                 aux.append(datos[x][y])
        beneficio.append(aux)
        aux=[]
    for x in range(len(beneficio)):
        print beneficio[x]
    print len(beneficio)
def prom(l):
    return sum(l, 0.0) / (len(l)-l.count(0))

leerdatos()


#print beneficio
#print pesos

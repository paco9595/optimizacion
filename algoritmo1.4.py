import random
import sys
global beneficio
global id_selecionados_posibles
global ben_selecionados
global pesos_selecionados
id_selecionados_posibles=[]
ben_selecionados=[]
pesos_selecionados=[]
beneficio=[]
def leerdatos():
    global pesos
    global beneficio
    global count
    global cap
    count=0
    line=0
    aux=[]
    suma=""
    datos=[]
    cunt=0
    cant=0
    #num=sys.argv[1]
    archivo = open("prueba.txt", "r")
    #print len(archivo.readlines())
    for linea in archivo.readlines():
        for x in linea:
            if x!=" " and x!='\n':
                suma+=x
            else:
                if x==0 and  (len(suma)>0):
                    cant=int(suma)
                    suma=""
                else:
                    if (len(suma)>0):
                        aux.append(int(suma))
                        suma=""
        if(len(aux)>0):
            datos.append(aux)
        aux=[]
    #print datos
    pesos=datos.pop()
    cap= datos.pop()
    cap=cap[0]
    datos.pop()
    datos.pop(0)
    print 'cap',cap
    aux=[]
    for x in range(len(datos)):
        for y in range(x):
            datos[x].insert(0,0)
    for x in range(len(datos)):
        for y in range(len(datos[x])):
             if x==y:
                 aux.append(datos[x][y])
             if y<x:
                 aux.append(datos[y][x])
             if x<y:
                 aux.append(datos[x][y])
        beneficio.append(aux)
        aux=[]
    #print len(beneficio

def prom(l):

    if (len(l)-l.count(0))!=0:
        return suma(l) / (len(l)-l.count(0))
    else:
        return 0
def suma(l):
    return sum(l, 0.0)
def constructor():
    prom_ben=[]
    for x in range(len(beneficio)):
        prom_ben.append(prom(beneficio[x]))
    print 'prom_ben', prom_ben
leerdatos()
for x in range(len(beneficio)):
    print beneficio[x]
print 'pesos',pesos

constructor()

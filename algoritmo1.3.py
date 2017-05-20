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
    num=sys.argv[1]
    archivo = open("1000_25/1000_25_"+num+".txt", "r")
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
        return sum(l,0.0) / (len(l)-l.count(0))
    else:
        return 0
def suma(l):
    return sum(l, 0.0)

def elegir():
    global id_selecionados_posibles
    global ben_selecionados
    global pesos_selecionados
    id_selecionados_posibles=[]
    ben_selecionados=[]
    pesos_selecionados=[]
    prom_ben=[]
    prom_ben_total=0
    prom_peso=[]
    peso_aux=0
    paso=True
    i=0
    for x in range(len(beneficio)):
        prom_ben.append(prom(beneficio[x]))
    while len(id_selecionados_posibles)<=5 and i<10:
        prom_ben_total=prom(prom_ben)
        prom_peso=prom(pesos)
        #print 'primer while'
        for x in range(len(beneficio)):
            if len(id_selecionados_posibles)<5:
                if  mochila[x]==0 and prom_ben[x]>prom_ben_total :# pesos[x]+peso_aux<cap:
                    #cor.append(x)
                    aux=beneficio[x].index(max(beneficio[x]))
                    #print aux
                    while paso:
                        print 'primer segundo'
                        aux=beneficio[x].index(max(beneficio[x]))
                        #print aux
                        if ben_selecionados.count(beneficio[x][aux])>=1 or (mochila[aux]==0 and pesos[aux]+peso_aux<cap):
                            paso=False
                            if x==aux:
                                id_selecionados_posibles.append([x,-1]) #si es cerro es que el mismo id
                                ben_selecionados.append(beneficio[x][aux])
                                beneficio[x][aux]==0
                            else:
                                id_selecionados_posibles.append([x,aux])# si es diferente es que es otro id
                                ben_selecionados.append(beneficio[x][aux])
                                beneficio[x][aux]==0
                                #mochila[x]=1
                                #mochila[aux]=1
                            prom_ben[x]=prom
                        else:
                            beneficio[x][aux]==0
                        if len(beneficio[x])==beneficio[x].count(0):
                            break
                        beneficio[x][aux]==0
                        prom_ben[x]=prom(beneficio[x])
                    paso=True
            else:
                break
        i+=1
        prom_ben=[]
    i=0
def constructor():
    global id_selecionados_posibles
    global pesos_selecionados
    global ben_selecionados
    peso_aux=0 
    for x in range(5):
        elegir()
        print x, id_selecionados_posibles
        ran =random.choice(id_selecionados_posibles)
        mochila[1]=1
        #print ran
        if ran[1]!=-1:
            mochila[ran[1]]=1
            print x,pesos[ran[0]]
        else:
            print x,pesos[ran[0]], paso[ran[0]]



leerdatos()
global mochila
mochila=[0]*len(beneficio)
constructor()
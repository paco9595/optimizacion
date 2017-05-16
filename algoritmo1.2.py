import random
import sys
global beneficio
global pesos
global beneficio_individaules
global mochila
global ceros
global selecionaos
global dentro
global cont
global peso_cap
global cap
global pesos_selecionados
pesos_selecionados=[]
cap=0
peso_cap=0
cont=0
ceros=[]
mochila=[0]*1000
beneficio=[]
pesos=[]
beneficio_individaules=[]
selecionaos=[]
dentro=[]
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
    #print len(beneficio)
def prom(l):
    if (len(l)-l.count(0))!=0:
        return sum(l, 0.0) / (len(l)-l.count(0))
    else:
        return 0
def suma(l):
    return sum(l, 0.0)   
def preSelecion():
    peso_cap=0
    global cont
    global cap
    global pesos_selecionado
    promedios_ben=[]
    prom_general=0
    promedios_peso=prom(pesos)
    
    pesos_selecionado=[]
    aux=[]
    for x in range(len(beneficio)):
        promedios_ben.append(prom(beneficio[x]))
    prom_general=prom(promedios_ben)
    print 'prom',prom_general
    for x in range(len(promedios_ben)):     
        if promedios_ben[x]>prom_general and mochila[x]==0 and peso_cap+pesos[x]<cap:
            id_obj= beneficio[x].index(max(beneficio[x]))
            if promedios_peso>pesos[x] and mochila[id_obj]==0 and promedios_peso>pesos[id_obj]: 
                if x==id_obj:
                    selecionaos.append([x,0])
                    peso_cap+=pesos[x]
                    pesos_selecionado.append(x)
                else:
                    selecionaos.append([x,1])
                    selecionaos.append([id_obj,-1])
                    peso_cap+=(pesos[x]+id_obj)
                    pesos_selecionado.append(x)
                    pesos_selecionado.append(id_obj)
                mochila[x]=1
                mochila[id_obj]=1
            pesos[x]=0
            pesos[id_obj]=0
                #beneficio[x][id_obj]=0
            beneficio[x][id_obj]=0
    '''print len(promedios_ben)
    print promedios_peso
    print prom_general
    print len(selecionaos)'''
    #print selecionaos
    #print 'pesos' ,len(pesos_selecionado)
    #print 'selec',len(selecionaos)
    cont+=1
def constructor():
    global cont
    global selecionaos
    global pesos_selecionado
    global cap
    global peso_cap
    aux=[]
    contador=0
    v=True
    peso_cap=0
    #print 'cap d',cap
    #print 'peso_cap',peso_cap
    while  contador<10:
        while len(selecionaos)<=5:
            preSelecion()
        #print 'selec',selecionaos
        while v:
            id_Sel=random.choice(selecionaos)
            if dentro.count(id_Sel[0])==0:
                if pesos_selecionado[selecionaos.index(id_Sel)]+peso_cap<cap:
                    #print 'print id',pesos_selecionado[selecionaos.index(id_Sel)]
                    contador=0
                    pesos_selecionado[selecionaos.index(id_Sel)]+peso_cap
                    v=False
                else:
                    contador+=1
            else:
                contador+=1
                if contador>=10:
                    break
        if contador<10:
            if id_Sel[1]==1:
                dentro.append(id_Sel[0])
                aux=selecionaos[(selecionaos.index(id_Sel))+1]
                dentro.append(aux[0])
                mochila[id_Sel[0]]=1
                mochila[aux[0]]=1
                #peso_cap+=selecionaos.index(id_Sel))+1
            elif id_Sel[1]==-1:  
                aux=selecionaos[(selecionaos.index(id_Sel))-1] 
                dentro.append(id_Sel[0])
                dentro.append(aux[0])
                mochila[id_Sel[0]]=1
                mochila[aux[0]]=1
            elif id_Sel[0]==0:
                dentro.append(id_Sel[0])
                mochila[id_Sel[0]]=1
            #selecionaos=[]
            v=True
        else:
            break
leerdatos()
#print pesos
todo=[]
while len(todo)<10:
    constructor()
    '''while suma(dentro)>=cap:
        dentro.pop()'''
    print 'pesos',pesos_selecionado
    print dentro,suma(dentro)
    todo.append(dentro)

    for x in range(len(dentro)):
        print 'hola',pesos_selecionado[dentro[x]]
    dentro=[]


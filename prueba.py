import random
import sys
from random import randint
global beneficio
global id_selecionados_posibles
global ben_selecionados
global pesos_selecionados
global mochila
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
    archivo = open("1000_25/1000_25_4.txt", "r")
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
def selecion():
    global mochila
    prom_ben=[]
    prom_total=0
    prom_pesos=0
    posibles=[]
    mayor_que_prom=[]
    for x in range(len(beneficio)):
        prom_ben.append(prom(beneficio[x]))# se saca el promedio de beneficios por casa objeto
    #print 'prom_ben', prom_ben
    prom_total=prom(prom_ben)
    prom_pesos=prom(pesos)
    #print 'prom_pesos',prom_pesos
    for x in range(len(beneficio)):
        for y in range(len(beneficio[x])):
            if beneficio[x][y]>=prom_total:
                mayor_que_prom.append([x,y])
    while len(posibles)<5:
        while True:
            cor=mayor_que_prom[randint(0,len(mayor_que_prom)-1)]
            if mochila[cor[0]]==0 and mochila[cor[1]]==0:
                posibles.append([cor[0],cor[1]])
                break

        #print 'objeto',beneficio[obj_x][obj_y]
    #print 'posibles',posibles
    return posibles
def constructor():
    global sosluciones
    global mochila
    peso_mochila=0
    sosluciones=[]
    selecionados=[]
    count=0
    while len(sosluciones)<10:
        while cap>peso_mochila and count<5:
            while True and count<5:
                candidado=random.choice(selecion())
                if cap>peso_mochila+pesos[candidado[0]]+pesos[candidado[1]]:
                    #print 'pesos',pesos[candidado[0]],pesos[candidado[1]]
                    mochila[candidado[0]]=1
                    mochila[candidado[1]]=1
                    selecionados.append(candidado)
                    peso_mochila+=pesos[candidado[0]]+pesos[candidado[1]]
                    # for x in range(len(selecionados)):
                    #     peso_mochila+=pesos[selecionados[x][0]]+pesos[selecionados[x][1]]
                    #print 'peso_mochila',peso_mochila,len(selecionados)
                    count=0
                    break
                else:
                    count+=1
        print 'len',len(selecionados),'selecionados',selecionados,'suma',peso_mochila
        sosluciones.append(selecionados)
        print len(sosluciones)
        mochila=[0]*len(beneficio)
        selecionados=[]
        peso_mochila=0
        count=0
def multiArranque():

leerdatos()
#for x in range(len(beneficio)):
#    print 'ben',x,beneficio[x],sum(beneficio[x],0.0)
#   print 'pesos',pesos
mochila=[0]*len(beneficio)
constructor()
multiArranque()

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
def prom_cor(l):
    global beneficio
    aux=0
    for x in range(len(l)):
        aux+=beneficio[l[x][0]][l[x][1]]
    return aux/len(l)
def prom(l):
    if (len(l)-l.count(0))!=0:
        return sum(l) / (len(l)-l.count(0))
    else:
        return 0
def selecion():
    global mochila
    global prom_ben
    global prom_total
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
def sacar_beneficio(l):
    global sosluciones
    global beneficio
    aux=0
    for x in range(len(l)):
        aux+=beneficio[l[x][0]][l[x][1]]
    return aux
def sacar_peso(l):
    global sosluciones
    global pesos
    aux=0
    for x in range(len(l)):
        aux+=pesos[l[x][0]]+pesos[l[x][1]]
    return aux
def constructor():
    global sosluciones
    global mochila
    global cont_mochilas
    peso_mochila=0
    sosluciones=[]
    selecionados=[]
    cont_mochilas=[]
    count=0
    ben_mochila=0
    while len(sosluciones)<5:
        while cap>peso_mochila and count<5:
            while True and count<5:
                candidado=random.choice(selecion())
                if cap>peso_mochila+pesos[candidado[0]]+pesos[candidado[1]]:
                    #print 'pesos',pesos[candidado[0]],pesos[candidado[1]]
                    mochila[candidado[0]]=1
                    mochila[candidado[1]]=1
                    selecionados.append(candidado)
                    peso_mochila+=pesos[candidado[0]]+pesos[candidado[1]]
                    ben_mochila+=beneficio[candidado[0]][candidado[1]]
                    count=0
                    break
                else:
                    count+=1
        print 'len',len(selecionados),'selecionados',selecionados,'suma',peso_mochila,'ben',ben_mochila
        sosluciones.append(selecionados)
        print len(sosluciones)
        cont_mochilas.append(mochila)
        mochila=[0]*len(beneficio)
        selecionados=[]
        peso_mochila=0
        count=0
        ben_mochila=0
def hacerCambios(sosluciones):
    global beneficio
    mayor_que_prom=[]
    mutli_posibles=[]

    for w in range(len(beneficio)):
        for y in range(len(beneficio[w])):
            if beneficio[w][y]>=prom_total:
                mayor_que_prom.append([w,y])
    while len(posibles)<5 and i<10:
        while True:
            cor=mayor_que_prom[randint(0,len(mayor_que_prom)-1)]
            if mochila[cor[0]]==0 and mochila[cor[1]]==0:
                mutli_posibles.append([cor[0],cor[1]])
                break
        i=+1
    while cap>nuevo_peso and count<5:
        while True and count<5:
            candidado=random.choice(mutli_posibles)
            if cap>nuevo_peso+pesos[candidado[0]]+pesos[candidado[1]]:
                #print 'pesos',pesos[candidado[0]],pesos[candidado[1]]
                cont_mochilas[x][candidado[0]]=1
                cont_mochilas[x][candidado[1]]=1
                selecionados.append(candidado)
                nuevo_peso+=pesos[candidado[0]]+pesos[candidado[1]]
                #ben_mochila+=beneficio[candidado[0]][candidado[1]]
                count=0
                break
            else:
                count+=1
    return selecionados
def multiArranque():
    global cont_mochilas
    global beneficio
    global sosluciones
    global prom_total
    nuevo_ben=0
    re_mochila=[0]*len(beneficio)
    for x in range(len(sosluciones)):
        ben=sacar_beneficio(sosluciones[x])
        vuelta=10
        inicio=0+(x*5)
        fin=5+(x*5)
        i=0
        while vuelta<10:
            retirados=sosluciones[x][inicio:fin]
            for y in range(len(retirados)):
                 sosluciones.pop(retirados[y])
            nuevo_peso=sacar_peso(sosluciones)
            opcion=hacerCambios()
            if ben>sacar_beneficio(opcion):
                i+=1
        print fin
leerdatos()
#for x in range(len(beneficio)):
#  print 'ben',x,beneficio[x],sum(beneficio[x],0.0)
#   print 'pesos',pesos

mochila=[0]*len(beneficio)
constructor()
multiArranque()

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
    archivo = open("1000_25/1000_25_1.txt", "r")
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
    for x in range(len(datos)):
        for j in range(len(datos[x])):
            if x==j:
                aux.append(datos[x][x])
                if datos[x][x]==0:
                    count+=1
            if x<j:
                aux.append(datos[j][x])
                if datos[j][x]==0:
                    count+=1
            if x>j:
                aux.append(datos[x][j])
                if datos[x][j]==0:
                    count+=1
        ceros.append(count)
        beneficio.append(aux)
        aux=[]
        print 'count',count
        cunt=[]
    print len(beneficio)
def prom(l):
    return sum(l, 0.0) / (len(l)-l.count(0))
def constructor():
    cap=0
    promedios_ben=[]
    prom_general=0
    promedios_peso=prom(pesos)
    selecionaos=[]
    pesos_selecionados=[]
    aux=[]
    V=True
    print "pesos",len(pesos)
    for x in range(len(beneficio)):
        promedios_ben.append(prom(beneficio[x]))
    prom_general=prom(promedios_ben)
    for x in range(len(promedios_ben)):
        print 'ben',x ,len(beneficio[x])
        if promedios_ben[x]>prom_general :
            id_obj= beneficio[x].index(max(beneficio[x]))
            if promedios_peso>pesos[x] :#and promedios_peso>pesos[id_obj]: 
                if x==id_obj:
                    selecionaos.append(x)
                    cap+=pesos[x]
                    pesos_selecionados.append(pesos[x])
                else:
                    selecionaos.append(x)
                    selecionaos.append(id_obj)
                    cap+=(pesos[x]+id_obj)
                    pesos_selecionados.append(pesos[x])
                    pesos_selecionados.append(pesos[id_obj])
                mochila[x]=1
                mochila[id_obj]=1
                pesos[x]=0
                pesos[id_obj]=0
                v=False 
            else:
                beneficio[x][id_obj]=0
    print len(promedios_ben)
    print promedios_peso
    print prom_general
    print len(selecionaos)
    print selecionaos

leerdatos()
constructor()

#print beneficio
#print pesos

global beneficio
global pesos
global beneficio_individaules
global mochila
mochila=[0]*1000
beneficio=[]
pesos=[]
beneficio_individaules=[]
def leerdatos(): 
    global pesos
    global beneficio
    line=0
    aux=[]
    suma=""
    cap=0
    datos=[]
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
                aux=[]
            else:
                if cap==0:
                    cap=aux[0]
                    aux=[]
                else:
                    pesos=aux
                    aux=[]
    aux=[]
    for x in range(len(datos)):
        for j in range(len(datos[x])):
            if x==j:
                aux.append(datos[x][x])
            elif x<j:
                aux.append(datos[j][x])
            elif x>j:
                aux.append(datos[x][j])
        beneficio.append(aux)
    print len(beneficio)
def prom(l):
    return sum(l, 0.0) / len(l)
def constructor():
    promedios_ben=[]
    for x in range(len(beneficio)):
       promedios_ben.append(prom(beneficio[x]))
    print len(promedios_ben)
    promedios_peso=prom(pesos)
    print promedios_peso
    

leerdatos()
constructor()

#print beneficio
#print pesos

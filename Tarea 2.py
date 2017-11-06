# -*- coding: utf-8 -*-




txt = raw_input("Ingrese el nombre del archivo a leer: ")
entrada = open(txt,"r")
sali = raw_input("Ingrese el nombre del archivo de salida: ")
salida = open(sali,"w")

a =entrada.readline()
t = int(a[0])
b = int(a[2])
f = int(a[4])
c = int(a[6])

nodos = 0
tl = t
lf =c
grafo = {}

if(c>0):
    tl = tl-2
    grafo[1] = [2,3]
    grafo[2] = []
    grafo[3] = [2]
    nodos = 3
    if(c==2):
        grafo[2] = [3]
        grafo[3] = [2]     
    if(c>2):
        a = c-1
        grafo[3].append(4)
        tl = tl -1
        for i in range(a):
            nodos = nodos +1
            if(nodos != c+2):
                grafo[nodos] = [2,nodos+1]
                tl = tl-1
            else:
                grafo[nodos] = [2]                           
            
if(tl!=0):
    cuenta = tl
    for i in range(cuenta):
        tl = tl-1
        nodos = nodos + 1
        if(i == 1):
            grafo[nodos] = []
        else:            
            if(tl!=0):
                grafo[nodos] = [nodos+1]
            else:
                grafo[nodos] = []

if(b!=0):
    if(b==1):
        grafo[2].append(1)
    if(b==2):
        grafo[2].append(1)
        grafo[3].append(1)
    if(b>2):
        grafo[2].append(1)
        grafo[3].append(1)
        aux = nodos
        for i in range(b-2):
            grafo[aux].append(aux-1)
            aux = aux-1
        
if(f!=0):
    if(f==1 and nodos > 3):
        grafo[1].append(4)
    else:
        grafo[1].append(3)
        unir = 4
        for i in range(f-1):
            if(unir<=nodos):
                grafo[1].append(unir)
                unir = unir +1
                lf = lf-1
        auxi = lf
        for i in range(auxi):
            a = 4
            b = 4
            for j in range(nodos+1)[3:-1]:
                grafo[j].append(a)
                a = a + 1
            b = b + 1
            a = b
            
                




        
for i in grafo:
    a = "Nodo " + str(i) +": "
    for jj in grafo[i]:
        a = a + str(jj) + " "
    a = a + "\n"
    salida.writelines(a)        
        



























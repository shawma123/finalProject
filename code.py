import numpy as np
import automata

n=2 #actual attack number
A=[{'a':'a','c':'c'},
   {'a':'ε','c':'a'},
   {'a':'c','c':['c','ac']}]

def algorithm1(G,A,Eo,Euo):
    tableC=np.array([[-1 for j in range(1)]for k in range(1)] ,dtype=str)
    for i in range(n+1):
        lenth=len(Xc)
        for m in range(M):
            Xc.append('x'+str(m)+str(i))
        #print(Xc)
        N=len(Xc)
        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
        for j in range(lenth):
            for g in range(lenth):
                tableNew[j][g]=tableC[j][g]
        tableC=tableNew.copy()
        tableC[0][lenth]='a'+str(i)
        for k in range(M):
            for e in Eo:
                for m in range(M): #k'==m
                    if table[k][m]==e:
                        if e in A[i]:
                            w=A[i][e]
                            if isinstance(w,str):
                                b=len(w)
                                if b==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(i))]=w
                                elif b>1:
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(m)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[c]
                                        
                                        else:
                                            tableC[Xc.index('x'+str(m)+str(c)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[c]
                                    tableC[Xc.index('x'+str(m)+str(c+1)+str(i))][Xc.index('x'+str(m)+str(i))]=w[c+1]
                            elif isinstance(w,list):
                                if len(w[0])==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(i))]=w[0]
                                    b=len(w[1])
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(m)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[1][c]
                                        else:
                                            tableC[Xc.index('x'+str(m)+str(c)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[1][c]
                                    tableC[Xc.index('x'+str(m)+str(c+1)+str(i))][Xc.index('x'+str(m)+str(i))]=w[1][c+1]
                                elif len(w[1])==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(i))]=w[1]
                                    b=len(w[0])
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(m)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[0][c]
                                        else:
                                            tableC[Xc.index('x'+str(m)+str(c)+str(i))][Xc.index('x'+str(m)+str(c+1)+str(i))]=w[0][c]
                                    tableC[Xc.index('x'+str(m)+str(c+1)+str(i))][Xc.index('x'+str(m)+str(i))]=w[0][c+1]
                                    
                        else:
                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m)+str(i))]
                            
        


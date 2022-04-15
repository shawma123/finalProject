import numpy as np
import automata




n=2 #actual attack number
A=[{'a':'a','c':'c'},
   {'a':'ε','c':'a'},
   {'a':'c','c':['c','ac']}]
def algorithm2(G,A,Eo,Euo):
    for k in range(M):
        for e in Eo:
            for m in range(M):
                if table[k][m]==e:
                    for i in range(1,n+1):
                        if e in A[i] and A[i][e] !='ε':
                            if not 'x'+str(k)+str(i) in Xc:
                                lenth=len(Xc)
                                Xc.append('x'+str(k)+str(i))
                                N=len(Xc)
                                tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                for j in range(lenth):
                                    for g in range(lenth):
                                        tableNew[j][g]=tableC[j][g]
                                tableC=tableNew.copy()
                                tableC[k][N-1]='a'+str(i)
                            w=A[i][e]
                            if isinstance(w,str):
                                b=len(w)
                                if b==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m))]=w
                                elif b>1:
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(k)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[c]
                                        
                                        else:
                                            tableC[Xc.index('x'+str(k)+str(c)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[c]
                                    tableC[Xc.index('x'+str(k)+str(c+1)+str(i))][Xc.index('x'+str(m))]=w[c+1]
                            elif isinstance(w,list):
                                if len(w[0])==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m))]=w[0]
                                    b=len(w[1])
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(k)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[1][c]
                                        else:
                                            tableC[Xc.index('x'+str(k)+str(c)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[1][c]
                                    tableC[Xc.index('x'+str(k)+str(c+1)+str(i))][Xc.index('x'+str(m))]=w[1][c+1]
                                elif len(w[1])==1:
                                    tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(m))]=w[1]
                                    b=len(w[0])
                                    for c in range(b-1):
                                        lenth=len(Xc)
                                        Xc.append('x'+str(k)+str(c+1)+str(i))
                                        N=len(Xc)
                                        tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                        for j in range(lenth):
                                            for g in range(lenth):
                                                tableNew[j][g]=tableC[j][g]
                                        tableC=tableNew.copy()
                                        if c==0:
                                            tableC[Xc.index('x'+str(k)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[0][c]
                                        else:
                                            tableC[Xc.index('x'+str(k)+str(c)+str(i))][Xc.index('x'+str(k)+str(c+1)+str(i))]=w[0][c]
                                    tableC[Xc.index('x'+str(k)+str(c+1)+str(i))][Xc.index('x'+str(m))]=w[0][c+1]

                        elif e in A[i] and A[i][e] =='ε':
                            tableC[k][m]=tableC[k][m]+'+a'+str(i)

def arrayMaker(l1,l2,tableOld):
    table=np.array([[-1 for j in range(l2)]for k in range(l2)] ,dtype=str)
    for i in range(l1):
        for j in range(l1):
            table[i][j]=tableOld[i][j]
    return table.copy()

def εR(f,X,B,e):
    lenth=len(X)
    x=[]
    for i in B:
        for j in range(lenth):
            if f[X.index(i)][j]==e:
                if x.count(X[j])==0:
                    x.append(X[j])
                    x.extend(εR(f,X,[X[j]],'ε'))
            if f[X.index(i)][j]=='ε':
                if x.count(X[j])==0:
                    x.append(X[j])
                    x.extend(εR(f,X,[X[j]],e))
    return list(set(x))  

def composition(G1,G2):
    len1=len(Z1)
    len2=len(Z2)
    E1=[]
    E2=[]
    for i in range(len1):
        for j in range(len1):
            if t1[i][j]!='-1' and E1.count(t1[i][j])==0:
                E1.append(t1[i][j])

    for i in range(len2):
        for j in range(len2):
            if t2[i][j]!='-1' and E2.count(t2[i][j])==0:
                E2.append(t2[i][j])

    E0=E1.copy()
    for i in range(len(E2)):
        if E0.count(E2[i])==0:
            E0.append(E2[i])
    Z=[]
    Z.append([Z1[0],Z2[0]])

    table=np.array([[-1 for j in range(1)]for k in range(1)] ,dtype=str)
    for i in Z:
        for j in E0:
            status1= False
            status2= False
            z0=i[0]
            z1=i[1]
            for n in range(len1):
                if t1[Z1.index(i[0])][n]==j:
                    status1=True
                    z0=Z1[n]
                    break
            for n in range(len2):
                if t2[Z2.index(i[1])][n]==j:
                    status1=True
                    z1=Z2[n]
                    break
            if status1 and status2:
                z=[z0,z1]
                lenth=len(Z)
                Z.append(z)
                lenthNew=len(Z)
                table=arrayMaker(lenth,lenthNew,table)
                table[Z.index(i)][lenthNew-1]=j
            elif status1 and not status2:
                z=[z0,z1]
                lenth=len(Z)
                Z.append(z)
                lenthNew=len(Z)
                table=arrayMaker(lenth,lenthNew,table)
                table[Z.index(i)][lenthNew-1]=j
            elif not status1 and status2:
                z=[z0,z1]
                lenth=len(Z)
                Z.append(z)
                lenthNew=len(Z)
                table=arrayMaker(lenth,lenthNew,table)
                table[Z.index(i)][lenthNew-1]=j


def diagnoser(Gnd,Xnd):
    End=[]
    lenthnd=len(Xnd)
    for i in range(lenthnd):
        for j in range(lenthnd):
            if Gnd[i][j]!='-1' and End.count(t1[i][j])==0:
                End.append(t1[i][j])
    Xobs=[]
    x0=[Xnd[0]]
    x0=εR(Gnd,Xnd,x0,'ε').append(Xnd[0])
    Xobs.append(x0)
    table=np.array([[-1 for j in range(1)]for k in range(1)] ,dtype=str)
    for b in range(len(Xobs)):
        for e in End:
            xNew=εR(Gnd,Xnd,Xobs[b],e)
            lenthX=len(Xobs)
            status=0
            for i in range(len(Xobs)):
                if set(Xobs[i]).difference(set(xNew))==set() and set(xNew).difference(Xobs[i])==set():
                    table[i][i]=e
                    status=1
                    break
            if status==0:
                lenthOld=len(Xobs)
                Xobs.append(xNew)
                table=arrayMaker(lenthOld,lenthOld+1,table)
                table[b][lenthOld]=e


def algorithm3 (Gs,A,Ea):
    n=len(A)
    Gobs = []
    Gl = []
    for i in range(n): # loop the set of attack dictionaries
        for k in range(M):
            for e in Eo:
                for m in range(M):
                    if table[k][m]==e:
                        for i in range(1,n+1):
                            if e in A[i] and A[i][e] !='ε':
                                if not 'x'+str(k)+str(i) in Xc:
                                    lenth=len(Xc)
                                    Xc.append('x'+str(k)+str(i))
                                    N=len(Xc)
                                    tableNew=np.array([[-1 for j in range(N)]for k in range(N)] ,dtype=str)
                                    for j in range(lenth):
                                        for g in range(lenth):
                                            tableNew[j][g]=tableC[j][g]
                                    tableC=tableNew.copy()
                                    tableC[k][N-1]='a'+str(i)



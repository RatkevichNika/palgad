from random import *
def sisesta_andmed(i, p):
    N=4
    for n in range(N):
        inimene=input('Teie nimi: ')
        i.append(inimene)
        palk=randint(1000,10000)
        p.append(palk)
        return i,p
def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],'-',p[n])
def kustutamine(i,p):
    nimi=input('Sisesta nimi, keda vaja kustutada: ')
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(e)
                print(t,'.',i[e],'-',p[e])
        j=int(input('Järjekordne number: '))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])

    return(i,p)
def suurim_palk(i,p):
    suurim=max(p)
    d=p.index(suurim)
    x=p.count(suurim)
    print(i[d],'-',p[d])
    return(i,p)
def sorteeremine(i,p,v):
    N=len(p)
    if v==1:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
        for n in range (0,N):
            for m in range (n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)
def vordsed_palgad(i,p):
    N=len(p)
    dublikatid=[x for x in palgad if palgad.count(x)>1]
    dublikatid=list(set(dublikatid))
    print(dublikatid)
    for palk in dublikatid:
        n=p.count(palk)
        k=0
        for j in range(n):
            k=p.index(palk,j+k)
            nimi=i[k]
        print(palk,'saab kätte',nimi)
def otsimine(i,p):
    nimi=input('Ssisesta nimi,keda vaja otsida:')
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(e)
                print(t,'.',i[e],'-',p[e])
def sort(i,p):
    zarplata=int(input('Sisesta palk: '))
    b=input('1.vähem\n2.suurem\nTeie valik: ')
    if b=='1':
        for palk in p:
            if zarplata>palk:
                print(palk,'-',i[p.index(palk)])
    elif b=='2':
        for palk in p:
            if zarplata<palk:
                print(palk,'-',i[p.index(palk)])
def keskmine(i,p):
    summa=0
    t=True
    for palk in p:
        summa+=palk
    summa/=len(p)
    print('Keskmine palk:', summa)
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print('Saab kätte:',i[n])
    else:
        t=False
    if t==False: 
        print('Sellised inimesed puuduvad')
inimesed=['A','B','C']
palgad=[3000,2000,1000]
keskmine(inimesed,palgad)

def top3(i,p):
        N=len(p)
        we=int(input('1-top 3 suuremaid palgad\n2- top3 vaiksemad palgad\nTeie valik:'))
        if we==1:
            for n in range (0,N):
                for m in range (n,N):
                    if p[n]<p[m]:
                        abi=p[n]
                        p[n]=p[m]
                        p[m]=abi
                        abi=i[n]
                        i[n]=i[m]
                        i[m]=abi
        elif we==2:
            for i in range (0,N):
                for m in range (n,N):
                    if p[n]>p[m]:
                        abi=p[n]
                        p[n]=p[m]
                        p[m]=abi
                        abi=i[n]
                        i[n]=i[m]
                        i[m]=abi
        for n in range(3):
            print(i[n],'-',p[n])
def sort_nimi_jargi(i,p):
    zp=int(input('Sisesta palk: '))
    b=input('1.vähem\n2.suurem\nTeie valik: ')
    if b=='1':
        for palk in p:
            if zp>palk:
                print(palk,'-',i[p.index(palk)])
    elif b=='2':
        for palk in p:
            if zp<palk:
                print(palk,'-',i[p.index(palk)])

while 1:
    valik=input('a - andmete sisestamine\ne - andmed ekranile\nk - kustutamine inimese palk\nmax - suurim palk\ns - sorteeremine\nd - võrdsed palgad\nl - inimese otsimine\nw- sisesta palk\nq-top3\nh-sort_nimi_jargi\nTeie valik: ')
    if valik.lower()=='a':
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=='e':
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=='k':
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik.lower()=='max':
        inimesed,palgad=suurim_palk(inimesed,palgad)
    elif valik.lower()=='s':
        sorteeremine(inimesed,palgad, int(input('1-kahaneb, 2-kasvab: ')))
    elif valik.lower()=='d':
        vordsed_palgad(inimesed,palgad)
    elif valik.lower()=='l':
        otsimine(inimesed,palgad)
    elif valik.lower()=='w':
        sort(inimesed,palgad)
    elif valik.lower()=='q':
        top3(inimesed,palgad)
    elif valik.lower()=='h':
        sort_nimi_jargi(inimesed,palgad,int(input('1 - A-Z\n2 - Z-A\nTeie valik:')))
    else:
        break
inimesed,palgad=sisesta_andmed(inimesed,palgad)
andmed_ekranile(inimesed,palgad)

'''n=int(input('n:'))
minim=1000
maxim=-1000
S=0
for i in range(n):
    x=int(input('x:'))
    ct=0
    for j in range(2,int(x/2)+1):
        if x%j==0:
            ct+=1
    if ct==0:
        if x<minim:
            minim=x
        if x>maxim:
            maxim=x
    copy_x=x
    if copy_x<10:
        S+=x
    else:
        crescator=True
        while copy_x>0:
            cifra_curenta=copy_x%10
            copy_x=int(copy_x/10)
            if (cifra_curenta)<(copy_x%10):
                crascator=False
                break
        if crescator:
            S+=x
print('Minim={},Maxim={}'.format(minim,maxim))
print('Suma numeelor cu cifre crescatoare este:{}'.format(S))'''

'''nr1=input('nr1:')
nr2=input('nr2:')
lungimea_nr1=len(nr1)
lungimea_nr2=len(nr2)
cpy_nr1=int(nr1)
cpy_nr2=int(nr2)
ct_nr1_nr2=0
elemente_folosite=''
while cpy_nr1>0:
    cifra_crt_nr1=cpy_nr1%10
    cpy_nr1=int(cpy_nr1/10)
    cpy_nr2=int(nr2)
    if str(cifra_crt_nr1) not in elemente_folosite:
        while cpy_nr2>0:
            cifra_crt_nr2=cpy_nr2%10
            if cifra_crt_nr1==cifra_crt_nr2:
                ct_nr1_nr2+=1
            cpy_nr2=int(cpy_nr2/10)
        elemente_folosite=elemente_folosite+str(cifra_crt_nr1)
    else:
        continue
if ct_nr1_nr2==lungimea_nr2:
    print('Numerele sunt formate din aceleasi cifre')'''

'''a)
def spatii(n):
    for i in range(1,n+1):
        print(end=' ')
def stelute(n):
    for i in range(1,n+1):
        print(end='*')
def bradulet(n):
    for i in range(1,n+1):
        spatii(n-i)
        stelute(2*i-1)
        print()
    spatii(n-1)
    print('*')
bradulet(5)'''

'''b)
x=int(input('x:'))
y=int(input('y:'))
def medie(x,y):
    print('({}+{})/2={}'.format(x,y,(x+y)/2))
medie(x,y)'''

'''c)
x=int(input('x:'))
y=int(input('y:'))
z=int(input('z:'))
t=int(input('t:'))
def M(x,y,z):
    print('M({},{},{})={}'.format(x,y,z,(x+y+z)/3))
M(x,y,z)
def F(x,y):
    print('F({},{})={}'.format(x, y, (x + 3) / 2 + y))
F(x,y)
def F(x,y,z,t):
    print('E({},{},{},{})={}'.format(x, y, z, t, (x + y) / 2 + (z*t)/3))
F(x,y,z,t)'''


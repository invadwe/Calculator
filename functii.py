def suma(a,b):
    return a+b

def produs(a,b):
    return a*b

def par(n):
    if n%2==0:
        return True
    else:
        return False

def prim(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
if __name__=='main':
    with open('test.txt','r') as file:
        linii=file.readlines()
    print(linii)
    for i in linii:
        if i.startswith('suma'):
            lista_suma=[]
            i=i.replace('suma: ','')
            i=i.replace('\n','')
            lista_suma=i.split(',')
            for j in lista_suma:
                var=j.split(' ')
                print('Suma numerelor {} si {} este {}'.format(var[0],var[1],suma(int(var[0]),int(var[1]))))
        if i.startswith('produs'):
            lista_produs=[]
            i=i.replace('produs: ','')
            i=i.replace('\n','')
            lista_produs=i.split(',')
            for j in lista_produs:
                var=j.split(' ')
                print('Produsul numerelor {} si {} este {}'.format(var[0],var[1],produs(int(var[0]),int(var[1]))))
        if i.startswith('par'):
            lista_par=[]
            i=i.replace('par: ','')
            i=i.replace('\n','')
            lista_par=i.split(' ')
            for j in lista_par:
                var=j.split(' ')
                print('Numarul '+j+(' este par' if par(int(j)) else ' nu este par'))
        if i.startswith('prim'):
            lista_prim=[]
            i=i.replace('prim: ','')
            i=i.replace('\n','')
            lista_prim=i.split(' ')
            for j in lista_prim:
                var=j.split(' ')
                print('Numarul '+j+(' este prim' if prim(int(j)) else ' nu este prim'))

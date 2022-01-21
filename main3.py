'''a)
lista_semne = "!@#$%^&*()_+-=[]{};:',<.>/?| " + '"'
cifre = '0123456789'

with open("problema_a.txt", 'r') as file:
    text = file.read()
text = text.replace("\n", '')
for i in lista_semne:
    text = text.replace(i,'')
text = text.lower()
for i in cifre:
    text = text.replace(i,'')
dictionar_litere = dict()
for i in text:
    if dictionar_litere.get(i):
        dictionar_litere[i] = dictionar_litere[i]+1
    else:
        dictionar_litere[i] = 1
key = dictionar_litere.keys()
with open("rezolvare_problema_a.txt" , 'w') as file:
    for i in key:
        file.write(i + " appeared {} times".format(dictionar_litere[i]) + "\n")'''

'''b)
fisier_1 = input("Numele primului fisier:")
fisier_2 = input("Numele celui de al doilea fisier:")
if not(fisier_1.endswith(".txt")):
    fisier_1+=".txt"
if not(fisier_2.endswith(".txt")):
    fisier_2+=".txt"

with open(fisier_1) as file1:
    first = file1.read()
with open(fisier_2) as file2:
    second = file2.read()
if first == second:
    print("Fisierele au acelasi continut!")
else:
    print("Fisierele nu au acelasi continut!")'''

'''c)
def Prim(n):
    for i in range(2,int(n/2)+1):
        if n%i  == 0:
            return False
    return True
with open("problema_c.txt" , 'r') as file:
    text = file.read()
numere_str = text.split(" ")
numere = []
for i in numere_str:
    numere.append(int(i))
nr_pare = []
nr_impare = []
nr_prime = []
for i in numere:
    if i%2 == 0:
        nr_pare.append(i)
    else:
        nr_impare.append(i)
    if Prim(i):
        nr_prime.append(i)
with open("rezolvare_problema_c_par.txt" , 'w') as file:
    file.write(str(nr_pare))
with open("rezolvare_problema_c_impar.txt" , 'w') as file:
    file.write(str(nr_impare))
with open("rezolvare_problema_c_prim.txt" , 'w') as file:
    file.write(str(nr_prime))'''

''''def Min(x,y,z):
    x if x<(y if y<z else z) else (y if y<z else z)
def Max(x,y,z):
    x if x>(y if y>z else z) else (y if y>z else z)
def Mij(x,y,z):
    max=Max(x,y,z)
    min=Min(x,y,z)
    Mij=x+y+z-max-min
    return Mij
x=int(input('x='))
y=int(input('y='))
z=int(input('z='))
print(Mij(x,y,z))'''

lista_semne = "!@#$%^&*()_+-=[]{};:',<.>/?| " + '"'
cifre = '0123456789'

with open("intrare.txt", 'r') as file:
    text = file.read()
text = text.replace("\n", '')
for i in lista_semne:
    text = text.replace(i,'')
text = text.lower()
for i in cifre:
    text = text.replace(i,'')
dictionar_litere = dict()
for i in text:
    if dictionar_litere.get(i):
        dictionar_litere[i] = dictionar_litere[i]+1
    else:
        dictionar_litere[i] = 1
key = dictionar_litere.keys()
with open("iesire.txt" , 'w') as file:
    for i in key:
        file.write(i + " appeared {} times".format(dictionar_litere[i]) + "\n")

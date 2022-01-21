# 1.
# class Dreptunghi:
#     def __init__(self,lungime,latime):
#         self.lungime=lungime
#         self.latime=latime
#     def Perimetru(self):
#         return (2*self.lungime)+(2*self.latime)
#     def Arie(self):
#         return (self.lungime*self.latime)
#     def Display(self):
#         print('Obiectula {} m si latimea {} m.'.format(self.lungime,self.latime))
#         print('Obiectul are perimetrul de {} m si aria de {} m patrati.'.format(self.Perimetru(),self.Arie()))
# class Paralelipiped(Dreptunghi):
#     def __init__(self,lungime,latime,inaltime):
#         super().__init__(lungime,latime)
#         self.inaltime=inaltime
#     def Volum(self):
#         return self.inaltime*self.Arie()
#     def Display(self):
#         super().Display()
#         print('Obiectul are inaltimea de {} m si volumul de {} m cubi'.format(self.inaltime,self.Volum()))
# var1=Paralelipiped(2,3,5)
# var1.Display()


# 2.
# def CheckPin(pin):
#     if pin>=1000 and pin <=9999 and type(pin) is int:
#         return True
#     else:
#         return False
# class BankAccount:
#     def __init__(self,pin):
#         if CheckPin(pin):
#             self.__pin=pin
#             self.__balanta=0
#         else:
#             del self
#     def Depozit(self,pin,amount):
#         if pin== self.__pin:
#             self.__balanta+=amount
#         else:
#             print('Wrong PIN!')
#     def Withdraw(self,pin,amount):
#         if pin==self.__pin:
#             if amount<=self.__balanta:
#                 self.__balanta_=amount
#             else:
#                 print('Not enough money!')
#         else:
#             print('Wrong PIN!')
#     def Get_balance(self,pin):
#         if pin==self.__pin:
#             print('Balanta este {}'.format(self.__balanta))
#         else:
#             print('Wrong PIN!')
#     def Change_pin(self,oldpin,newpin):
#         if oldpin==self.__pin:
#             self.__pin=newpin
#             print('Pin changed!')
#         else:
#             print('Wrong PIN!')
# A=BankAccount(1234)
# A.Depozit(1234,10000)
# A.Get_balance(1234)
# A.Withdraw(1234,77)
# A.Get_balance(1234)
# A.Change_pin(1234,2234)
# A.Get_balance(1234)
'''def Prim(n):
    for i in range(2,int(n/2)+1):
        if n%i==0
            prim=False

lista=list()
with open('fisier_citire','r') as file:
    for i in file.readlines():
        a=i.split(' ')
        a[2]=a[2].replace('\n','')
        lista.append(int(a[2]))
print(lista)
with open('fisiere')'''

'''with open('intrare.txt','r') as file:
    var=file.readline()
lista=var.split(' ')
S=0
for i in lista:
    S+=int(i)
with open('iesire.txt','a') as file:
    file.write('Suma este '+str(S)+'\n')'''

'''numef=input('Numele fisierului: ')
with open(numef,'r') as file:
    var=file.read()
print(var)
with open('output.txt','w') as file:
    file.write(var)'''

'''def Prim(m):
    for i in range(2,int(m/2)+1):
        if m%i==0:
            return False
    return True

lista=list()
with open('fisier_citire.txt','r') as file:
    var=file.readlines()
    for i in var:
        i=i.replace('n = ','')
        i=i.replace('\n','')
        lista.append(i)
print(lista)
with open('fisier_scriere.txt','w') as file:
    for i in lista:
        file.write('n = ' + i + '->')
        for j in range(1,int(i)+1):
            if Prim(j):
                file.write(str(j)+' ')
        file.write('\n')'''



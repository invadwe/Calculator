istoric=[]
def Adunare(a,b):
    return a+b
def Scadere(a,b):
    return a-b
def Inmultire(a,b):
    return a*b
def Impartire(a,b):
    return a/b
def Modulo(a,b):
    return a%b
def RidicareLaPutere(a,b):
    return a**b
import math

def Factorial(n):
    return math.factorial(n)
def lg(n):
    return math.log10(n)
def logX(x,base):
    return math.log(x,base)
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def ctan(x):
    return 1/math.tan(math.radians(x))
def exp(x):
    return math.e**x
pi=math.pi
e=math.e


print('Selectati operatia:')
print('1.Adunare')
print('2.Scadere')
print('3.Inmultire')
print('4.Impartire')
print('5.Modulo')
print('6.Ridicarea la putere')
print('7.factorial')
print('8.Logaritm in baza 10')
print('9.Logaritm cu o baza X introdusa de la tastatura')
print('10.Logaritm natural')
print('11.Sin')
print('12.Cos')
print('13.Tangenta')
print('14.Cotangenta')
print('15.Exponentiala')


while True:
   choice=input('Alegeti operatia(1/2/3/4/5/6/7/8/9/10/11/12/13/14/15):')
   if choice in ('1','2','3','4','5','6','7','8','9','10', '11','12','13','14','15'):
       print('operatie corecta')
   else:
       print('Error')

   if choice=='1':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}+{}={}'.format(nr1,nr2,Adunare(nr1,nr2)))
       istoric.append(Adunare(nr1,nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')

   elif choice=='2':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}-{}={}'.format(nr1, nr2, Scadere(nr1, nr2)))
       istoric.append(Scadere(nr1, nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')
   elif choice == '3':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}*{}={}'.format(nr1, nr2, Inmultire(nr1, nr2)))
       istoric.append(Inmultire(nr1, nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')
   elif choice == '4':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}/{}={}'.format(nr1, nr2, Impartire(nr1, nr2)))
       istoric.append(Impartire(nr1, nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')
   elif choice == '5':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}%{}={}'.format(nr1, nr2, Modulo(nr1, nr2)))
       istoric.append(Modulo(nr1, nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')
   elif choice == '6':
     try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('{}**{}={}'.format(nr1, nr2, RidicareLaPutere(nr1, nr2)))
       istoric.append(RidicareLaPutere(nr1, nr2))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')
   elif choice == '7':
     try:
       nr1 = input('nr1:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = int(nr1)
       print(nr1, "!", '=', Factorial(nr1))
       istoric.append(Factorial(nr1))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')

   elif choice == '8':
     try:
       nr1 = input('nr1:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       print("log10", nr1, "=", lg(nr1))
       istoric.append(lg(nr1))
     except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')

   elif choice == '9':
    try:
       nr1 = input('nr1:')
       nr2 = input('nr2:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       if nr2 == 'e':
           nr2 = math.e
       elif nr2 == 'pi':
           nr2 = math.pi
       else:
           nr2 = float(nr2)
       print('Log in base', nr2, "din", nr1, "=", logX(nr1, nr2))
       istoric.append(logX(nr1, nr2))
    except ValueError as error:
        print(error)
        print('Ati introdus stringuri!')


   elif choice == '10':
    try:
       nr1 = input('nr1:')
       if nr1 == 'e':
           nr1 = math.e
       elif nr1 == 'pi':
           nr1 = math.pi
       else:
           nr1 = float(nr1)
       print("ln", nr1, "=", logX(nr1,e))
       istoric.append(logX(nr1,e))
    except ValueError as error:
        print(error)
        print('Ati introdus stringuri!')


   elif choice == '11':
    try:
        nr1 = int(input('nr1:'))
        print('Sinus de', nr1, 'este:', sin(nr1))
        istoric.append(sin(nr1))
    except ValueError as error:
         print(error)
         print('Ati introdus stringuri!')

   elif choice == '12':
      try:
        nr1 = int(input('nr1:'))
        print('Cosinus din', nr1, 'este:', cos(nr1))
        istoric.append(cos(nr1))
      except ValueError as error:
          print(error)
          print('Ati introdus stringuri!')

   elif choice == '13':
    try:
        x = int(input('x='))
        print('Tangenta din', x, 'este:', tan(x))
        istoric.append(tan(nr1))
    except ValueError as error:
        print(error)
        print('Ati introdus stringuri!')
   elif choice == '14':
    try:
        nr1 = int(input('nr1:'))
        print('Cotangenta din', nr1, 'este:', ctan(nr1))
        istoric.append(ctan(nr1))
    except ValueError as error:
        print(error)
        print('Ati introdus stringuri!')

   elif choice == '15':
    try:
        nr1 = int(input('nr1:'))
        print('Exponential din', nr1, 'este:', exp(nr1))
        istoric.append(exp(nr1))
    except ValueError as error:
        print(error)
        print('Ati introdus stringuri!')

   calcul_nou=input('Continuati calculul?(da/nu):')
   if calcul_nou in ('da','nu'):
       print()
   else:
       print('Error')
   if calcul_nou=='nu':
       istoric_op = input('Doresti sa vezi istoricul operatiilor?(da/nu)')
       if istoric_op in ('da', 'nu'):
           print()
       else:
           print('error')
       if istoric_op == 'da':
           print('istoricul este:', istoric[-5:])
       else:
           print('ok!')

       break


try:
 fisier=input('Doriti sa introduceti un fisier ca si input? (da/nu):')
 if fisier in ('da','nu'):
     print()
 else:
     print('error')

 if fisier=='da':
     fisier_input= input('Introduceti nume fisierului pe care doriti sa il cititi :') #fisierul va contine cate o operatie pe fiecare linie cu spatiu intre numere si operatie (exemplu: 2 + 1) operatii disponibile:(+, -, , /,%, *, !)
     f=open(fisier_input,'r')
     print('fisierul exista!')

     file=f.readlines()
     newList=[]
     for line in file:
        if line[-1]=='\n':
           newList.append(line[:-1])#cu exceptia ultimului
        else:
            newList.append(line)
     f_new=open('rezultate.txt', 'w') #in noul fisier se va afisa rezultatul operatiilor corespunzatoare liniilor(exemplu: pe linia 1 se va afisa rezultatul operatiei de pe linia 1 din fisierul input)


     for i in range(0, len(newList)):
        coppy=newList
        calcul=coppy[i].split(' ')
        if len(calcul)==3:
         nr1=calcul[0]
         nr2=calcul[2]
         if nr1 == 'e':
             nr1 = math.e
         elif nr1 == 'pi':
             nr1 = math.pi
         else:
             nr1 = float(nr1)
         if nr2 == 'e':
             nr2 = math.e
         elif nr2 == 'pi':
             nr2 = math.pi
         else:
             nr2 = float(nr2)

         operatie=calcul[1]
        if len(calcul)==2:
         nr1=calcul[0]
         if nr1 == 'e':
             nr1 = math.e
         elif nr1 == 'pi':
             nr1 = math.pi
         else:
             nr1 = float(nr1)
         operatie=calcul[1]
        if operatie=='+':
            A=Adunare(nr1,nr2)
            f_new.write(str(A))
            f_new.write('\n')
        elif operatie == '-':
            f_new.write(str(Scadere(nr1,nr2)))
            f_new.write('\n')
        elif operatie == '*':
            P = Inmultire(nr1, nr2)
            f_new.write(str(P))
            f_new.write('\n')
        elif operatie=='/':
            f_new.write(str(Impartire(nr1,nr2)))
            f_new.write('\n')
        elif operatie=='%':
            f_new.write(str(Modulo(nr1,nr2)))
            f_new.write('\n')

        elif operatie=='**':
            f_new.write(str(RidicareLaPutere(nr1,nr2)))
            f_new.write('\n')
        elif operatie=='!':
            factorial=Factorial(int(nr1))
            f_new.write(str(factorial))
            f_new.write('\n')

     f.close()
     f_new.close()
 else:
    print('ok!')

except FileNotFoundError:
   print('Fisierul nu exista!')


from tkinter import *
istoric_grafic=[]
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnClearDisplay():
    global operator
    operator=''
    text_input.set('')
def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator = ''
    istoric_grafic.append(sumup)




root=Tk()
root.configure(background='light pink')
root.geometry("330x390+0+0")
root.title('Calculator')
root.resizable(0, 0)
operator=''
text_input=StringVar()

calc=Frame(root)
calc.grid()


txtDisplay=Entry(calc,font=('arial',20, 'bold'),bg='light pink', bd=20, width=19, justify=RIGHT, textvariable=text_input)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,'0')

btn7=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(7),text='7').grid(row=1,column=0,pady=1)
btn8=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(8),text='8').grid(row=1,column=1,pady=1)
btn9=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(9),text='9').grid(row=1,column=2,pady=1)
btnAdd=Button(calc,text='+', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick('+')).grid(row=1,column=3,pady=1)
btn4=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(4),text='4').grid(row=2,column=0,pady=1)
btn5=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(5),text='5').grid(row=2,column=1,pady=1)
btn6=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(6),text='6').grid(row=2,column=2,pady=1)
btnSub=Button(calc,text='-', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick('-')).grid(row=2,column=3,pady=1)
btn1=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(1),text='1').grid(row=3,column=0,pady=1)
btn2=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(2),text='2').grid(row=3,column=1,pady=1)
btn3=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(3),text='3').grid(row=3,column=2,pady=1)
btnMulti=Button(calc,text='×', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick('*')).grid(row=3,column=3,pady=1)
btn0=Button(calc,width=3,height=1,font=('arial',20, 'bold'),bd=4,bg='light grey',command=lambda:btnClick(0),text='0').grid(row=4,column=1,pady=1)
btnClear=Button(calc,text=chr(67), width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=btnClearDisplay).grid(row=5,column=0,pady=1)
btnEq=Button(calc,text='=', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=btnEqualsInput).grid(row=5,column=3,pady=1)
btnDiv=Button(calc,text='÷', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick('/')).grid(row=4,column=3,pady=1)
btn_r_par=Button(calc,text=')', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick(')')).grid(row=5,column=2,pady=1)
btn_l_par=Button(calc,text='(', width=3,height=1,font=('arial',20, 'bold'),bd=4, bg='light pink',command=lambda:btnClick('(')).grid(row=5,column=1,pady=1)

root.mainloop()
istoric_calculator_grafic = input('Doresti sa vezi istoricul operatiilor din calculatorul grafic?(da/nu)')
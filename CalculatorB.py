import math
import time
def suma(a,b):
    return a+b
def diferenta(a,b):
    return a-b
def inmultire(a,b):
    return a*b
def impartire(a,b):
    return a/b
def putere(a,b):
    return a**b
def modul(a,b):
    return a%b
def log2(a):
    return math.log2(a)
def factorial(a):
    return math.factorial(a)
def log10(a):
    return math.log10(a)
def log(a):
    return math.log(a)
def logn(a,baza):
    return math.log(a, baza)
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def exp(a):
    return math.exp(a)
def check (x):
    ok=1
    e = math.e
    pi = math.pi
    while ok==1:
        ok=0

        if (x=='pi') :
            x=pi
        elif (x=='e'):
            x=e
        else:
            for i in x:
                if ok == 1:
                    x = input(" introduceti un alt numar: ")

    return float(x)

print("1. Suma")
print("2. Diferenta")
print("3. Inmultire")
print("4. Impartire")
print("5. Putere")
print("6. Modul")
print("7. N factorial")
print("8. Logaritm zecimal")
print("9. Logaritm natural")
print("10. Logaritm in baza x din n")
print("11. Functii trigonometrice")
print("12. Exponential")

istoric=[]
while True:
    choice = input("Introduceti operatia aleasa (1/2/3/4/5/6/7/8/9/10/11/12): ")
    if choice in ('1', '2', '3', '4','5','6','10'):
        nr1 = input("Introduceti primul numar: ")
        nr2 = input("Introduceti al doilea numar: ")
        nr1 = check(nr1)
        nr2 = check(nr2)
        if choice == '1':
            print(nr1, "+", nr2, "=", suma(nr1, nr2))
            istoric.append('{} + {} = {}'.format(nr1,nr2,suma(nr1, nr2)))
        elif choice == '2':
            print(nr1, "-", nr2, "=", diferenta(nr1, nr2))
            istoric.append('{} - {} = {}'.format(nr1,nr2,diferenta(nr1, nr2)))
        elif choice == '3':
            print(nr1, "*", nr2, "=", inmultire(nr1, nr2))
            istoric.append('{} * {} = {}'.format(nr1,nr2,inmultire(nr1, nr2)))
        elif choice == '4':
            print(nr1, "/", nr2, "=", impartire(nr1, nr2))
            istoric.append('{} / {} = {}'.format(nr1,nr2,impartire(nr1, nr2)))
        elif choice == '5':
            print(nr1, "**", nr2, "=", putere(nr1, nr2))
            istoric.append('{} ** {} = {}'.format(nr1, nr2, putere(nr1, nr2)))
        elif choice == '6':
            print(nr1, "%", nr2, "=", modul(nr1, nr2))
            istoric.append('{} % {} = {}'.format(nr1, nr2, modul(nr1, nr2)))
        elif choice == '10':
            print('log',nr1,'(',nr2, ") =", math.log(nr2,nr1))
            istoric.append('log {} ( {} ) = {}'.format(nr1, nr2, math.log(nr2, nr1)))
    if choice in ('7'):
        nr1 = int(input("Introduceti numarul: "))
        if choice == '7':
            print(nr1,'! =', math.factorial(nr1))
            istoric.append('{} ! = {}'.format(nr1, nr2, math.factorial(nr1, nr2)))
    if choice in ('11'):
        print("1. Sinus")
        print("2. Cosinus")
        print("3. Tangenta")
        choice = input("Introduceti functia trigonometrica (1/2/3): ")
        if choice == '1':
            nr1 = input("Introduceti numarul: ")
            nr1 = check(nr1)
            print('sin(', nr1, ') =', math.sin(math.radians(nr1)))
            istoric.append('sin( {} ) = {}'.format(nr1, math.sin(math.radians(nr1))))
        elif choice == '2':
            nr1 = input("Introduceti numarul: ")
            nr1 = check(nr1)
            print('cos(', nr1, ') =', math.cos(math.radians(nr1)))
            istoric.append('cos( {} ) = {}'.format(nr1, math.cos(math.radians(nr1))))
        elif choice == '3':
            nr1 = input("Introduceti numarul: ")
            nr1 = check(nr1)
            print('tan(', nr1, ') =', math.tan(math.radians(nr1)))
            istoric.append('tan( {} ) = {}'.format(nr1, math.tan(math.radians(nr1))))
    if choice in ('8', '9', '12'):
        nr1 = input("Introduceti numarul: ")
        nr1 = check(nr1)
        if choice == '8':
            print('log10(',nr1,') = ',math.log10(nr1))
            istoric.append('log10( {} ) = {}'.format(nr1,math.log10(nr1)))
        elif choice == '9':
            print('loge(',nr1,') = ', math.log(nr1))
            istoric.append('loge( {} ) = {}'.format(nr1, math.log(nr1)))
        elif choice == '12':
            print('e **',nr1,' =',math.exp(nr1))
            istoric.append('e ** {} = {}'.format(nr1, math.exp(nr1)))
    elif choice not in ('1', '2', '3', '4','5','6','7','8','9','10','11','12'):
        print("Operatia nu exista")
    time.sleep(2)
    urmatorul_calcul = input("Doriti sa mai calculati ceva? (da/nu): ")
    if urmatorul_calcul == "nu":
        istoric_op = input('Doriti sa vedeti istoricul operatiilor? (da/nu):')
        if istoric_op in ('da', 'nu'):
            if istoric_op == 'da':
                print('Istoricul este:', istoric[-5:])
            else:
                print('ok!')
        else:
            print('error')
        break

try:
 fisier=input('Doriti sa introduceti un fisier ca si input? (da/nu): ')
 if fisier in ('da','nu'):
     if fisier == 'da':
         fisier_input = input('Introduceti numele fisierului pe care doriti sa il cititi: ')#(ex: 2 + 1)
         f = open(fisier_input, 'r')
         print('Fisierul exista!')

         file = f.readlines()
         newList = []
         for line in file:
             if line[-1] == '\n':
                 newList.append(line[:-1])
             else:
                 newList.append(line)
         f_new = open('rezultate.txt','w')

         for i in range(0, len(newList)):
             coppy = newList
             calcul = coppy[i].split(' ')
             if len(calcul) == 3:
                 nr1 = calcul[0]
                 nr2 = calcul[2]
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

                 operatie = calcul[1]
             if len(calcul) == 2:
                 nr1 = calcul[0]
                 if nr1 == 'e':
                     nr1 = math.e
                 elif nr1 == 'pi':
                     nr1 = math.pi
                 else:
                     nr1 = float(nr1)
                 operatie = calcul[1]
             if operatie == '+':
                 A = suma(nr1, nr2)
                 f_new.write(str(A))
                 f_new.write('\n')
             elif operatie == '-':
                 f_new.write(str(diferenta(nr1, nr2)))
                 f_new.write('\n')
             elif operatie == '*':
                 P = inmultire(nr1, nr2)
                 f_new.write(str(P))
                 f_new.write('\n')
             elif operatie == '/':
                 f_new.write(str(impartire(nr1, nr2)))
                 f_new.write('\n')
             elif operatie == '%':
                 f_new.write(str(modul(nr1, nr2)))
                 f_new.write('\n')

             elif operatie == '**':
                 f_new.write(str(putere(nr1, nr2)))
                 f_new.write('\n')
             elif operatie == '!':
                 factorial = factorial(int(nr1))
                 f_new.write(str(factorial))
                 f_new.write('\n')

         f.close()
         f_new.close()
     else:
        print('ok!')
 else:
     print('error')

except FileNotFoundError:
   print('Fisierul nu exista!')
time.sleep(2)

from tkinter import *
import tkinter.messagebox

def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cos':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tan':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sin':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == chr(177):
            answer = -(float(entryField.get()))

        elif value == chr(247):
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        elif value == 'x!':
            answer = math.factorial(int(entryField.get()))

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass
def iExit():
    iExit = tkinter.messagebox.askyesno("Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
root = Tk()
root.title('Calculator')
root.config(bg='black')

calc = Frame(root)

menubar = Menu(calc)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=iExit)
root.config(menu = menubar)

frame=Frame(root , bg = 'black', bd = 5, height = 100, relief = RAISED, width = 100 )
frame.grid(row = 0, column = 0, padx = 5, pady = 5)

entryField = Entry(frame,bg='grey',relief=SUNKEN,justify = RIGHT,width=36)
entryField.grid(row = 0, column = 0, columnspan=5)

button_text_list = ['sin','cos','tan','CE','C','π','e', "√",chr(8731),'%',"x\u00B2",'(',')','x!',chr(247),"x\u00B3",'7','8','9','*','x\u02b8','4','5','6','-','log₁₀','1','2','3','+','ln',chr(177),"0", ".","="]
rowvalue=1
columnvalue=0
for i in button_text_list:
    if columnvalue<=4:
        if columnvalue >= 1 and columnvalue <= 3:
            if rowvalue <=3:
                button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                            activebackground='grey', command=lambda button=i: click(button))
                button.grid(row=rowvalue, column=columnvalue, pady=0)
            if rowvalue >=4 and rowvalue<=6:
                button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='orange', fg='white',
                            activebackground='grey', command=lambda button=i: click(button))
                button.grid(row=rowvalue, column=columnvalue, pady=0)
            if columnvalue==1 and rowvalue==7:
                button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                            activebackground='grey', command=lambda button=i: click(button))
                button.grid(row=rowvalue, column=columnvalue, pady=0)
            if columnvalue == 2 and rowvalue == 7:
                button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='orange', fg='white',
                            activebackground='grey', command=lambda button=i: click(button))
                button.grid(row=rowvalue, column=columnvalue, pady=0)
            if columnvalue == 3 and rowvalue == 7:
                button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                            activebackground='grey', command=lambda button=i: click(button))
                button.grid(row=rowvalue, column=columnvalue, pady=0)
        else:
            button = Button(frame, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                    activebackground='grey', command=lambda button=i: click(button))
            button.grid(row=rowvalue, column=columnvalue, pady=0)
        columnvalue+=1
    if columnvalue>4:
        rowvalue+=1
        columnvalue=0

root.mainloop()
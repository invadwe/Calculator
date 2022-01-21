from tkinter import*
import math
e=math.e
pi=math.pi
root=Tk()
root.title("Calculator folosind PyCharm")
root.geometry=("820x1000+600+60")

calc=Frame(root, bd=20, pady=5,bg='Blue',relief=RIDGE)
calc.grid()

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input=set(operator)

class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value=True
        self.check_sum=False
        self.op=""
        self.result=False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)



    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
    def operation(self, op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False

    def valid_function(self):
        if self.op=="Add":
            self.total+=self.current
        if self.op=="Sub":
            self.total-=self.current
        if self.op=="Multiple":
            self.total*=self.current
        if self.op == "Divide":
            self.total /= self.current

        if self.op=="Dot":
            self.total, =self.current
        if self.op == "mod":
            self.total %= self.current

        self.input_vlue=True
        self.check_sum=False
        self.display(self.total)



    def Clear_Entry(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input_value=True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def delectBS(self):
        numLen=len(txtDisplay.get())
        txtDisplay.delete(numLen - 1, 'end')
        if numLen==1:
            txtDisplay.insert(0,"0")

    def display(self, value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0, value)



    def mathsPM(self):
        self.result=False
        self.current=-(float(txtDisplay.get()))
        self.display(self.current)
    def squared(self):
       self.result=False
       self.current=math.sqrt(float(txtDisplay.get()))
       self.display(self.current)

    def cos(self):
       self.result=False
       self.current=math.cos(math.radians(float(txtDisplay.get())))
       self.display(self.current)

    def sin(self):
       self.result=False
       self.current=math.sin(math.radians(float(txtDisplay.get())))
       self.display(self.current)

    def tan(self):
       self.result=False
       self.current = math.tan(math.radians(float(txtDisplay.get())))
       self.display(self.current)

    def log10(self):
        self.result=False
        self.current=math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result=False
        self.current=math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result=False
        self.current=math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def pi(self):
        self.result=False
        self.current=math.pi
        self.display(self.current)

    def log1p(self):
        self.result=False
        self.current=math.log1p(float(txtDisplay.get()))
        self.display(self.current)

    def e(self):
        self.result=False
        self.current=math.e
        self.display(self.current)

    def abs(self):
        self.result = False
        self.current = math.fabs(float(txtDisplay.get()))
        self.display(self.current)



    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def pow(self):
        self.power=2
        self.result = False
        self.current = math.pow(float(txtDisplay.get()),2)
        self.display(self.current)

    def atan(self):
        self.result = False
        self.current = math.atan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def factorial(self):
        self.result = False
        self.current=math.factorial(int(txtDisplay.get()))
        self.display(self.current)

    def mod(self, other):
        self.result=False
        self.current = math.modf(int(txtDisplay.get()))
        self.display(self.current)



added_value=Calc()


txtDisplay=Entry(calc, font=('arial',20,'bold'), bd=20,bg='Magenta' ,width=28, justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")


numberpad='789456123'
i=0
btn=[]

for j in range(3,6):
    for k in range(3):
        btn.append(Button (calc, width=6, height=2, font=('Bradley Hand ITC',22,'bold'),bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k,pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x) 
        i=i+1
#=====================================================================================================================
btnDelete=Button(calc, width=6, height=2, text="DEL", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.delectBS ).grid(row=1, column=0, pady=1)
btnClear=Button(calc, width=6, height=2, text="C", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.Clear_Entry ).grid(row=1, column=1, pady=1)
btnClearAll=Button(calc, width=6, height=2, text="CE", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.all_Clear_Entry).grid(row=1, column=2, pady=1)
btnPM=Button(calc, width=6, height=2, text=chr(177), font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.mathsPM).grid(row=1, column=3, pady=1)
#======================================================================================================================

btnSquare=Button(calc, width=6, height=2, text="√", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.squared).grid(row=2, column=0, pady=1)
btnCos=Button(calc, width=6, height=2, text="Cos", font=('arial',20,'bold'),bd=4, bg="Pink",command=added_value.cos).grid(row=2, column=1, pady=1)
btnTan=Button(calc, width=6, height=2, text="Tan", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.tan).grid(row=2, column=2, pady=1)
btnSin=Button(calc,width=6, height=2, text="Sin", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.sin).grid(row=2,column=3,pady=1)
#======================================================================================================================
btnAdd=Button(calc, width=6, height=2, text="+", font=('arial',20,'bold'), bd=4, bg="Pink",command=lambda:added_value.operation('Add')).grid(row=3, column=3, pady=1)
btnSub=Button(calc, width=6, height=2, text="-", font=('arial',20,'bold'), bd=4, bg="Green",command=lambda:added_value.operation("Sub")).grid(row=4, column=3, pady=1)
btnMultiple=Button(calc, width=6, height=2, text="*", font=('arial',20,'bold'), bd=4, bg="Magenta",command=lambda:added_value.operation("Multiple")).grid(row=5, column=3, pady=1)
btnDivide=Button(calc, width=6, height=2, text=chr(247), font=('arial',20,'bold'), bd=4, bg="Pink",command=lambda:added_value.operation("Divide")).grid(row=6, column=3, pady=1)
#======================================================================================================================
btnDot=Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Pink", command=lambda:added_value.numberEnter(".")).grid(row=6, column=1, pady=1)
btnEquals=Button(calc, width=6, height=2, text="=", font=('arial',20,'bold'), bd=4, bg="Pink",command=added_value.sum_of_total).grid(row=6, column=2, pady=1)
btnZero=Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Pink", command=lambda:added_value.numberEnter(0)).grid(row=6, column=0, pady=1)
btnE=Button(calc, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gray", command=added_value.e).grid(row=6, column=4, pady=1)
#======================================================================================================================
btnLog2=Button(calc, text='log2', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gainsboro", command=added_value.log2).grid(row=7, column=0, pady=1)
btnLog10=Button(calc, text='log10', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gainsboro", command=added_value.log10).grid(row=7, column=1, pady=1)
btnDeg=Button(calc, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gainsboro", command=added_value.degrees).grid(row=7, column=2, pady=1)
btnPi=Button(calc, text='π', width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="gainsboro", command=added_value.pi).grid(row=7, column=3, pady=1)

btnExp=Button(calc, text="exp", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Dark Blue", command=added_value.exp).grid(row=4, column=4, pady=1)
btnAbs=Button(calc, text='abs',width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Dark Blue", command=added_value.abs).grid(row=5, column=4, pady=1)
defPow=Button(calc, text='x^2',width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="Dark Blue", command=added_value.pow).grid(row=3, column=4, pady=1)
btnMod=Button(calc, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="Pink", command=lambda:added_value.operation("mod")).grid(row=1, column=4, pady=1)

btnatan=Button(calc,text='ctg',width=6,height=2,font=('arial',20,'bold'),bd=4,bg='dark blue', command=added_value.atan).grid(row=2,column=4,pady=1)
btnFactorial=Button(calc,text='n!',width=6,height=2,font=('arial',20,'bold'), bd=4,bg='dark blue',command=added_value.factorial).grid(row=7,column=4,pady=1)
#======================================================================================================================
root.mainloop()

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

                if i in ('1', '2', '3', '4', '5', '6', '9', '7', '8', '9'):
                    o = 1
                else:
                    ok = 1
            if ok == 1:
                x = input(" introduceti un alt numar: ")

    return float(x)




def adunare(x, y):
    return x + y



def scadere(x, y):
    return x - y


def inmultire(x, y):
    return x * y


def impartire(x, y):
    return x / y

def log2(x):
    return math.log2(x)

def factorial(x):
    return math.factorial(x)

def logn(x,base):
    return math.log(x, base)

def log10(x):
    return math.log10(x)

def log(x):
    return math.log(x)

def exp(x):
    return math.exp(x)

def pow(x,y):
    return math.pow(x,y)

def fmod(x,y):
    return math.fmod(x,y)

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def atan(x):
    return math.atan(x)

print("1.Adunare")
print("2.Scadere")
print("3.Inmultire")
print("4.Impartire")
print("5.Logaritm in baza 2")
''''print("6.Factorial")'''''
print("6.Logartitm din x in baza n")
print("7.Logaritm in baza 10 din x")
print("8.logatritm in baza e din x")
print("9.Exponentiala (e la puterea x)")
print('10.Pow')
print('11.Mod')
print('12.Sin')
print('13.Cos')
print('14.Tan')
print('15.Ctg')
print('16.Factorial')

while True:


    choice = input("Introduceti optiunea aleasa (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16):")


    if choice in ('1', '2', '3', '4','6','10','11'):
        numar1 = input("Introduceti primul numar: ")
        numar1=check(numar1)
        numar2 = input("Introduceti al doilea numar: ")
        numar2=check(numar2)

        if choice == '1':
            print(float(numar1), "+", float(numar2), "=", adunare(numar1, numar2))

        elif choice == '2':
             print(numar1, "-", numar2, "=", scadere(numar1,numar2))

        elif choice == '3':
            print(numar1, "*", numar2, "=", inmultire(numar1, numar2))

        elif choice == '4':
            if numar2==0:
                print('Operatia nu poate sa fie efectuata')
            else:
               print(numar1, "/", numar2, "=", impartire(numar1, numar2))

        elif choice=='6':
             print("logaritm in baza", numar2,'din',numar1, logn(numar1,numar2))

        elif choice=="10":
             print('x',numar1,'^',numar2,pow(numar1,numar2))

        elif choice=='11':
             print('retul impartirii lui ', numar1, 'la', numar2,'este',fmod(numar1,numar2))





    if choice in ('5','7','8','9','12','13','14','15'):
        numar3=input('Introduceti al 3-lea numar')
        numar3=check(numar3)

        if choice=='5':
            print("Logaritm in baza 2 din x este:",numar3,"=",log2(numar3))

        elif choice=='7':
              print('Logaritm in baza 10 din ',numar3,'=',log10(numar3))

        elif choice=='8':
             print("Logaritm in baza e","din",numar3,"=",log(numar3))

        elif choice=='9':
             print("e la puterea ", numar3,'egal', exp(numar3))

        elif choice=='12':
              print('sin de',numar3,'egal',sin(numar3))

        elif choice=='13':
             print('cos de',numar3,'egal',cos(numar3))

        elif choice=='14':
             print('tan de',numar3,'egal',tan(numar3))

        elif choice == '15':
             print('ctg de', numar3, 'egal', 1/tan(numar3))




    next_calculation = input("Doriti sa faceti operatia urmatoare??? (da/nu): ")
    if next_calculation == "nu":
       break

    if choice in ('16'):
        numar4=int(input('Al 4-lea nr este'))
        if choice=='16':
            print("factorialul numarului este",factorial(numar4))
            if next_calculation == "nu":
                break

    else:
        print('Eroare')

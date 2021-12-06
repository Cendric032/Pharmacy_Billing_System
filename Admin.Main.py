from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("Pharmacy Billing System")
root.configure(background='light blue')

Tops = Frame(root,bg='light blue',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('arial',60,'bold'),text='Pharmacy Billing System',bd=21,bg='black',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='light blue',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='light blue',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='light blue',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='light blue',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='light blue',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='light blue',bd=4)
Cost_F.pack(side=BOTTOM)
PainReliever_F=Frame(MenuFrame,bg='light blue',bd=4)
PainReliever_F.pack(side=TOP)


PainReliever_F=Frame(MenuFrame,bg='light blue',bd=4,relief=RIDGE)
PainReliever_F.pack(side=LEFT)
Vitamins_F=Frame(MenuFrame,bg='light blue',bd=4,relief=RIDGE)
Vitamins_F.pack(side=RIGHT)


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofVitamins = StringVar()
CostofPainReliever = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Biogesic = StringVar()
E_Alaksan = StringVar()
E_Dolfenal = StringVar()
E_Medicol = StringVar()
E_Ibuprofen = StringVar()
E_Aspirin = StringVar()
E_Naproxen = StringVar()
E_BioFlu = StringVar()

E_Ascorbic_Acid = StringVar()
E_Conzace = StringVar()
E_Calciumade = StringVar()
E_Enervon = StringVar()
E_ImmunoPro = StringVar()
E_Maxvit = StringVar()
E_NutriBest = StringVar()
E_Revicon_Forte = StringVar()

E_Biogesic.set("0")
E_Alaksan.set("0")
E_Dolfenal.set("0")
E_Medicol.set("0")
E_Ibuprofen.set("0")
E_Aspirin.set("0")
E_Naproxen.set("0")
E_BioFlu.set("0")

E_Ascorbic_Acid.set("0")
E_Conzace.set("0")
E_Calciumade.set("0")
E_Enervon.set("0")
E_ImmunoPro.set("0")
E_Maxvit.set("0")
E_NutriBest.set("0")
E_Revicon_Forte.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofVitamins.set("")
    CostofPainReliever.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)

    E_Biogesic.set("0")
    E_Alaksan.set("0")
    E_Dolfenal.set("0")
    E_Medicol.set("0")
    E_Ibuprofen.set("0")
    E_Aspirin.set("0")
    E_Naproxen.set("0")
    E_BioFlu.set("0")

    E_Ascorbic_Acid.set("0")
    E_Conzace.set("0")
    E_Calciumade.set("0")
    E_Enervon.set("0")
    E_ImmunoPro.set("0")
    E_Maxvit.set("0")
    E_NutriBest.set("0")
    E_Revicon_Forte.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtBiogesic.configure(state=DISABLED)
    txtAlaksan.configure(state=DISABLED)
    txtDolfenal.configure(state=DISABLED)
    txtMedicol.configure(state=DISABLED)
    txtIbuprofen.configure(state=DISABLED)
    txtAspirin.configure(state=DISABLED)
    txtNaproxen.configure(state=DISABLED)
    txtBioFlu.configure(state=DISABLED)
    txtAscorbic_Acid.configure(state=DISABLED)
    txtConzace.configure(state=DISABLED)
    txtCalciumade.configure(state=DISABLED)
    txtEnervon.configure(state=DISABLED)
    txtImmunoPro.configure(state=DISABLED)
    txtMaxvit.configure(state=DISABLED)
    txtNutriBest.configure(state=DISABLED)
    txtRevicon_Forte.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Biogesic.get())
    Item2=float(E_Alaksan.get())
    Item3=float(E_Dolfenal.get())
    Item4=float(E_Medicol.get())
    Item5=float(E_Ibuprofen.get())
    Item6=float(E_Aspirin.get())
    Item7=float(E_Naproxen.get())
    Item8=float(E_BioFlu.get())

    Item9=float(E_Ascorbic_Acid.get())
    Item10=float(E_Conzace.get())
    Item11=float(E_Calciumade.get())
    Item12=float(E_Enervon.get())
    Item13=float(E_ImmunoPro.get())
    Item14=float(E_Maxvit.get())
    Item15=float(E_NutriBest.get())
    Item16=float(E_Revicon_Forte.get())

    PriceofPainReliever =(Item1 * 6) + (Item2 * 8) + (Item3 * 12) + (Item4 * 12) + (Item5 * 15) + (Item6 * 10) + (Item7 * 15) + (Item8 * 7)

    PriceofVitamins =(Item9 * 20) + (Item10 * 15) + (Item11 * 15) + (Item12 * 13) + (Item13 * 30) + (Item14 * 25) + (Item15 * 40) + (Item16 * 20)



    PainRelieverPrice = "P" + str('%.2f' % PriceofPainReliever)
    VitaminsPrice =  "P" + str('%.2f' % PriceofVitamins)
    CostofVitamins.set(VitaminsPrice)
    CostofPainReliever.set(PainRelieverPrice)
    SC = "P" + str('%.2f'% 1.59)
    ServiceCharge.set(SC)

    SubTotalofITEMS = "P" + str('%.2f'%(PriceofPainReliever + PriceofVitamins + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "P" + str('%.2f'%((PriceofPainReliever + PriceofVitamins + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofPainReliever + PriceofVitamins + 1.59) * 0.15)
    TC="P" + str('%.2f'%(PriceofPainReliever + PriceofVitamins + 1.59 + TT))
    TotalCost.set(TC)


def chk_Biogesic():
    if(var1.get() == 1):
        txtBiogesic.configure(state = NORMAL)
        txtBiogesic.focus()
        txtBiogesic.delete('0',END)
        E_Biogesic.set("")
    elif(var1.get() == 0):
        txtBiogesic.configure(state = DISABLED)
        E_Biogesic.set("0")

def chk_Alaksan():
    if(var2.get() == 1):
        txtAlaksan.configure(state = NORMAL)
        txtAlaksan.focus()
        txtAlaksan.delete('0',END)
        E_Alaksan.set("")
    elif(var2.get() == 0):
        txtAlaksan.configure(state = DISABLED)
        E_Alaksan.set("0")

def chk_Dolfenal():
    if(var3.get() == 1):
        txtDolfenal.configure(state = NORMAL)
        txtDolfenal.delete('0',END)
        txtDolfenal.focus()
    elif(var3.get() == 0):
        txtDolfenal.configure(state = DISABLED)
        E_Dolfenal.set("0")

def chk_Medicol():
    if(var4.get() == 1):
        txtMedicol.configure(state = NORMAL)
        txtMedicol.delete('0',END)
        txtMedicol.focus()
    elif(var4.get() == 0):
        txtMedicol.configure(state = DISABLED)
        E_Medicol.set("0")

def chk_Ibuprofen():
    if(var5.get() == 1):
        txtIbuprofen.configure(state = NORMAL)
        txtIbuprofen.delete('0',END)
        txtIbuprofen.focus()
    elif(var5.get() == 0):
        txtIbuprofen.configure(state = DISABLED)
        E_Ibuprofen.set("0")

def chk_Aspirin():
    if(var6.get() == 1):
        txtAspirin.configure(state = NORMAL)
        txtAspirin.delete('0',END)
        txtAspirin.focus()
    elif(var6.get() == 0):
        txtAspirin.configure(state = DISABLED)
        E_Aspirin.set("0")

def chk_Naproxen():
    if(var7.get() == 1):
        txtNaproxen.configure(state = NORMAL)
        txtNaproxen.delete('0',END)
        txtNaproxen.focus()
    elif(var7.get() == 0):
        txtNaproxen.configure(state = DISABLED)
        E_Naproxen.set("0")

def chk_BioFlu():
    if(var8.get() == 1):
        txtBioFlu.configure(state = NORMAL)
        txtBioFlu.delete('0',END)
        txtBioFlu.focus()
    elif(var8.get() == 0):
        txtBioFlu.configure(state = DISABLED)
        E_BioFlu.set("0")

def chk_Ascorbic_Acid():
    if(var9.get() == 1):
        txtAscorbic_Acid.configure(state = NORMAL)
        txtAscorbic_Acid.delete('0',END)
        txtAscorbic_Acid.focus()
    elif(var9.get() == 0):
        txtAscorbic_Acid.configure(state = DISABLED)
        E_Ascorbic_Acid.set("0")

def chk_Conzace():
    if(var10.get() == 1):
        txtConzace.configure(state = NORMAL)
        txtConzace.delete('0',END)
        txtConzace.focus()
    elif(var10.get() == 0):
        txtConzace.configure(state = DISABLED)
        E_Conzace.set("0")

def chk_Calciumade():
    if(var11.get() == 1):
        txtCalciumade.configure(state = NORMAL)
        txtCalciumade.delete('0',END)
        txtCalciumade.focus()
    elif(var11.get() == 0):
        txtCalciumade.configure(state = DISABLED)
        E_Calciumade.set("0")

def chk_Enervon():
    if(var12.get() == 1):
        txtEnervon.configure(state = NORMAL)
        txtEnervon.delete('0',END)
        txtEnervon.focus()
    elif(var12.get() == 0):
        txtEnervon.configure(state = DISABLED)
        E_Enervon.set("0")

def chk_ImmunoPro():
    if(var13.get() == 1):
        txtImmunoPro.configure(state = NORMAL)
        txtImmunoPro.delete('0',END)
        txtImmunoPro.focus()
    elif(var13.get() == 0):
        txtImmunoPro.configure(state = DISABLED)
        E_ImmunoPro.set("0")

def chk_Maxvit():
    if(var14.get() == 1):
        txtMaxvit.configure(state = NORMAL)
        txtMaxvit.delete('0',END)
        txtMaxvit.focus()
    elif(var14.get() == 0):
        txtMaxvit.configure(state = DISABLED)
        E_Maxvit.set("0")

def chk_NutriBest():
    if(var15.get() == 1):
        txtNutriBest.configure(state = NORMAL)
        txtNutriBest.delete('0',END)
        txtNutriBest.focus()
    elif(var15.get() == 0):
        txtNutriBest.configure(state = DISABLED)
        E_NutriBest.set("0")

def chk_Revicon_Forte():
    if(var16.get() == 1):
        txtRevicon_Forte.configure(state = NORMAL)
        txtRevicon_Forte.delete('0',END)
        txtRevicon_Forte.focus()
    elif(var16.get() == 0):
        txtRevicon_Forte.configure(state = DISABLED)
        E_Revicon_Forte.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Biogesic:\t\t\t\t\t' + E_Biogesic.get() +'\n')
    txtReceipt.insert(END,'Alaksan:\t\t\t\t\t'+ E_Alaksan.get()+'\n')
    txtReceipt.insert(END,'Dolfenal:\t\t\t\t\t'+ E_Dolfenal.get()+'\n')
    txtReceipt.insert(END,'Medicol:\t\t\t\t\t'+ E_Medicol.get()+'\n')
    txtReceipt.insert(END,'Ibuprofen:\t\t\t\t\t'+ E_Ibuprofen.get()+'\n')
    txtReceipt.insert(END,'Aspirin:\t\t\t\t\t'+ E_Aspirin.get()+'\n')
    txtReceipt.insert(END,'Naproxen:\t\t\t\t\t'+ E_Naproxen.get()+'\n')
    txtReceipt.insert(END,'BioFlu:\t\t\t\t\t'+ E_BioFlu.get()+'\n')
    txtReceipt.insert(END,'Ascorbic_Acid:\t\t\t\t\t'+ E_Ascorbic_Acid.get()+'\n')
    txtReceipt.insert(END,'Conzace:\t\t\t\t\t'+ E_Conzace.get()+'\n')
    txtReceipt.insert(END,'Calciumade:\t\t\t\t\t'+ E_Calciumade.get()+'\n')
    txtReceipt.insert(END,'Enervon:\t\t\t\t\t'+ E_Enervon.get()+'\n')
    txtReceipt.insert(END,'ImmunoPro:\t\t\t\t\t'+ E_ImmunoPro.get()+'\n')
    txtReceipt.insert(END,'Maxvit:\t\t\t\t\t'+ E_Maxvit.get()+'\n')
    txtReceipt.insert(END,'NutriBest:\t\t\t\t\t'+ E_NutriBest.get()+'\n')
    txtReceipt.insert(END,'Revicon_Forte:\t\t\t\t\t'+ E_Revicon_Forte.get()+'\n')
    txtReceipt.insert(END,'Cost of PainReliever:\t\t\t\t\t'+ CostofPainReliever.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Vitamins:\t\t\t\t'+ CostofVitamins.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


Biogesic=Checkbutton(PainReliever_F,text='Biogesic',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Biogesic).grid(row=0,sticky=W)
Alaksan=Checkbutton(PainReliever_F,text='Alaksan',variable=var2,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Alaksan).grid(row=1,sticky=W)
Dolfenal=Checkbutton(PainReliever_F,text='Dolfenal',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Dolfenal).grid(row=2,sticky=W)
Medicol=Checkbutton(PainReliever_F,text='Medicol',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Medicol).grid(row=3,sticky=W)
Ibuprofen=Checkbutton(PainReliever_F,text='Ibuprofen',variable=var5,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Ibuprofen).grid(row=4,sticky=W)
Aspirin=Checkbutton(PainReliever_F,text='Aspirin',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Aspirin).grid(row=5,sticky=W)
Naproxen=Checkbutton(PainReliever_F,text='Naproxen',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_Naproxen).grid(row=6,sticky=W)
BioFlu=Checkbutton(PainReliever_F,text='BioFlu',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='light blue',command=chk_BioFlu).grid(row=7,sticky=W)

txtBiogesic = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Biogesic)
txtBiogesic.grid(row=0,column=1)

txtAlaksan = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Alaksan)
txtAlaksan.grid(row=1,column=1)

txtDolfenal = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Dolfenal)
txtDolfenal.grid(row=2,column=1)

txtMedicol= Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Medicol)
txtMedicol.grid(row=3,column=1)

txtIbuprofen = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Ibuprofen)
txtIbuprofen.grid(row=4,column=1)

txtAspirin = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Aspirin)
txtAspirin.grid(row=5,column=1)

txtNaproxen = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Naproxen)
txtNaproxen.grid(row=6,column=1)

txtBioFlu = Entry(PainReliever_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_BioFlu)
txtBioFlu.grid(row=7,column=1)

Ascorbic_Acid = Checkbutton(Vitamins_F,text="Ascorbic_Acid\t\t\t ",variable=var9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Ascorbic_Acid).grid(row=0,sticky=W)
Conzace = Checkbutton(Vitamins_F,text="Conzace",variable=var10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Conzace).grid(row=1,sticky=W)
Calciumade = Checkbutton(Vitamins_F,text="Calciumade ",variable=var11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Calciumade).grid(row=2,sticky=W)
Enervon = Checkbutton(Vitamins_F,text="Enervon ",variable=var12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Enervon).grid(row=3,sticky=W)
ImmunoPro = Checkbutton(Vitamins_F,text="ImmunoPro ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_ImmunoPro).grid(row=4,sticky=W)
Maxvit = Checkbutton(Vitamins_F,text="Maxvit ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Maxvit).grid(row=5,sticky=W)
NutriBest = Checkbutton(Vitamins_F,text="NutriBest ",variable=var15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_NutriBest).grid(row=6,sticky=W)
Revicon_Forte = Checkbutton(Vitamins_F,text="Revicon ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='light blue',command=chk_Revicon_Forte).grid(row=7,sticky=W)

txtAscorbic_Acid=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Ascorbic_Acid)
txtAscorbic_Acid.grid(row=0,column=1)

txtConzace=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Conzace)
txtConzace.grid(row=1,column=1)

txtCalciumade=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Calciumade)
txtCalciumade.grid(row=2,column=1)

txtEnervon=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Enervon)
txtEnervon.grid(row=3,column=1)

txtImmunoPro=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_ImmunoPro)
txtImmunoPro.grid(row=4,column=1)

txtMaxvit=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Maxvit)
txtMaxvit.grid(row=5,column=1)

txtNutriBest=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_NutriBest)
txtNutriBest.grid(row=6,column=1)

txtRevicon_Forte=Entry(Vitamins_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Revicon_Forte)
txtRevicon_Forte.grid(row=7,column=1)

lblCostofPainReliever=Label(Cost_F,font=('arial',14,'bold'),text='Cost of PainReliever\t',bg='light blue',
                fg='black',justify=CENTER)
lblCostofPainReliever.grid(row=0,column=0,sticky=W)
txtCostofPainReliever=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofPainReliever)
txtCostofPainReliever.grid(row=0,column=1)

lblCostofVitamins=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Vitamins  ',bg='light blue',
                fg='black',justify=CENTER)
lblCostofVitamins.grid(row=1,column=0,sticky=W)
txtCostofVitamins=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofVitamins)
txtCostofVitamins.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='light blue',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='light blue',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='light blue',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='light blue',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='light blue',command=iExit).grid(row=0,column=3)




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='light blue',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='light blue',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='light blue',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='light blue',command=lambda:btnClick('+')).grid(row=2,column=3)
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='light blue',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='light blue',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='light blue',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='light blue',command=lambda:btnClick('-')).grid(row=3,column=3)
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='light blue',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='light blue',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='light blue',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='light blue',command=lambda:btnClick('*')).grid(row=4,column=3)
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='light blue',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='light blue',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='light blue',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='light blue',command=lambda:btnClick('/')).grid(row=5,column=3)







root.mainloop()

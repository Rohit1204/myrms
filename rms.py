from tkinter import *
import random
from csv import DictWriter
import os
root = Tk()
root.title("restaurant Management system")
root.geometry("1000x700")
root.configure(bg="grey26")
#photo=PhotoImage(file="hotel4.png")
label=Label(root,bg="grey26").place(x=730,y=300)
global randomref
#############################################################################################################################################

#frame
topframe = Frame(root,bg="grey26",height=100,width=1000,relief="raise",bd=8)
topframe.pack(side = TOP)
bottomlframe = Frame(root,bg="grey26",height=600,width=700,relief="raise",bd=8)
bottomlframe.pack(side = LEFT)
##############################################################################################################################################

#Label
lblInfo= Label(topframe,font=('Helvetica',30,'bold'),text='Restaurant Management System',bd=8,bg="grey26",fg="Red",anchor='w').place(x=300,y=10)
label=Label(bottomlframe,text="Reference",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=80)
label=Label(bottomlframe,text="Large Fries",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=160)
label=Label(bottomlframe,text="Burger Meal",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=220)
label=Label(bottomlframe,text="Filet_o_Meal",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=280)
label=Label(bottomlframe,text="Chicken Meal",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=340)
label=Label(bottomlframe,text="Cheese meal",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=10,y=400)
label=Label(bottomlframe,text="Drinks",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=80)
label=Label(bottomlframe,text="Cost of meal",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=160)
label=Label(bottomlframe,text="Service Charge",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=220)
label=Label(bottomlframe,text="State Tax",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=280)
label=Label(bottomlframe,text="Sub total",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=340)
label=Label(bottomlframe,text="Total Cost",font=('Helvetica',16,'bold'),bg="grey26",fg="skyblue").place(x=300,y=400)
###############################################################################################################################################

#datatype declare
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
h=StringVar()
i=StringVar()
j=StringVar()
k=StringVar()
l=StringVar()
################################################################################################################################################


#Entry
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=a).place(x=150,y=85)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=b).place(x=150,y=165)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=c).place(x=150,y=225)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=d).place(x=150,y=285)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=e).place(x=150,y=345)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=f).place(x=150,y=405)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=g).place(x=500,y=85)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=h).place(x=500,y=165)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=i).place(x=500,y=225)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=j).place(x=500,y=285)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=k).place(x=500,y=345)
entry=Entry(bottomlframe,bd=4,width=13,bg='white',relief="raise",textvariable=l).place(x=500,y=405)
###################################################################################################
randomref=StringVar()

def sum():
    global randomref
    x=random.randint(10,99)
    y="abcdefghijklmnopqrstuvwxyz"
    z="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    randomref=str(x)
    a.set(randomref+random.choice(y)+random.choice(z)+str(random.randint(10,99)))
####################calculation#####################################################################
    coF=float(b.get())
    coD=float(c.get())
    coFilet=float(d.get())
    coBurger=float(e.get())
    coChicburger=float(f.get())
    coCheese_Burger=float(g.get())

    CostofFries=coF*45
    costofDrinks=coD*60
    costofFilet=coFilet*70
    cosrofburger=coBurger*45
    costChicken_burger=coChicburger*75
    costcheese_burger=coCheese_Burger*55

    costofMeal=str('%.2f'%(CostofFries+costofDrinks+costofFilet+
                                cosrofburger+costChicken_burger+costcheese_burger))
    PayTax=((CostofFries+costofDrinks+costofFilet+cosrofburger+
             costChicken_burger+costcheese_burger)*0.2)
    ser_charge=((CostofFries+costofDrinks+costofFilet+cosrofburger+
                 costChicken_burger+costcheese_burger)/99)
    Total=((CostofFries+costofDrinks+costofFilet+cosrofburger+
                 costChicken_burger+costcheese_burger))
    
    service=str('%.2f'% ser_charge)
    paidTax=str('%.2f'% PayTax)
    overallcost=str('%.2f'% (PayTax+Total+ser_charge))

    h.set("Rs :"+costofMeal+"/-")
    i.set("Rs :"+service+"/-")
    j.set("Rs :"+paidTax+"/-")
    k.set("Rs :"+costofMeal+"/-")
    l.set("Rs :"+overallcost+"/-")
            

def re():
    a.set(" ")
    b.set(" ")
    c.set(" ")
    d.set(" ")
    e.set(" ")
    f.set(" ")
    g.set(" ")
    h.set("Rs"+" ")
    i.set("Rs"+" ")
    j.set("Rs"+" ")
    k.set("Rs"+" ")
    l.set("Rs"+" ")

def exit():
    root.destroy()

def print():
    lev=Toplevel(root)
    lev.title("Final Bill")
    lev.configure(bg="light grey")
    lev.geometry('300x400')
    lab=Label(lev,text="**********************BILL***********************",fg="Red",bg="sky blue").pack()
    def ok():
        with open("RMS.csv","a") as f:
            
             dict_writer=DictWriter(f,fieldnames=["Reference","Large Fries","Burger Meal","Filet_o_Meal","Chicken Meal","Cheese meal","Drinks","Cost of meal",
                                             "Service Charge","State Tax","Sub total","Total Cost"])
             if os.stat("RMS.csv").st_size==0:
                dict_writer.writeheader()
             dict_writer.writerow({"Reference":a.get(),"Large Fries":b.get(),"Burger Meal":c.get(),"Filet_o_Meal":d.get(),"Chicken Meal":e.get(),"Cheese meal":f.get(),
                              "Drinks":g.get(),"Cost of meal":h.get(),"Service Charge":i.get(),"State Tax":j.get(),"Sub total":k.get(),"Total Cost":l.get()})
             f.close()
            
    bt=Button(lev,text="Ok",padx=10,pady=10,bd=4,fg="blue",width=15,relief="raise",command=ok).place(x=100,y=350)
    lab=Label(lev,text="Referencestr :"+a.get()+"\nLarge Fries :"+b.get()+"\nBurger Meal "+c.get()+"\nFilet_o_Meal :"+d.get()+"\nChicken Meal :"+e.get()
              +"\nCheese meal :"+f.get()+"\nDrinks :"+g.get()+"\n\nCost of meal :"+h.get()+"\nService Charge :"+i.get()+"\nState Tax :"+j.get()
              +"\nSub total :"+k.get()+"\n\n\n\nTotal Cost :"+l.get(),font=('Helvetica',12),bg="lightgrey").pack()

    root.mainloop()
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Large Fries", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="45", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="45", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Filet_o_meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="75", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="55", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="60", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)
    
############################################################################################################################################    
    

#button
btnTotal=Button(bottomlframe,pady=8,padx=8,bd=8,fg='red',font=('Helvetica',18,'bold'),width=5,text="Total",command=sum).place(x=80,y=500)
btnTotal=Button(bottomlframe,pady=8,padx=8,bd=8,fg='red',font=('Helvetica',18,'bold'),width=5,text="Reset",command=re).place(x=230,y=500)
btnTotal=Button(bottomlframe,pady=8,padx=8,bd=8,fg='red',font=('Helvetica',18,'bold'),width=5,text="Quit",command=exit).place(x=380,y=500)
btnTotal=Button(root,pady=8,padx=8,bd=8,fg='red',font=('Helvetica',18,'bold'),width=5,text="Print",command=print).place(x=750,y=600)
btnTotal=Button(root,pady=8,padx=8,bd=8,fg='red',font=('Helvetica',18,'bold'),width=5,text="Price",command=price).place(x=520,y=650)



root.mainloop()

from tkinter import *

root=Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_dosa.delete(0,END)
    entry_Idli.delete(0,END)
    entry_PavBaji.delete(0,END)
    entry_Biryani.delete(0,END)
    entry_Mandi.delete(0,END)
    entry_Noodles.delete(0,END)
    entry_Momos.delete(0,END)
    entry_Burger.delete(0,END)

def Total():
    try:a1=int(dosa.get())
    except: a1=0

    try:a2=int(Idli.get())
    except: a2=0

    try:a3=int(PavBaji.get())
    except: a3=0

    try:a4=int(Biryani.get())
    except: a4=0

    try:a5=int(Mandi.get())
    except: a5=0

    try:a6=int(Noodles.get())
    except: a6=0

    try:a7=int(Momos.get())
    except: a7=0

    try:a8=int(Burger.get())
    except: a8=0

    c1=60*a1
    c2=50*a2
    c3=80*a3
    c4=230*a4
    c5=650*a5
    c6=120*a6
    c7=140*a7
    c8=160*a8

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)

#bill
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill=Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)


    


Label(text="BILL MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

#menu card
f=Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)

Label(f,text="MENU",font=("Gabriola",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Dosa..........Rs.60/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Idli............Rs.50/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="PavBaji....Rs.80/plate",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Biryani....Rs.230/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Mandi......Rs.650/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Noodles....Rs.120/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Momos.....Rs.140/plate",fg="black",bg="lightgreen").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Burger.....Rs.160/plate",fg="black",bg="lightgreen").place(x=10,y=290)


#Entry work

f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

dosa=StringVar()
Idli=StringVar()
PavBaji=StringVar()
Biryani=StringVar()
Mandi=StringVar()
Noodles=StringVar()
Momos=StringVar()
Burger=StringVar()
Total_bill=StringVar()

#Label
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=12,fg="blue4")
lbl_Idli=Label(f1,font=("aria",20,'bold'),text="Idli",width=12,fg="blue4")
lbl_PavBaji=Label(f1,font=("aria",20,'bold'),text="PavBaji",width=12,fg="blue4")
lbl_Biryani=Label(f1,font=("aria",20,'bold'),text="Biryani",width=12,fg="blue4")
lbl_Mandi=Label(f1,font=("aria",20,'bold'),text="Mandi",width=12,fg="blue4")
lbl_Noodles=Label(f1,font=("aria",20,'bold'),text="Noodles",width=12,fg="blue4")
lbl_Momos=Label(f1,font=("aria",20,'bold'),text="Momos",width=12,fg="blue4")
lbl_Burger=Label(f1,font=("aria",20,'bold'),text="Burger",width=12,fg="blue4")
lbl_dosa.grid(row=1,column=0)
lbl_Idli.grid(row=2,column=0)
lbl_PavBaji.grid(row=3,column=0)
lbl_Biryani.grid(row=4,column=0)
lbl_Mandi.grid(row=5,column=0)
lbl_Noodles.grid(row=6,column=0)
lbl_Momos.grid(row=7,column=0)
lbl_Burger.grid(row=8,column=0)


#entry
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightblue")
entry_Idli=Entry(f1,font=("aria",20,'bold'),textvariable=Idli,bd=6,width=8,bg="lightblue")
entry_PavBaji=Entry(f1,font=("aria",20,'bold'),textvariable=PavBaji,bd=6,width=8,bg="lightblue")
entry_Biryani=Entry(f1,font=("aria",20,'bold'),textvariable=Biryani,bd=6,width=8,bg="lightblue")
entry_Mandi=Entry(f1,font=("aria",20,'bold'),textvariable=Mandi,bd=6,width=8,bg="lightblue")
entry_Noodles=Entry(f1,font=("aria",20,'bold'),textvariable=Noodles,bd=6,width=8,bg="lightblue")
entry_Momos=Entry(f1,font=("aria",20,'bold'),textvariable=Momos,bd=6,width=8,bg="lightblue")
entry_Burger=Entry(f1,font=("aria",20,'bold'),textvariable=Burger,bd=6,width=8,bg="lightblue")
entry_dosa.grid(row=1,column=1)
entry_Idli.grid(row=2,column=1)
entry_PavBaji.grid(row=3,column=1)
entry_Biryani.grid(row=4,column=1)
entry_Mandi.grid(row=5,column=1)
entry_Noodles.grid(row=6,column=1)
entry_Momos.grid(row=7,column=1)
entry_Burger.grid(row=8,column=1)

#button

btn_reset=Button(f1,bd=5,fg="black",bg="lightpink",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="black",bg="lightpink",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)






root.mainloop()

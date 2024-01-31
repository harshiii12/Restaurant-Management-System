import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector
import time
from datetime import datetime
import csv
mydb=mysql.connector.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
mycursor=mydb.cursor()
now=datetime.now()
breakfast=now.replace(hour=12, minute=0, second=0)
evening=now.replace(hour=17, minute=0, second=0)
totalbill=0
bill_id=''
name=''

phone_number=0
def gettable():
    global tableno
    try:
        tableno=int(var3.get())
        if tableno>12:
            raise TypeError
        else:
            opt_table['state']=tk.DISABLED
            opt.configure(state="normal")
            quantitymenu.configure(state="normal")
            
    except:
        from tkinter import messagebox
        messagebox.showerror("Error","Please enter valid table no")
        
def columnskip(row,columno,initial):
    for i in range(columno):
        label=tk.Label(text="\t\t\t\t\t\t",bg='snow').grid(row=row,column=initial+1+columno)
root=tk.Tk()
root.configure(bg='snow')
root.title("Food ordering Desk")
def printorder(foodordered,quantity,cost,row):
    l=foodordered.split('@')
    a=l[0]
    labelitem=tk.Label(text=a,bg='snow').grid(row=row,column=5,sticky='E')
    labelquant=tk.Label(text=quantity,bg='snow').grid(row=row,column=6,sticky='We')
    labelcost=tk.Label(text=u'\u20B9'+str(cost),bg='snow').grid(row=row,column=7,sticky='We')
    
def orderfood():
    global totalbill
    foodordered=variable.get()
    from tkinter import messagebox
    quantity=quantitymenu.get()
    if foodordered=="Select":
        messagebox.showerror("Failed","Please select valid food item")
    elif eval(quantity)==0:
        messagebox.showerror("Failed","Please enter valid quantity")
    else:
        cost=menudict[foodordered]*eval(quantity)
        confirm=messagebox.askquestion("Confirmation","Do you confirm ordering "+str(foodordered)+" quantity "+str(quantity)+" for Rs."+str(cost))
        if confirm=="yes":
            global line
            totalbill+=cost
            printorder(foodordered,quantity,cost,line)
            line+=1
            paybutton=tk.Button(text='Pay Now '+u'\u20B9'+str(totalbill), command=pay).place(x=690,y=560)
            query=('insert into table'+str(tableno)+' values(%s,%s,%s)')
            values=((foodordered.split('@'))[0],quantity,cost)
            mycursor.execute(query,values)
            mydb.commit()
        else:
            return None
def proceed():
    global var1
    global var2
    from tkinter import messagebox
    global bill_id
    global name
    global phone_number
    if var1.get()=='' or type(var1.get())==int or var2.get()=='' or len(var2.get())!=10:
        messagebox.showerror("Failed","Please enter valid information")
    else:
        name=var1.get()
        phone_number=var2.get()
        bill_id=name[0]+'_'+str(tableno) + '_' + time.strftime('%H_%M_%S')+'_'+phone_number[-1]
        root.destroy()
        proceedings=tk.Tk()
        if var.get()==1:
            label=tk.Label(proceedings,text="Thank you for choosing ANR. Pay at the desk")
            label1=tk.Label(proceedings,text="Your bill ID is " + bill_id).pack()
            label.pack()
            query1=("Select * from table"+str(tableno))
            mycursor.execute(query1)
            result=mycursor.fetchall()

            c=csv.writer(open(bill_id +'.csv','w'))
            for x in result:
                c.writerow(x)
            
            query=("delete from table"+str(tableno))
            mycursor.execute(query)
            mydb.commit()

        else:
            label_1=tk.Label(proceedings,text="Enter Card holder Name").pack()
            entry_1=tk.Entry(proceedings).pack() 
            
            label_2=tk.Label(proceedings,text="Enter Card number").pack()
            entry_2=tk.Entry(proceedings).pack()
            
            button=tk.Button(proceedings,text="Pay",command=end).pack()
            
        
        proceedings.mainloop()


def end():
    global bill_id
    global name
    global phone_number
    bill_id=name[0]+'_'+str(tableno) + '_' + time.strftime('%H_%M_%S')+'_'+phone_number[-1]+'_' +"%"
    thank=tk.Tk()
    label=tk.Label(thank,text="Thanks for choosing ANR Take your bill from counter!").pack()
    label2=tk.Label(thank,text="Your bill ID is " + bill_id ).pack()
    query1=("Select * from table"+str(tableno))
    mycursor.execute(query1)
    result=mycursor.fetchall()

    c=csv.writer(open(bill_id +'.csv','w'))
    for x in result:
        c.writerow(x)
    query=("delete from table"+str(tableno))
    mycursor.execute(query)
    mydb.commit()
def pay():
    global var
    global var1
    global var2
    
    paywindow=tk.Toplevel(root)
    var=tk.IntVar(paywindow)
    var1=tk.StringVar(paywindow)
    var2=tk.StringVar(paywindow)
    label=tk.Label(paywindow,text="Choose the method to pay").pack()
    label_1=tk.Label(paywindow,text="Enter Your name").pack()
    entry_5=tk.Entry(paywindow,textvariable=var1).pack()
    label_2=tk.Label(paywindow,text="Enter your phone number").pack()
    entry_6=tk.Entry(paywindow,textvariable=var2).pack()
    
    radio1=tk.Radiobutton(paywindow,text="Pay at desk",variable=var,value=1).pack(anchor='w')
    radio2=tk.Radiobutton(paywindow,text="Debit Card",variable=var,value=2).pack(anchor='w')
    button=tk.Button(paywindow,text="Proceed",command=proceed).pack()
    paywindow.mainloop()

root.geometry('800x600')

image1=Image.open("image.jpeg")
image1 = image1.resize((300,300), Image.ANTIALIAS)
image2=ImageTk.PhotoImage(image1)
background_label = tk.Label(root, image=image2,height=300,width=300,bg='snow',relief='flat')
background_label.place(x=0,y=110)
time1 = ''
clock = tk.Label(root, font=('times', 20, 'bold'), bg='snow')
clock.place(x=690,y=0)
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
tick()
tables=[1,2,3,4,5,6,7,8,9,10,11,12]
var3=tk.StringVar(root)
var3.set("Select table number here")
label_1=tk.Label(text="Choose table number", font='20',bg='snow')
label_1.grid(row=0,column=0)
opt_table=tk.OptionMenu(root,var3,*tables)
opt_table.grid(row=1,column=0)
button_1=tk.Button(text='-->',fg='white',bg='black',command=gettable)
button_1.grid(row=1,column=1,sticky='W')
if now<=breakfast:
    query1=("Select item,cost from menu where time='Breakfast' or time='Extras'")
    mycursor.execute(query1)
    options=["Select"]
    for item,cost in mycursor:
        options.append(item + '@'+ u'\u20B9' + str(cost))
        menudict={"Select":0}
    query2=("Select cost from menu where time='Breakfast' or time='Extras'")
    mycursor.execute(query2)
elif now>breakfast and now<=evening:
    query1=("Select item,cost from menu where time='Lunch' or time='Extras'")
    mycursor.execute(query1)
    options=["Select"]
    for item,cost in mycursor:
        options.append(item + '@'+ u'\u20B9' + str(cost))
        menudict={"Select":0}
    query2=("Select cost from menu where time='Lunch' or time='Extras'")
    mycursor.execute(query2)
elif now>evening:
    query1=("Select item,cost from menu where time='Dinner' or time='Extras'")
    mycursor.execute(query1)
    options=["Select"]
    for item,cost in mycursor:
        options.append(item + '@'+ u'\u20B9' + str(cost))
        menudict={"Select":0}
    query2=("Select cost from menu where time='Dinner' or time='Extras'")
    mycursor.execute(query2)
count=1
for cost in mycursor:
    menudict[options[count]]=cost[0]
    count+=1
variable = tk.StringVar(root)
variable.set(options[0])
opt = tk.OptionMenu(root, variable, *options)
opt.configure(state="disabled")
opt.grid(row=3,column=0,sticky='EW')
quantityopt=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
quantitymenu=ttk.Combobox(root,  value=quantityopt)
quantitymenu.configure(state="disabled")
quantitymenu.current(0)
quantitymenu.grid(row=3,column=1,sticky='EW')
label_3=tk.Label(text="ITEM",font='Helvetica 12 bold',bg='snow')
label_3.grid(row=2,column=0,sticky='EW')
label_4=tk.Label(text="Quantity",font='Helvetica 12 bold',bg='snow')
label_4.grid(row=2,column=1,sticky='EW')
columnskip(3,3,1)
line=5
label_5=tk.Label(text="Food Ordered",font='Helvetica 14 bold',bg='snow')
label_5.grid(row=3,column=5,sticky='E')
label_6=tk.Label(text="    Quantity",font='Helvetica 14 bold',bg='snow')
label_6.grid(row=3,column=6,sticky='W')
label_7=tk.Label(text="    Cost",font='Helvetica 14 bold',bg='snow')
label_7.grid(row=3,column=7,sticky='W')
label_8=tk.Label(text="Current Time:",bg='snow',font='Times 14 bold')
label_8.place(x=565,y=5)
button_2=tk.Button(text="order",command=orderfood)
button_2.grid(row=4,column=0,sticky='W')
label_9=tk.Label(text="*Breakfast is available only till 12 PM",bg='snow',font='Times 14 bold').place(x=0,y=420)
label_10=tk.Label(text="**Lunch is available only till 5 PM",bg='snow',font='Times 14 bold').place(x=0,y=440)

root.mainloop()

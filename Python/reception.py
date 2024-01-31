from tkinter import *
import mysql.connector as sqltor
from PIL import ImageTk,Image
# Creating Window To Work
root=Tk()
root.title("ANR Restaurant")
root.iconbitmap("anr 2.ico")
root.resizable(height= False, width= False)

# Importing Necessary Photo files
photo=PhotoImage(file=r"table.png")
photoimage=photo.subsample(4,4)
photo1=PhotoImage(file=r"ANR11.png")
photoimage1=photo1.subsample(22,30)

# Connecting wth MYSQL database
mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
crsr=mycon.cursor()

# Defining Function to Show The order of Table_1
def TABLE1():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table1 ")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table1")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE1()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)
    

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)

# Defining Function to Show The order of Table_2
def TABLE2():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table2")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table2")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE2()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)






# Defining Function to Show The order of Table_3
def TABLE3():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table3")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table3")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE3()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)





# Defining Function to Show The order of Table_4
def TABLE4():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table4")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="kartik123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table4")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE4()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)





# Defining Function to Show The order of Table_5
def TABLE5():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table5")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)


    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table5")
        mycon.commit()
    def refresh():
        Top.destroy()
        TABLE5()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)






# Defining Function to Show The order of Table_6
def TABLE6():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table6")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="kartik123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table6")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE6()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)
    






# Defining Function to Show The order of Table_7
def TABLE7():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table7")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table7")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE7()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)



# Defining Function to Show The order of Table_8
def TABLE8():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table8")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="kartik123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table8")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE8()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)


# Defining Function to Show The order of Table_9
def TABLE9():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table9")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table9")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE9()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)



# Defining Function to Show The order of Table_10
def TABLE10():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table10")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table10")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE10()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)



# Defining Function to Show The order of Table_11
def TABLE11():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table11")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table11")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE11()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)



# Defining Function to Show The order of Table_12
def TABLE12():
    Top=Toplevel()
    Top.configure(bg="wheat")
    mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
    crsr=mycon.cursor()
    crsr.execute( "select * from table12")
    records=crsr.fetchall()
    item_record=""
    money_record=""
    pay_money=0

    for record in records:
        item_record+=str(record[0]) +" \n"
    for record in records:
        money_record+=str(record[2]) +" \n"
    for record in records:
        pay_money+=record[2]

    label_item1=Label(Top,text="Items  Ordered",bg="wheat",borderwidth=4).grid(row=0,column=0)
    label_money1=Label(Top,text="Price (in Rs.)",bg="wheat",borderwidth=4).grid(row=0,column=1)
  
    label_item=Label(Top,text=item_record,bg="wheat",compound=LEFT).grid(row=1,column=0)
    label_money=Label(Top,text=money_record,bg="wheat",compound=LEFT).grid(row=1,column=1)

    def pay():
        mycon=sqltor.connect(host="localhost",user="root",passwd="abc123",database="restaurant")
        crsr=mycon.cursor()
        crsr.execute("DELETE FROM table12")
        mycon.commit()

    def refresh():
        Top.destroy()
        TABLE12()

    refresh_button=Button(Top,text="REFRESH",bg="blue",fg="white",font=" Helvetica 9 bold",command=refresh).grid(row=3,column=0)
    text1=str(pay_money)
    label_pay=Label(Top,text=("your total bill is: "+ u'\u20B9'+ text1),bg="wheat").grid(row=2,column=1)
    pay_button=Button(Top,text=("PAY:  " + u'\u20B9'+ text1),bg="blue",fg="white",font=" Helvetica 9 bold",command=pay).grid(row=3,column=1,ipadx=30)

    label_thanks=Label(Top,text=" Thank You! "+"\n"+"Visit us Again.",fg="red", font="Boulder 10 bold",bg="wheat").grid(row=4,column=0,columnspan=2)

# Creating buttons for each Table to show the food orddered
Table_1=Button(root, text="Table 1",font=' Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE1)
Table_2=Button(root, text="Table 2",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE2)
Table_3=Button(root, text="Table 3",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE3)
Table_4=Button(root, text="Table 4",font='Calluna 25' ,image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE4)
Table_5=Button(root, text="Table 5",font='Calluna 25' ,image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE5)
Table_6=Button(root, text="Table 6",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE6)
Table_7=Button(root, text="Table 7",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE7)
Table_8=Button(root, text="Table 8",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE8)
Table_9=Button(root, text="Table 9",font='Calluna 25 ',image=photoimage,compound=LEFT,padx=30 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE9)
Table_10=Button(root, text="Table 10",font='Calluna 25' ,image=photoimage,compound=LEFT,padx=24 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE10)
Table_11=Button(root, text="Table 11",font='Calluna 25' ,image=photoimage,compound=LEFT,padx=24 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE11)
Table_12=Button(root, text="Table 12",font='Calluna 25' ,image=photoimage,compound=LEFT,padx=24 ,pady=20,bg='lightcoral' ,fg='black', borderwidth=7, command=TABLE12)
label_1=Label(root,text="Please select the TABLE NO.",image=photoimage1,compound=LEFT, bg="black", fg="white", font='Helevetica 16 bold',padx=231.9 ,pady=-10,borderwidth=3)

Table_1.grid(row=1,column=0)
Table_2.grid(row=1,column=1)
Table_3.grid(row=1,column=2)
Table_4.grid(row=2,column=0)
Table_5.grid(row=2,column=1)
Table_6.grid(row=2,column=2)
Table_7.grid(row=3,column=0)
Table_8.grid(row=3,column=1)
Table_9.grid(row=3,column=2)
Table_10.grid(row=4,column=0)
Table_11.grid(row=4,column=1)
Table_12.grid(row=4,column=2)
label_1.grid(row=0,column=0,columnspan=10)


root.mainloop()

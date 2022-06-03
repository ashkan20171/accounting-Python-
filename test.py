import tkinter
import arabic_reshaper
from bidi.algorithm import get_display
import sqlite3
from tkinter import messagebox
def fa(x):
    return get_display(arabic_reshaper.reshape(x))

try:
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    query = "select name from person"
    data = cur.execute(query)
    my_data =[r for r , in data]
    my_list = list(map(fa,my_data))
except sqlite3.Error as error:
    print("error new costomer didn't insert",error)

finally:
    con.close()


def new_co() :
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        p = new_co_input.get()
        print (p)
        query = "insert into person(name) values(?)"
        cur.execute(query,(p,))
        con.commit()
    except sqlite3.Error as error:
        print("error new costomer didn't insert",error)

    finally:
        con.close()


def insert():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        my_data = [fa(i1.get()),i2.get(),i3.get()]
        query = "insert into orders (person_id,order_detail,order_price) values (?,?,?)"
        cur.execute(query,my_data)
        con.commit()
        print('سفارش ثبت شد ')
    except sqlite3.Error as error:
        print("error new costomer didn't insert",error)
    finally:
        con.close()
def select():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        query = 'select * from orders where person_id = ?'
        person = fa(i1.get())
        cur.execute(query,(person,))
        result = cur.fetchall()
        all_money =0
        for r in result:
            print(r)
            all_money+=int(r[2])
    except sqlite3.Error as error:
        print("error new costomer didn't insert",error)
    finally:
        print('کل بدهی',all_money)
        return all_money,person
        con.close()

def delete():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        person = fa(i1.get())
        qurey = "delete from orders where person_id=?"
        cur.execute(qurey,(person,))
        con.commit()
        print('کل بدهی ها پاک شدند')
    except sqlite3.Error as error:
        print("failed to read data from sqlite table",error)
    finally:
        con.close()

def alert():
    m,p = select()
    tkinter.messagebox.showinfo('سلام'+p,fa('میزان بدهی شما')+'\n'+str(m))


w = tkinter.Tk()
w.geometry("500x500")
new_co = tkinter.Button(w,text=fa('مشتری جدید'),command=new_co)
new_co.place(x=350,y=0)

new_co_input = tkinter.Entry(w,width=14)
new_co_input.place(x=350,y=30)


w2 = tkinter.Frame(w,width=100,height=100)
w2.pack()

l1 = tkinter.Label(w2,text=fa('نام مشتری')).pack()
i1 = tkinter.Spinbox(w2,values=my_list,command=select)
i1.pack()

l2 = tkinter.Label(w2,text=fa('جزییات سفارش')).pack()
i2 = tkinter.Entry(w2)
i2.pack()

l3 = tkinter.Label(w2,text=fa('هزینه سفارش')).pack()
i3 = tkinter.Entry(w2)
i3.pack()

b = tkinter.Button(w2,text=fa('ثبت سفارش'),bg='blue',fg='orange',command=insert)
b.pack(anchor=tkinter.CENTER)


d = tkinter.Button(w,text=fa('حذف کل بدهی'),fg='green',bg='red',command=delete)
d.place(x=20,y=200)


a = tkinter.Button(w,text=fa('محاسبه بدهی'),fg='yellow',bg='purple',command=alert)
a.place(x=0,y=0)






w.mainloop()

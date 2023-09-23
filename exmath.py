from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('คิดราคาเนื้อหมู')
GUI.geometry('800x800')


bg = PhotoImage(file='EP5/porkicon.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='ราคาหมูวันนี้ (บาท)',font=(None,20))
L.pack()
v_price = StringVar() #ตัวแปรเก็บข้อตวาม เมื่อพิมพ์เสร็จแล้ว
E2 = ttk.Entry(GUI, textvariable=v_price, font=(None, 20)) #สร้างตัวแปรเก็บไว้ใน E2 แบบ text variacle
E2.pack()#แปะไว้ใน gui


L = Label(GUI,text='จำนวนหมู (กิโลกรัม)',font=(None,20))
L.pack()
v_quantity = StringVar() #ตัวแปรเก็บข้อตวาม เมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 20)) #สร้างตัวแปรเก็บไว้ใน E1 แบบ text variacle
E1.pack() #แปะไว้ใน gui



def cal():
    try:    
        quan = float(v_quantity.get())
        prc = float(v_price.get())
        calc = quan * prc
        messagebox.showinfo('ราคาทั้งหมด', 'ราคาหมูทั้งหมด {}' .format(calc))
        v_quantity.set('')
        v_price.set('')
        E2.focus() 

    except:
        messagebox.showwarning('กรอกผิด', 'กรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('1')
B = ttk.Button(GUI, text='คิดราคา', command=cal)
B.pack(ipadx=30,ipady=20)

GUI.mainloop() #ทำงานตลอดเวลา วนลูป
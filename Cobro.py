import sqlite3
from tkinter import *
from tkinter import messagebox

conexion=sqlite3.connect("ControlClient")
cursor=conexion.cursor()


root=Tk()
root.title('Cobrando')
root.geometry('650x550')
root.config(bg='medium aquamarine')

barra_menu=Menu(root)
root.config(menu=barra_menu,width=200,height=200)

menu_list=Menu(barra_menu,tearoff=0)
menu_list.add_command(label='lista de clientes')

salir=Menu(barra_menu,tearoff=0)
salir.add_command(label='cerrar ventana')

barra_menu.add_cascade(label='lista de clientes',menu=menu_list)
barra_menu.add_cascade(label='Salir', menu=salir)

#---------------------------------------------------------------------------

frame3=Frame(root)
frame3.pack()

cuadro_C=Entry(frame3)
cuadro_C.grid(row=1,column=2,padx=50,pady=20)
cuadro_C.config(fg='green', justify='right')

cuadro_nombre=Entry(frame3)
cuadro_nombre.grid(row=3,column=2,padx=50,pady=20)
cuadro_nombre.config(justify='right')

cuadro_direccion=Entry(frame3)
cuadro_direccion.grid(row=4,column=2,padx=50,pady=20)
cuadro_direccion.config(justify='right')

cuadro_saldo=Entry(frame3)
cuadro_saldo.grid(row=5,column=2,padx=50,pady=20)
cuadro_saldo.config(justify='right')

cuadro_uabono=Entry(frame3)
cuadro_uabono.grid(row=6,column=2,padx=50,pady=20)
cuadro_uabono.config(justify='right')

#----------------------------------------
dato_c='01'
dato_N='michael'
dato_D='Heredia'
dato_s=10000
dato_ub='27/9/2019'


label_c=Label(frame3,text=dato_c)
label_c.grid(row=1,column=1,sticky='e',padx=20,pady=20)

label_n=Label(frame3,text=dato_N)
label_n.grid(row=2,column=1,sticky='e',padx=20,pady=20)

label_d=Label(frame3,text=dato_D)
label_d.grid(row=3,column=1,sticky='e',padx=20,pady=20)

label_s=Label(frame3,text=dato_s)
label_s.grid(row=4,column=1,sticky='e',padx=20,pady=20)

label_ub=Label(frame3,text=dato_ub)
label_ub.grid(row=5,column=1,sticky='e',padx=20,pady=20)

#------------------------------------------------------------------

label_c2=Label(frame3,text='Codigo:')
label_c2.grid(row=1,column=0,sticky='e',padx=20,pady=20)

label_n2=Label(frame3,text='Cliente:')
label_n2.grid(row=2,column=0,sticky='e',padx=20,pady=20)

label_d2=Label(frame3,text='Direccion:')
label_d2.grid(row=3,column=0,sticky='e',padx=20,pady=20)

label_s2=Label(frame3,text='saldo:')
label_s2.grid(row=4,column=0,sticky='e',padx=20,pady=20)

label_ub2=Label(frame3,text='Ult Abono:')
label_ub2.grid(row=5,column=0,sticky='e',padx=20,pady=20)

label_check=Label(frame3,text='Chequeado')
label_check.grid(row=6,column=0,sticky='e',padx=20,pady=20)

















root.mainloop()

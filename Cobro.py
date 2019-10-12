import sqlite3
from tkinter import *
from tkinter import messagebox

conexion=sqlite3.connect("ControlClient")
cursor=conexion.cursor()


root=Tk()
root.title('Cobrando')
root.geometry('350x500')
root.config(bg='Gray')

def abonarc():
	valor=messagebox.askquestion("Confirmar abono","abonar ?")
	if valor=="yes":
		print('vas bien')

barra_menu=Menu(root)
root.config(menu=barra_menu,width=500,height=50)

menu_list=Menu(barra_menu,tearoff=0)
menu_list.add_command(label='lista de clientes')

salir=Menu(barra_menu,tearoff=0)
salir.add_command(label='cerrar ventana')

barra_menu.add_cascade(label='lista de clientes',menu=menu_list)
barra_menu.add_cascade(label='Salir', menu=salir)

#---------------------------------------------------------------------------

frame3=Frame(root)
frame3.pack(ipadx=150,expand=True)


#----------------------------------------
dato_c='01'
dato_N='michael'
dato_D='Heredia'
dato_s=10000
dato_ub='27/9/2019'
dato_factual='11/10/2019'
dato_check='x'


label_c=Label(frame3,text=dato_D)
label_c.grid(row=1,column=1,sticky='e',padx=10,pady=10)

label_n=Label(frame3,text=dato_N)
label_n.grid(row=2,column=1,sticky='e',padx=10,pady=10)

label_d=Label(frame3,text=dato_D)
label_d.grid(row=3,column=1,sticky='e',padx=10,pady=10)

label_s=Label(frame3,text=dato_s)
label_s.grid(row=4,column=1,sticky='e',padx=10,pady=10)

label_ub=Label(frame3,text=dato_ub)
label_ub.grid(row=5,column=1,sticky='e',padx=10,pady=10)

label_check=Label(frame3,text=dato_check)
label_check.grid(row=6,column=1,sticky='e',padx=10,pady=10)

#------------------------------------------------------------------

label_c2=Label(frame3,text='Zona:')
label_c2.grid(row=1,column=0,sticky='e',padx=20,pady=20)
label_c2.config(fg='blue')
label_n2=Label(frame3,text='Cliente:')
label_n2.grid(row=2,column=0,sticky='e',padx=20,pady=20)
label_n2.config(fg='blue')
label_d2=Label(frame3,text='Direccion:')
label_d2.grid(row=3,column=0,sticky='e',padx=20,pady=20)
label_d2.config(fg='blue')
label_s2=Label(frame3,text='saldo:')
label_s2.grid(row=4,column=0,sticky='e',padx=20,pady=20)
label_s2.config(fg='blue')
label_ub2=Label(frame3,text='Ult Abono:')
label_ub2.grid(row=5,column=0,sticky='e',padx=20,pady=20)
label_ub2.config(fg='blue')
label_check2=Label(frame3,text='Chequeado')
label_check2.grid(row=6,column=0,sticky='e',padx=20,pady=20)
label_check2.config(fg='blue')



abono_actual=StringVar()

#label_fecha=Label(frame3,text='Fecha de hoy')
#label_fecha.grid(row=8,column=0,sticky='e',padx=10,pady=10)
label_zona=Label(frame3,text='Codigo:')
label_zona.grid(row=8,column=0,sticky='e',padx=10,pady=10)
#label_f_act=Label(frame3,text=dato_factual)
#label_f_act.grid(row=9,column=0,sticky='e',padx=10,pady=10)
label_ingabono=Label(frame3,text='Ingrese el abono:')
label_ingabono.grid(row=9,column=0,sticky='e',padx=10,pady=10)
cuadro_codg=Entry(frame3, textvariable=dato_c)
cuadro_codg.grid(row=8,column=1,padx=5,pady=5)
cuadro_codg.config(justify='right')
cuadro_abon=Entry(frame3, textvariable=abono_actual)
cuadro_abon.grid(row=9,column=1,padx=5,pady=5)
cuadro_abon.config(justify='right')
boton_abonar=Button(frame3, text='Abonar', command=abonarc)
boton_abonar.grid(row=9,column=2,sticky='e',padx=10,pady=10)
#boton_ok=Button(frame3, text='Ok',) #command=)
#boton_ok.grid(row=8,column=3,sticky='e',padx=10,pady=10)

boton_venta=Button(frame3, text='Venta',) #command=)
boton_venta.grid(row=10,column=0,sticky='e',padx=10,pady=10)
boton_devolucion=Button(frame3, text='Devolucion',) #command=)
boton_devolucion.grid(row=10,column=1,sticky='e',padx=10,pady=10)
boton_Terminar=Button(frame3, text='Terminar',) #command=)
boton_Terminar.grid(row=10,column=2,sticky='e',padx=10,pady=10)















root.mainloop()

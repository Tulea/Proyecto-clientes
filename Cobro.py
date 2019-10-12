import sqlite3
from tkinter import *
from tkinter import messagebox

conexion = sqlite3.connect("Base de Datos")
cursor=conexion.cursor()


def pp():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT * FROM CLIENTES WHERE zona=")
        client2 = cursor.fetchall()
        for i in client2:
            if i == dato_z.get():
                messagebox.showinfo('byTulea', 'Zona correcta')
        root2.destroy()
    except:
        messagebox.showinfo('byTulea', 'la Zona no existe')


root2 = Tk()
root2.title('Cobrando')
root2.geometry('250x150')
dato_z = StringVar()
dato_FH = StringVar()
label_zona2 = Label(root2, text='ingrese zona :')
label_zona2.grid(row=0, column=0, sticky='e', padx=10, pady=10)
label_fechaactu = Label(root2, text='ingrese fecha :')
label_fechaactu.grid(row=1, column=0, sticky='e', padx=10, pady=10)
cuadroZ = Entry(root2, textvariable=dato_z)
cuadroZ.grid(row=0, column=1, padx=10, pady=10)
cuadrofec = Entry(root2, textvariable=dato_FH)
cuadrofec.grid(row=1, column=1, padx=10, pady=10)

boton_ok = Button(root2, text='Ok', command=pp)
boton_ok.grid(row=3, column=1, sticky='w', padx=10, pady=10)

root2.mainloop()

dato_zona = dato_z.get()
fecha_act = dato_FH.get()

conexion = sqlite3.connect('Base de Datos')
cursor = conexion.cursor()




root=Tk()
root.title('Cobrando')
root.geometry('350x500')
root.config(bg='Gray')


def ok():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM CLIENTES WHERE codigo=" + codigo.get())
    client = cursor.fetchall()

    for user in client:
        codigo.set(user[0])
        dato_c.set(user[1])
        dato_s.set(user[2])
        dato_D.set(user[3])
        dato_N.set(user[4])
        dato_v.set(user[5])
        dato_ub.set(user[6])
        observacion.insert(1.0, user[7])

    conexion.commit()





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
dato_c = StringVar()
dato_N = StringVar()
dato_D = StringVar()
dato_ub = StringVar()
dato_check='x'
dato_v = StringVar()

label_c=Label(frame3,text=dato_D)
label_c.grid(row=1,column=1,sticky='e',padx=10,pady=10)

label_n=Label(frame3,text=dato_N)
label_n.grid(row=2,column=1,sticky='e',padx=10,pady=10)

label_d=Label(frame3,text=dato_D)
label_d.grid(row=3,column=1,sticky='e',padx=10,pady=10)

label_s = Label(frame3, text=dato_zona)
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
boton_ok = Button(frame3, text='Ok', )  # command=)
boton_ok.grid(row=8, column=2, sticky='e', padx=10, pady=10)

boton_venta=Button(frame3, text='Venta',) #command=)
boton_venta.grid(row=10,column=0,sticky='e',padx=10,pady=10)
boton_devolucion=Button(frame3, text='Devolucion',) #command=)
boton_devolucion.grid(row=10,column=1,sticky='e',padx=10,pady=10)
boton_Terminar=Button(frame3, text='Terminar',) #command=)
boton_Terminar.grid(row=10,column=2,sticky='e',padx=10,pady=10)















root.mainloop()

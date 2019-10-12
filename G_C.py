import tkinter
from tkinter import messagebox
import sqlite3
#from funciones_ventana import*

root=tkinter.Tk()
root.title('Gestion Clientes')
def conexionbbdd():
	conexion=sqlite3.connect("controlClient_BYTulea")
	cursor=conexion.cursor()

	try:
		cursor.execute('''
			CREATE TABLE DATOSCLIENTES (
			CODIGO INTEGER ,
			CLIENTE VARCHAR(50),
			SALDO INTEGER,
			ZONA VARCHAR (50),
			TELEFONO INTEGER,
			COMPRAS VARCHAR (100000),
			ult_abono VARCHAR (20) PRIMARY KEY,
			DESCRIBCION VARCHAR(100))
			''')
		MESSAGEBOX.SHOWINFO("ByTulea","la base de datos se creo correctamente")
	except:
		messagebox.showwarning("ByTulea","La base de datos ya existe")




def salirapp():
	valor=messagebox.askquestion("salir","desea cerrar")
	if valor=="yes":
		root.destroy()

def limpiarC():
	codigo.set("")
	cliente.set("")
	saldo.set("")
	zona.set("")
	telefono.set("")
	ult_abono.set("")
	observacion.delete(1.0, tkinter.END)

def crear():
	conexion=sqlite3.connect("controlClient_BYTulea")
	cursor=conexion.cursor()

	cursor.execute("INSERT INTO DATOSCLIENTES VALUES('" + codigo.get() +"','" + cliente.get() +
		"','" + saldo.get() +"','" + zona.get() +"','" + telefono.get() +"','" + compras.get() +"','"+ ult_abono.get() +"','" + observacion.get("1.0", tkinter.END) + "')")
		  
	conexion.commit()
	messagebox.showinfo("ByTulea","registro ingresado con exito")

def leer():
	conexion=sqlite3.connect("controlClient_BYTulea")
	cursor=conexion.cursor()

	cursor.execute("SELECT * FROM DATOSCLIENTES WHERE codigo="+codigo.get())
	usuario=cursor.fetchall()
	for i in usuario:
		codigo.set(usuario[0])
		cliente.set(usuario[1])
		saldo.set(usuario[3])
		zona.set(usuario[4])
		telefono.set(usuario[5])
		#ult_a.set(usuario[6])
		ult_abono.set(usuario[7])
		observacion.Insert(1.0, usuario[8])
	conexion.commit()

def actualizar():
	conexion=sqlite3.connect("controlClient_BYTulea")
	cursor=conexion.cursor()

	cursor.execute("""UPDATE DATOSCLIENTES SET cliente='" + cliente.get()+"',
		saldo='" + saldo.get() +"',
		zona='" + zona.get() +"',
		telefono='" + telefono.get() +"',
		compras='" + compras.get()+"',
		ult_abono='" + ult_abono.get() +"',
		observacion='" + observacion.get("1.0",END) +
		"' WHERE CODIGO=""" + codigo.get())
	conexion.commit()
	messagebox.showinfo("ByTulea","registro a sido actualizado")

def borrar():
	conexion=sqlite3.connect("controlClient_BYTulea")
	cursor=conexion.cursor()

	cursor.execute("DELETE FROM DATOSCLIENTES WHERE CODIGO ="+ codigo.get())

	conexion.commit()
	messagebox.showinfo("bytulea","el cliente a sido eliminado")



barraMenu=tkinter.Menu(root)
root.config(menu=barraMenu, width=300,height=300)

bbddMenu=tkinter.Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='conectar', command=conexionbbdd)
bbddMenu.add_command(label='salir',command=salirapp)

limpiar=tkinter.Menu(barraMenu, tearoff=0)
limpiar.add_command(label='limpiar campos', command=limpiarC)

opciones=tkinter.Menu(barraMenu, tearoff=0)
opciones.add_command(label='crear', command=crear)
opciones.add_command(label='leer', command=leer)
opciones.add_command(label='modificar',command=actualizar)
opciones.add_command(label='borrar', command=borrar)

ayuda=tkinter.Menu(barraMenu, tearoff=0)
ayuda.add_command(label='licencia')
ayuda.add_command(label='acerca de:')

barraMenu.add_cascade(label="bbdd",menu=bbddMenu)
barraMenu.add_cascade(label="limpiar",menu=limpiar)
barraMenu.add_cascade(label="opciones",menu=opciones)
barraMenu.add_cascade(label="ayuda",menu=ayuda)

#comiendo de campor

frame=tkinter.Frame(root)
frame.pack()
 
codigo=tkinter.StringVar()
cliente=tkinter.StringVar()
saldo=tkinter.StringVar()
zona=tkinter.StringVar()
telefono=tkinter.StringVar()
compras=tkinter.StringVar()
ult_abono=tkinter.StringVar()


cuadrocodigo=tkinter.Entry(frame, textvariable=codigo)
cuadrocodigo.grid(row=0,column=1,padx=10,pady=10)

cuadrocliente=tkinter.Entry(frame, textvariable=cliente)
cuadrocliente.grid(row=1,column=1,padx=10,pady=10)
cuadrocliente.config(fg='blue')

cuadrosaldo=tkinter.Entry(frame, textvariable=saldo)
cuadrosaldo.grid(row=2,column=1,padx=10,pady=10)

cuadrozona=tkinter.Entry(frame, textvariable=zona)
cuadrozona.grid(row=3,column=1,padx=10,pady=10)

cuadrotelefono=tkinter.Entry(frame, textvariable=telefono)
cuadrotelefono.grid(row=4,column=1,padx=10,pady=10)

cuadrocompras=tkinter.Entry(frame, textvariable=ult_abono)
cuadrocompras.grid(row=5,column=1,padx=15,pady=15)

observacion=tkinter.Text(frame, width=16, height=5)
observacion.grid(row=6,column=1,padx=10,pady=10)
scrollvert=tkinter.Scrollbar(frame, command=observacion.yview)
scrollvert.grid(row=6,column=2,sticky='nsew')
observacion.config(yscrollcommand=scrollvert)


# empezamos con etiquetas

codigolabel=tkinter.Label(frame, text='Codigo:')
codigolabel.grid(row=0,column=0,sticky='e',padx=10,pady=10)

clientelabel=tkinter.Label(frame, text='Cliente:')
clientelabel.grid(row=1,column=0,sticky='e',padx=10,pady=10)

saldolabel=tkinter.Label(frame, text='Saldo:')
saldolabel.grid(row=2,column=0,sticky='e',padx=10,pady=10)

zonalabel=tkinter.Label(frame, text='Zona:')
zonalabel.grid(row=3,column=0,sticky='e',padx=10,pady=10)

telefonolabel=tkinter.Label(frame, text='Telefono:')
telefonolabel.grid(row=4,column=0,sticky='e',padx=10,pady=10)

compraslabel=tkinter.Label(frame, text='ult_abono:')
compraslabel.grid(row=5,column=0,sticky='e',padx=10,pady=10)

textolabel=tkinter.Label(frame, text='Descripcion:')
textolabel.grid(row=6,column=0,sticky='e',padx=10,pady=10)

# ingresamos botones

frame2=tkinter.Frame(root)
frame2.pack()

botoncrear=tkinter.Button(frame2, text='Crear', command=crear)
botoncrear.grid(row=1,column=0,sticky='e',padx=10,pady=10)

botonbuscar=tkinter.Button(frame2, text='Buscar', command=leer)
botonbuscar.grid(row=1,column=1,sticky='e',padx=10,pady=10)

botonmodificar=tkinter.Button(frame2, text='Modificar', command=actualizar)
botonmodificar.grid(row=1,column=2,sticky='e',padx=10,pady=10)

root.mainloop()
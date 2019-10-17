from tkinter import *
from tkinter import messagebox
import sqlite3

paladin = Tk()
paladin.title('By_Tulea')
paladin.geometry('1000x500')
paladin.config(bg='black')


def base_datos():
    conexion = sqlite3.connect("Base de Datos")
    cursor = conexion.cursor()

    try:
        cursor.execute(''' CREATE TABLE CLIENTES (
			CODIGO INTEGER PRIMARY KEY,
			CLIENTE VARCHAR (50),
			SALDO INTEGER ,
			ZONA VARCHAR (50),
			TELEFONO INTERGER ,
			VENTAS VARCHAR (100),
			ULT_ABONO VARCHAR (50),
			OBSERVACION VARCHAR (100))
			''')
        cursor.execute('''CREATE TABLE ZONAS (
			ZONA VARCHAR (50) PRIMARY KEY,
			DESCRIPCION VARCHAR (50))''')

        cursor.execute('''CREATE TABLE VENTAS (
			NUMERO INTEGER PRIMARY KEY AUTOINCREMENT,
			CODIGO INTEGER, ARTICULO VARCHAR (50), PRECIO INTEGER, CLIENTE VARCHAR (50), FECHA VARCHAR (50))''')
        cursor.execute('''CREATE TABLE COBROS (
        			FECHA VARCHAR (50),
        			SIABONADOS VARCHAR (50), NOABONADOS VARCHAR (50), TOTALCLIENTES VARCHAR (50), COBRO VARCHAR (50), 
        			VENTAS VARCHAR (50), DEVOLUCIONES VARCHAR (50), SALDOZONA VARCHAR (50) )''')

        messagebox.showinfo('base de datos', 'la base de datos a sido creada')
    except:
        messagebox.showwarning('¡ATENCION!', "La base de datos ya existe")
    conexion.commit()


def salirapp():
    vaor = messagebox.askquestion('Salir', 'Cerrar Programa ? ')
    if vaor == 'yes':
        root.destroy()


def limpiarC():
    codigo.set('')
    cliente.set('')
    saldo.set('')
    zona.set('')
    telefono.set('')
    compras.set('')
    ult_abono.set('')
    observacion.delete(1.0, END)


def crear():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute(" INSERT INTO CLIENTES VALUES('" + codigo.get() +
                   "','" + cliente.get() +
                   "','" + saldo.get() +
                   "','" + zona.get() +
                   "','" + telefono.get() +
                   "','" + compras.get() +
                   "','" + ult_abono.get() +
                   "','" + observacion.get("1.0", END) + "')")

    messagebox.showinfo('base de datos', 'Se a Creado con exito')
    conexion.commit()


def leer():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM CLIENTES WHERE codigo=" + codigo.get())
    client = cursor.fetchall()

    for user in client:
        codigo.set(user[0])
        cliente.set(user[1])
        saldo.set(user[2])
        zona.set(user[3])
        telefono.set(user[4])
        compras.set(user[5])
        ult_abono.set(user[6])
        observacion.insert(1.0, user[7])

    conexion.commit()


def actualizar():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()
    cursor.execute("UPDATE CLIENTES SET CLIENTE='" + cliente.get() +
                   "', saldo='" + saldo.get() +
                   "', zona='" + zona.get() +
                   "', telefono='" + telefono.get() +
                   "', ventas='" + compras.get() +
                   "', ult_abono='" + ult_abono.get() +
                   "', observacion='" + observacion.get("1.0", END) +
                   "' WHERE codigo=" + codigo.get())
    conexion.commit()
    messagebox.showinfo('base de datos', 'Cliente actuaizado')


def borrar():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM CLIENTES WHERE codigo=" + codigo.get())
    conexion.commit()
    messagebox.showinfo('base da datos', 'cliente borrado')


def consultar():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM CLIENTES WHERE codigo=" + codigoventana.get())
    client = cursor.fetchall()
    for i in client:
        zonaventana.set(i[3])
    conexion.commit()

    if zonaventana.get()==zonavtv.get():

        conexion = sqlite3.connect('Base de Datos')
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CLIENTES WHERE codigo=" + codigoventana.get())
        client = cursor.fetchall()
        ventana_texto.delete(0,END)

        for user in client:
            ventana_texto.insert(END,user[0],'')
            codigoventana.set(user[0])
            ventana_texto.insert(END, user[1],'')
            clienteventana.set(user[1])
            ventana_texto.insert(END,user[2],'')
            saldoventana.set(user[2])
            ventana_texto.insert(END, user[3],'')
            zonaventana.set(user[3])
            ventana_texto.insert(END, user[4],'')
            telefonoventana.set(user[4])
            ventana_texto.insert(END, 'Usuario-Si','')
            comprasventana.set(user[5])
            ventana_texto.insert(END, user[6],'')
            ult_abonoventana.set(user[6])
            ventana_texto.insert(END, user[7],'')
            observacionventana.set(user[7])


        conexion.commit()
    else:
        messagebox.showinfo('','CLIENTE NO PERTENECE A ZONA')


def restar(aboo):
    a = int(saldoventana.get())
    b = aboo
    c = int(a - b)

    vaor = messagebox.askquestion('Salir', 'abonar ')
    if vaor == 'yes':
        saldoventana.set(c)

        if aboo > 1:
            totalcobro.set(int(totalcobro.get()) + aboo)
            conexion = sqlite3.connect('Base de Datos')
            cursor = conexion.cursor()
            cursor.execute("UPDATE CLIENTES SET CLIENTE='" + clienteventana.get() +
                           "', saldo='" + saldoventana.get() +
                           "', zona='" + zonaventana.get() +
                           "', telefono='" + telefonoventana.get() +
                           "', ventas='" + comprasventana.get() +
                           "', ult_abono='" + fechaactual.get() +
                           "', observacion='" + observacionventana.get() +
                           "' WHERE codigo=" + codigoventana.get())
            siabonados.set((int(siabonados.get())) + 1)
            print(siabonados.get())
            conexion.commit()
        else:
            conexion = sqlite3.connect('Base de Datos')
            cursor = conexion.cursor()
            cursor.execute("UPDATE CLIENTES SET CLIENTE='" + clienteventana.get() +
                           "', saldo='" + saldoventana.get() +
                           "', zona='" + zonaventana.get() +
                           "', telefono='" + telefonoventana.get() +
                           "', ventas='" + comprasventana.get() +
                           "', ult_abono='" + ult_abonoventana.get() +
                           "', observacion='" + observacionventana.get() +
                           "' WHERE codigo=" + codigoventana.get())
            noabonados.set((int(noabonados.get()))+1)
            conexion.commit()




        messagebox.showinfo('base de datos', 'Cliente abonado')
        consultar()
        resul()






    # minicuadro.mainloop()
def vender(vt):

    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute(" INSERT INTO VENTAS VALUES(NULL, '" + codigoventana.get() +
                   "','" + descripcionventa.get() +
                   "','" + precioventas.get() +
                   "','" + clienteventana.get() +
                   "','" + fechaactual.get() + "')")
    conexion.commit()

    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    a = int(saldoventana.get())
    b = vt
    c = int(a + b)
    saldoventana.set(c)
    cursor.execute("UPDATE CLIENTES SET CLIENTE='" + clienteventana.get() +
                   "', saldo='" + saldoventana.get() +
                   "', zona='" + zonaventana.get() +
                   "', telefono='" + telefonoventana.get() +
                   "', ventas='" + comprasventana.get() +
                   "', ult_abono='" + ult_abonoventana.get() +
                   "', observacion='" + observacionventana.get() +
                   "' WHERE codigo=" + codigoventana.get())

    messagebox.showinfo('base de datos', 'Genial !')
    descripcionventa.set('')
    precioventas.set('')
    ventass.set(int(ventass.get())+vt)
    conexion.commit()
    consultar()
    resul()

def zonaconsulta():
    ZONA = Tk()

    ZONA.title('Zonas')
    ZONA.geometry('350x150')
    #zona4 = StringVar()
    #DESCRIPCION4 = StringVar()

    def enviar():
        conexion = sqlite3.connect('Base de Datos')
        cursor = conexion.cursor()

        cursor.execute(" INSERT INTO ZONAS VALUES('" + zona4.get() +
                       "','" + DESCRIPCION4.get() + "')")

        messagebox.showinfo('base de datos', 'Se a Creado la zona')
        conexion.commit()

    def buscar():
        conexion = sqlite3.connect('Base de Datos')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM ZONAS WHERE ZONA=" + zona4.get())
        client = cursor.fetchall()

        for user in client:
            zona4.set(user[0])
            DESCRIPCION4.set(user[1])

        conexion.commit()

    def BORRAR():
        conexion = sqlite3.connect('Base de Datos')
        cursor = conexion.cursor()
        vaor = messagebox.askquestion('Salir', 'Borrar Zona ? ')
        if vaor == 'yes':
            cursor.execute("DELETE FROM ZONAS WHERE ZONA=" + zona4.get())
            conexion.commit()
            messagebox.showinfo('base da datos', 'Se a Borrado')

    label_zona2 = Label(ZONA, text='ingrese zona :')
    label_zona2.grid(row=0, column=0, sticky='e', padx=10, pady=10)
    label_fechaactu = Label(ZONA, text='ingrese describcion :')
    label_fechaactu.grid(row=1, column=0, sticky='e', padx=10, pady=10)
    cuadroZona = Entry(ZONA, textvariable=zona4)
    cuadroZona.grid(row=0, column=1, padx=10, pady=10)
    cuadrodescribcion = Entry(ZONA, textvariable=DESCRIPCION4)
    cuadrodescribcion.grid(row=1, column=1, padx=10, pady=10)

    boton_crear = Button(ZONA, text='Crear', command=enviar)
    boton_crear.grid(row=0, column=4, sticky='e', padx=5, pady=5)

    boton_buscar = Button(ZONA, text='Buscar', command=buscar)
    boton_buscar.grid(row=1, column=4, sticky='e', padx=5, pady=5)

    boton_modificar = Button(ZONA, text='borrar', command=BORRAR)
    boton_modificar.grid(row=2, column=4, sticky='e', padx=5, pady=5)

    ZONA.mainloop()

def consultarventas():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM VENTAS WHERE codigo=" + codigoventana.get())
    client = cursor.fetchall()
    ventana_texto.delete(0, END)

    for user in client:
        ventana_texto.insert(0,('VENTA:',user[0],'CODIGO:',user[1]),'ARTICULO:',user[2],'PRECIO:',user[3],'CLIENTE:',user[4],'FechaVENTA:',user[5])
        #ventana_texto.insert(0,*user)
        ventana_texto.insert(0,'*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        conexion.commit()

def iniciar():
    vaor5 = messagebox.askquestion('Salir', 'Iniciar? ')
    if vaor5 == 'yes':
        clientescheck.set(0)
        siabonados.set(0)
        noabonados.set(0)
        totalcobro.set(0)
        ventass.set(0)
        clientesenzona.set(0)
        devoluciones.set(0)
        saldozonatotal.set(0)
        conexion = sqlite3.connect('Base de Datos')
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CLIENTES WHERE ZONA=" +zonavtv.get())
        client = cursor.fetchall()
        print(client)
        for i in client:
            clientesenzona.set((int(clientesenzona.get())+1))







        conexion.commit()
        resul()

def devolucion():
    vaor = messagebox.askquestion('Salir', 'abonar ')
    if vaor == 'yes':
        devol()


def devol():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM VENTAS WHERE NUMERO=" + numerodevolucion.get())
    client = cursor.fetchall()
    for a in client:
        preciodevolucion.set(a[3])

    a = int(saldoventana.get())
    b = int(preciodevolucion.get())
    c = int(a - b)
    saldoventana.set(c)
    cursor.execute("UPDATE CLIENTES SET CLIENTE='" + clienteventana.get() +
                   "', saldo='" + saldoventana.get() +
                   "', zona='" + zonaventana.get() +
                   "', telefono='" + telefonoventana.get() +
                   "', ventas='" + comprasventana.get() +
                   "', ult_abono='" + ult_abonoventana.get() +
                   "', observacion='" + observacionventana.get() +
                   "' WHERE codigo=" + codigoventana.get())
    conexion.commit()
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM VENTAS  WHERE NUMERO=" + numerodevolucion.get())
    conexion.commit()

    messagebox.showinfo('base de datos', 'Devuelto!')
    devoluciones.set(int(devoluciones.get())+b)
    consultar()

def fin():
    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM CLIENTES WHERE ZONA=" + zonavtv.get())
    client = cursor.fetchall()
    for i in client:
        t = i[2]
        saldozonatotal.set(int(saldozonatotal.get()) + t)
    conexion.commit()

    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()

    cursor.execute(" INSERT INTO COBROS VALUES('" + fechaactual.get() +
                   "','" + siabonados.get() +
                   "','" + noabonados.get() +
                   "','" + clientesenzona.get() +
                   "','" + totalcobro.get() +
                   "','" + ventass.get() +
                   "','" + devoluciones.get() +
                   "','" + saldozonatotal.get() + "')")
    conexion.commit()
    MINI= Tk()
    finlabel = Label(MINI, text='FECHA:')
    finlabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)
    finlabel1 = Label(MINI, text='ABONADOS:')
    finlabel1.grid(row=1, column=0, sticky='e', padx=10, pady=10)
    finlabel2 = Label(MINI, text='NO ABONADOS:')
    finlabel2.grid(row=2, column=0, sticky='e', padx=10, pady=10)
    finlabel3 = Label(MINI, text='TOTAL CLIENTS:')
    finlabel3.grid(row=3, column=0, sticky='e', padx=10, pady=10)
    finlabel4 = Label(MINI, text='MONTO COBRO:')
    finlabel4.grid(row=4, column=0, sticky='e', padx=10, pady=10)
    finlabel5 = Label(MINI, text='VENTAS:')
    finlabel5.grid(row=5, column=0, sticky='e', padx=10, pady=10)
    finlabel6 = Label(MINI, text='DEVOLUCIONES:')
    finlabel6.grid(row=6, column=0, sticky='e', padx=10, pady=10)
    finlabel7 = Label(MINI, text='SALDO ZONA:')
    finlabel7.grid(row=7, column=0, sticky='e', padx=10, pady=10)
    finlabel8 = Label(MINI, text=fechaactual.get())
    finlabel8.grid(row=0, column=1, sticky='e', padx=10, pady=10)
    finlabel9 = Label(MINI, text=siabonados.get())
    finlabel9.grid(row=1, column=1, sticky='e', padx=10, pady=10)
    finlabel10 = Label(MINI, text=noabonados.get())
    finlabel10.grid(row=2, column=1, sticky='e', padx=10, pady=10)
    finlabel11 = Label(MINI, text=clientesenzona.get())
    finlabel11.grid(row=3, column=1, sticky='e', padx=10, pady=10)
    finlabel12 = Label(MINI, text=totalcobro.get())
    finlabel12.grid(row=4, column=1, sticky='e', padx=10, pady=10)
    finlabel13 = Label(MINI, text=ventass.get())
    finlabel13.grid(row=5, column=1, sticky='e', padx=10, pady=10)
    finlabel14 = Label(MINI, text=devoluciones.get())
    finlabel14.grid(row=6, column=1, sticky='e', padx=10, pady=10)
    finlabel15 = Label(MINI, text=saldozonatotal.get())
    finlabel15.grid(row=7, column=1, sticky='e', padx=10, pady=10)
    MINI.mainloop()

def faltantes():

    conexion = sqlite3.connect('Base de Datos')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM CLIENTES WHERE ZONA=" + zonavtv.get())
    client = cursor.fetchall()
    for i in client:
        if i[6]!=fechaactual.get():
            ventana_texto.insert(END,'CODIGO:',i[0])
            ventana_texto.insert(END,'CLIENTE:', i[1])
            ventana_texto.insert(END,'INF:', i[6])
            ventana_texto.insert(END,'-------------------------------')






DESCRIPCION4=StringVar()
zona4=StringVar()
faltanteszona=StringVar()
montodevolucion=StringVar()
saldozonatotal=StringVar()
devoluciones=StringVar()
clientesenzona=StringVar()
preciodevolucion=StringVar()
numerodevolucion=StringVar()
codigo = StringVar()
cliente = StringVar()
saldo = StringVar()
zona = StringVar()
zona1 = StringVar()
telefono = StringVar()
compras = StringVar()
ult_abono = StringVar()
fechaactual = StringVar()
abono = StringVar()
totalclient = StringVar()
siabonados = StringVar()
noabonados = StringVar()
totalcobro = StringVar()
clientescheck = StringVar()
precioventas = StringVar()
codigoventana = StringVar()
clienteventana = StringVar()
saldoventana = StringVar()
zonaventana = StringVar()
telefonoventana = StringVar()
comprasventana = StringVar()
ult_abonoventana = StringVar()
observacionventana = StringVar()
codigoventa = StringVar()
clienteventa = StringVar()
saldoventa = StringVar()
zonavtv = StringVar()
telefonoventa = StringVar()
comprasventa = StringVar()
ult_abonoventa = StringVar()
observacionventa = StringVar()
descripcionventa=StringVar()
ventass= StringVar()
totalabonados=StringVar()

barraMenu = Menu(paladin)
paladin.config(menu=barraMenu, width=300, height=300)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label='conectar', command=base_datos)
bbddMenu.add_command(label='salir', command=salirapp)

limpiar = Menu(barraMenu, tearoff=0)
limpiar.add_command(label='limpiar campos', command=limpiarC)

opciones = Menu(barraMenu, tearoff=0)
opciones.add_command(label='crear', command=crear)
opciones.add_command(label='leer', command=leer)
opciones.add_command(label='modificar', command=actualizar)
opciones.add_command(label='borrar', command=borrar)

Zonas = Menu(barraMenu, tearoff=0)
Zonas.add_command(label='Faltantes', command=faltantes)
Zonas.add_command(label='Consultar Zona', command=leer)
Zonas.add_command(label='Gestionar Zona', command=zonaconsulta)


ayuda = Menu(barraMenu, tearoff=0)
ayuda.add_command(label='licencia')
ayuda.add_command(label='acerca de:')

barraMenu.add_cascade(label="bbdd", menu=bbddMenu)
barraMenu.add_cascade(label="limpiar", menu=limpiar)
barraMenu.add_cascade(label="Zonas", menu=Zonas)
barraMenu.add_cascade(label="opciones", menu=opciones)
barraMenu.add_cascade(label="ayuda", menu=ayuda)


gestorclientes = Frame(paladin)
gestorclientes.place(y=1, x=1, width=306, height=500)
codigolabel = Label(gestorclientes, text='Codigo:')
codigolabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

clientelabel = Label(gestorclientes, text='Cliente:')
clientelabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

saldolabel = Label(gestorclientes, text='Saldo:')
saldolabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

zonalabel = Label(gestorclientes, text='Zona:')
zonalabel.grid(row=3, column=0, sticky='e', padx=10, pady=10)

telefonolabel = Label(gestorclientes, text='Telefono:')
telefonolabel.grid(row=4, column=0, sticky='e', padx=10, pady=10)

compraslabel = Label(gestorclientes, text='ult_abono:')
compraslabel.grid(row=5, column=0, sticky='e', padx=10, pady=10)

textolabel = Label(gestorclientes, text='Descripcion:')
textolabel.grid(row=6, column=0, sticky='e', padx=10, pady=10)

# -------------------------------------------------------------------

cuadrocodigo = Entry(gestorclientes, textvariable=codigo)
cuadrocodigo.grid(row=0, column=1, padx=10, pady=10,columnspan=2)

cuadrocliente = Entry(gestorclientes, textvariable=cliente)
cuadrocliente.grid(row=1, column=1, padx=10, pady=10)
cuadrocliente.config(fg='blue')

cuadrosaldo = Entry(gestorclientes, textvariable=saldo)
cuadrosaldo.grid(row=2, column=1, padx=10, pady=10)

cuadrozona = Entry(gestorclientes, textvariable=zona)
cuadrozona.grid(row=3, column=1, padx=10, pady=10)

cuadrotelefono = Entry(gestorclientes, textvariable=telefono)
cuadrotelefono.grid(row=4, column=1, padx=10, pady=10)

cuadrocompras = Entry(gestorclientes, textvariable=ult_abono)
cuadrocompras.grid(row=5, column=1, padx=15, pady=15)

observacion = Text(gestorclientes, width=16, height=5)
observacion.grid(row=6, column=1, padx=10, pady=10,rowspan=2,ipady=20)
scrollvert = Scrollbar(gestorclientes, command=observacion.yview)
scrollvert.grid(row=6, column=3, sticky='nsew',rowspan=2)
observacion.config(yscrollcommand=scrollvert)

ventana = Frame(paladin)
ventana.place(x=310, y=1, width=380, height=500)
ventana_texto = Listbox(ventana, bg='#000',fg='#fff')
ventana_texto.grid(row=0,column=0,columnspan=4,rowspan=5,padx=10,pady=10,ipadx=100,ipady=60)
client= Label(ventana,text='Codigo: ')
client.grid(row=6,column=0, sticky='e', padx=10, pady=5)
cuadroclient = Entry(ventana, textvariable=codigoventana)
cuadroclient.grid(row=6, column=1, padx=10, pady=5)
cuadroclient.config(justify='right')
clien= Label(ventana,text='Abono: ')
clien.grid(row=7,column=0, sticky='e', padx=10, pady=5)
cuadroclietee = Entry(ventana, textvariable=abono)
cuadroclietee.grid(row=7, column=1, padx=10, pady=5)
cuadroclietee.config(justify='right')
botonDev = Button(ventana, text='Devolucion', command=devolucion)
botonDev.grid(row=10, column=2, sticky='e', padx=10, pady=5)
botonconsultarV = Button(ventana, text='Consultar Ventas', command=consultarventas)
botonconsultarV.grid(row=9, column=2, sticky='e', padx=10, pady=5)
botonconsultar = Button(ventana, text='Consultar', command=consultar)
botonconsultar.grid(row=6, column=2, sticky='e', padx=10, pady=5)
botonabonar = Button(ventana, text='abonar', command=lambda: restar(int(abono.get())))
botonabonar.grid(row=7, column=2, sticky='e', padx=10, pady=5)
botonavv= Button(ventana, text='Vender', command=lambda:vender(int(precioventas.get())))
botonavv.grid(row=8, column=2, sticky='e', padx=10, pady=5)
vlabel2 = Label(ventana, text='articulo:')
vlabel2.grid(row=8, column=0, sticky='e', padx=10, pady=5)
vplabel2 = Label(ventana, text='precio:')
vplabel2.grid(row=9, column=0, sticky='e', padx=10, pady=5)
cuadrovl2 = Entry(ventana, textvariable=descripcionventa)
cuadrovl2.grid(row=8, column=1, padx=10, pady=5)
cuadrovl2.config(justify='right')
cuadrovp = Entry(ventana, textvariable=precioventas)
cuadrovp.grid(row=9, column=1, padx=10, pady=5)
cuadrovp.config(justify='right')
scrollvert1 = Scrollbar(ventana, command=ventana_texto.yview)
scrollvert1.grid(row=0, column=6, sticky='nsew',rowspan=2)
ventana_texto.config(yscrollcommand=scrollvert)
vplabel = Label(ventana, text='# Factura')
vplabel.grid(row=10, column=0, sticky='e', padx=10, pady=5)
cuadrovl = Entry(ventana, textvariable=numerodevolucion)
cuadrovl.grid(row=10, column=1, padx=10, pady=5)


gestionabonos = Frame(paladin)
gestionabonos.place(x=693, y=1, width=306, height=500)
zonalabel = Label(gestionabonos, text='Zona:')
zonalabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)
flabel = Label(gestionabonos, text='Fecha cobro:')
flabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)
cuadrozonaabonos = Entry(gestionabonos, textvariable=zonavtv)
cuadrozonaabonos.grid(row=1, column=1, padx=15, pady=15)
cuadrozonaabonos.config(fg='red')
cuadrofechaactual = Entry(gestionabonos, textvariable=fechaactual)
cuadrofechaactual.grid(row=2, column=1, padx=15, pady=15)
cuadrofechaactual.config(fg='red')
totalclient2 = Label(gestionabonos, text='chequeados')
totalclient2.grid(row=3, column=0, sticky='e', padx=2, pady=5)
siabonados2 = Label(gestionabonos, text='pagaron')
siabonados2.grid(row=4, column=0, sticky='e', padx=2, pady=5)
noabonados2 = Label(gestionabonos, text='No pagaron')
noabonados2.grid(row=5, column=0, sticky='e', padx=2, pady=5)
cobro2 = Label(gestionabonos, text='Cobro')
cobro2.grid(row=6, column=0, sticky='e', padx=2, pady=5)
ventas2 = Label(gestionabonos, text='Ventas')
ventas2.grid(row=7, column=0, sticky='e', padx=5, pady=5)





def resul():
    siabonados3 = Label(gestionabonos, text=siabonados.get())
    siabonados3.grid(row=4, column=1, sticky='e', padx=5, pady=5)
    noabonados3 = Label(gestionabonos, text=noabonados.get())
    noabonados3.grid(row=5, column=1, sticky='e', padx=5, pady=5)
    cobro3 = Label(gestionabonos, text=totalcobro.get())
    cobro3.grid(row=6, column=1, sticky='e', padx=5, pady=5)
    totalabonados.set(int(siabonados.get())+int(noabonados.get()))
    totalclient3 = Label(gestionabonos, text=(totalabonados.get(),'/',clientesenzona.get()))
    totalclient3.grid(row=3, column=1, sticky='e', padx=5, pady=5)
    ventas3 = Label(gestionabonos, text=ventass.get())
    ventas3.grid(row=7, column=1, sticky='e', padx=5, pady=5)

botoniniciar = Button(gestionabonos, text='INICIAR',fg='green', command=iniciar)
botoniniciar.grid(row=1, column=3, sticky='n', padx=5, pady=5)
botonfin = Button(gestionabonos, text='FIN',fg='red', command=fin)
botonfin.grid(row=2, column=3, sticky='n', padx=5, pady=5)



botoncrear = Button(gestorclientes, text='Crear', command=crear)
botoncrear.grid(row=8, column=0, sticky='w', padx=5, pady=5)

botonbuscar = Button(gestorclientes, text='Buscar', command=leer)
botonbuscar.grid(row=9, column=0, sticky='w', padx=5, pady=5)

botonmodificar = Button(gestorclientes, text='Modificar', command=actualizar)
botonmodificar.grid(row=8, column=1, sticky='w', padx=5, pady=5)

botonborrar = Button(gestorclientes, text='limpiar', command=limpiarC)

botonborrar.grid(row=9, column=1, sticky='w', padx=8, pady=8,ipadx=10)

img = PhotoImage(file="tul.gif")
widget = Label(gestionabonos, image=img).grid(sticky='e',columnspan=3,padx=10,pady=30)

paladin.mainloop()

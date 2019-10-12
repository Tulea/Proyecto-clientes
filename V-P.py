from tkinter import *
from tkinter import messagebox




raiz=Tk()

raiz.title('By_Tulea')
raiz.geometry('750x450')
raiz.config(bg='medium aquamarine')
frame=Frame()
frame.pack(fill='both',expand='True')
frame.config(bg='PaleGreen4')
frame.config(width='745',height='445')
frame.columnconfigure(5, weight=5)
frame.rowconfigure(5, weight=5)
frame.rowconfigure(5, weight=5)
Label(frame,text='Programa Control De Clientes',font=(12)).place(x=280,y=20)
#aqui va <<<imagen
def G_C():
    print('todo va bien')
    # poner las llamadas aqui
    from G_C import root as G_C_root
    G_C_root.mainloop()

def cobro_func():
    from Cobro import root as Cobro_root
    Cobro_root.mainloop()
    #*****************************************************************

# puedes crear mas llamadas
boton_client=Button(frame,text='Gestionar Clientes',width=3,command=G_C)
boton_client.place(relx=0.2, rely=0.2,relwidth=0.2, relheight=0.1)
#boton_client.pack()
boton_zona=Button(frame,text='Zonas',width=3,command=G_C)
boton_zona.place(relx=0.6, rely=0.8,relwidth=0.2, relheight=0.1)
#boton_zona.pack()
boton_cobro=Button(frame,text='Check Cobro',width=3,command=cobro_func)
boton_cobro.place(relx=0.6, rely=0.2,relwidth=0.2, relheight=0.1)
#boton_cobro.pack()
boton_cobros=Button(frame,text='Ver Cobros Anteriores',width=3,command=G_C)
boton_cobros.place(relx=0.2, rely=0.8,relwidth=0.2, relheight=0.1)





raiz.mainloop()

# Developer: Universidad
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk
from tkinter import Frame
from tkinter import StringVar
import os
import time
import mysql.connector as sql

# crear ventana
v0=Tk()
v0.title("Controles GPIO")
v0.geometry("1575x560+200+200")
fr1=ttk.Frame(v0,height="300",width="500")
fr2=ttk.Frame(v0,height="300",width="500")
fr3=ttk.Frame(v0,height="300",width="500")

table_data=ttk.Treeview(v0, columns=("col0","col1","col2","col3"),show="headings")

fr1.grid(row=0,column=0,padx=10,pady=20)
fr2.grid(row=0,column=1,padx=10,pady=20)
fr3.grid(row=0,column=2,padx=10,pady=20)

table_data.grid(row=1,column=0,sticky=E+W,columnspan=4)

scrollbar = ttk.Scrollbar(v0, orient=VERTICAL, command=table_data.yview)
table_data.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky='ns')

#texto
text1=font.Font(family="Arial", size=80)
text2=font.Font(family="Arial",size=16)


#llamado de la funcion
def clean():
            horai.set('')
            minini.set('')
            horaf.set('')
            minf.set('')
            
#imagenes
img_on=PhotoImage(file="/home/msabillon/ProyectoFinal/on.png").subsample(4)
img_off=PhotoImage(file="/home/msabillon/ProyectoFinal/off.png").subsample(4)

#-----------------------------------------Mostrar informacion de mysql-----------------------------------------

def VaciarDatos():                
                   informacion=table_data.get_children()
                   for cant in informacion:
                       table_data.delete(cant)
def LlenarTabla():
                  conexion=sql.connect(host="localhost",user="sabillon",password="123456",database="bdarqui")
                  consulta=StringVar()
                  consulta="SELECT * FROM arqui"
                  cursor=conexion.cursor()
                  cursor.execute(consulta)
                  resultado=cursor.fetchall()

                  for valor in resultado:
                                         table_data.insert("","0",values=valor)

                  conexion.close()

table_data.column("#0",width=0,anchor=CENTER)
table_data.column("col0",width=100,anchor=CENTER)
table_data.column("col1",width=140,anchor=CENTER)
table_data.column("col2",width=140,anchor=CENTER)
table_data.column("col3",width=140,anchor=CENTER)

table_data.heading("col0",text="Id",anchor=CENTER)
table_data.heading("col1",text="Descripcion",anchor=CENTER)
table_data.heading("col2",text="Estado",anchor=CENTER)
table_data.heading("col3",text="Fecha",anchor=CENTER)

LlenarTabla()
                       
#----------------------------------------------------GPIO17----------------------------------------------------
def encenderGpios17():
               print("Encendido GPIO17")
               os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/on17.sh'))
               VaciarDatos()
               LlenarTabla()
               
        
def apagarGpios17():
              print("Apagado GPIO17")
              os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/off17.sh'))
              VaciarDatos()
              LlenarTabla()


#funcion recursiva
def actualiza1Gpios17():
                    pf=open("/home/msabillon/ProyectoFinal/estado17.txt","r")
                    for linea in pf:
                                    campo=linea.split("\n")
                                    campof=campo[0]
                                    if(campof=="1"):
                                                     label_onGpios17=Label(fr1,text="1",font=text1).place(x=160,y=60)
                                                     fr1.after(1000,actualiza1Gpios17)
                                    if(campof=="0"):
                                                    label_offGpios17=Label(fr1,text="0",font=text1).place(x=160,y=60)
                                                    fr1.after(1000,actualiza1Gpios17)

actualiza1Gpios17()

def actualiza2Gpios17():
                 pf2=open("/home/msabillon/ProyectoFinal/estado17.txt","r")
                 for linea in pf2:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   btn_1Gpios17=Button(fr1,image=img_on).place(x=250,y=60)
                                                   fr1.after(1000,actualiza2Gpios17)

                                  if (campof=="0"):
                                                   btn_0Gpios17=Button(fr1,image=img_off).place(x=250,y=60)
                                                   fr1.after(1000,actualiza2Gpios17)
                                                   
actualiza2Gpios17()

# Titulo
label_t17=Label(fr1,text="CONTROL GPIO 17",font=text2,fg="blue",bg="ghostwhite").place(x=120,y=10)
# Zona de Botones
btn_onGpios17=Button(fr1,text="ON",command=encenderGpios17,fg="white",bg="green").place(x=88,y=75)
btn_offGpios17=Button(fr1,text="OFF",command=apagarGpios17,fg="white",bg="green").place(x=85,y=110)

#------------------------------------------------ GUI TIEMPO ------------------------------------------------

text3=font.Font(family="Arial",size=12)


def Salvar_TiempoGpios17():
                     print("Registrando Tiempo GPIO17")
                     hi=horai.get()
                     mi=minini.get()
                     hf=horaf.get()
                     mf=minf.get()
                     tab=" "
                     dia="*"
                     mes="*"
                     ism="*"
                     user="root"
                     path1="/home/msabillon/ProyectoFinal/on17.sh"
                     path2="/home/msabillon/ProyectoFinal/off17.sh"

                     cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                     cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
                     
                     #Asignar full acceso escritura
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura1'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura2'))

                     pf1=open("/etc/cron.d/lectura1","w")
                     pf1.write(cadena1)
                     pf1.write("\n")
                     pf1.close()

                     pf2=open("/etc/cron.d/lectura2","w")
                     pf2.write(cadena2)
                     pf2.write("\n")
                     pf2.close()          

                     #Pausa Estratetica
                     time.sleep(0.1)

                     # Revertir Permisos
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura1'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura2'))

                     # Reiniciar servicio cron

                     os.system("echo %s|sudo -S %s" % ('123456','sudo /./etc/init.d/cron restart'))
                     #os.system("sudo /./etc/init.d/cron restart")

                     # invocar la funcion privada clean()
                     clean()
                               
def DialogoTiempoGpios17():
                     print("Programando Tiempo GPIO17")
                     v1=Toplevel()
                     v1.title("Temporizador GPIO17")
                     v1.geometry("310x200")
                     # Etiquetas
                     label_t2=Label(v1,text="--- TEMPORIZADOR ---",font=text3).place(x=10,y=5)
                     label_horai=Label(v1,text="Hora Encendido:",font=text3).place(x=10,y=50)
                     label_minini=Label(v1,text="Minuto Encendido:",font=text3).place(x=10,y=90)
                     label_horaf=Label(v1,text="Hora Apagado:",font=text3).place(x=10,y=130)
                     label_minf=Label(v1,text="Minuto Apagado:",font=text3).place(x=10,y=170)

                     # Variables Cajas de texto para el Temporizador
                     global horai,minini,horaf,minf
                     horai=StringVar()
                     minini=StringVar()
                     horaf=StringVar()
                     minf=StringVar()

                     # Cajas de Texto
                     txt_horai=Entry(v1,textvariable=horai,width=10).place(x=150,y=50)
                     txt_minini=Entry(v1,textvariable=minini,width=10).place(x=150,y=90)
                     txt_horaf=Entry(v1,textvariable=horaf,width=10).place(x=150,y=130)
                     txt_minf=Entry(v1,textvariable=minf,width=10).place(x=150,y=170)

                     # botones
                     btn_salvarGpios17=Button(v1,text="SAVE",command=Salvar_TiempoGpios17).place(x=240,y=100)
                     
                     
                     v1.mainloop()
                     
                    
btn_tiempoGpios17=Button(fr1,text="Tiempo",command=DialogoTiempoGpios17,bg="green",fg="beige").place(x=0,y=90)
# Funciones

def EvaluarCheckBoxGpios17():                    
                      ck=checkGpios17.get()
                      if (ck=="1"):
                                   encenderGpios17()
                      if (ck=="0"):
                                   apagarGpios17()

def EvaluarRadiobuttonGpios17():
                         r=radioGpios17.get()
                         if (r=="1"):
                                   encenderGpios17()
                         if (r=="0"):
                                   apagarGpios17()
                                   
def EvaluarComboGpios17():
                    cmb=comboGpios17.get()
                    ckm=sndemailGpios17.get()
                    if (ckm=="1"):                        
                                  if (cmb=="ON"):
                                                 encenderGpios17()
                                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOn17.sh'))
                                  if (cmb=="OFF"):
                                                  apagarGpios17()
                                                  os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOff17.sh'))
                    else:
                         if (cmb=="ON"):
                                        encenderGpios17()
                         if (cmb=="OFF"):
                                         apagarGpios17()
                                  

def EvaluarEmailGpios17():
                   ckm=ckemailGpios17.get()
                   if (ckm=="1"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/lecturaInbox17.sh &'))
                                 messagebox.showinfo("save",message="Email Receive Service GPIO17 --enabled--")
                                 
                                 
                   if (ckm=="0"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo pkill -f lecturaInbox17.sh'))
                                 VaciarDatos()
                                 LlenarTabla()
                                 messagebox.showinfo("save",message="Email Receive Service GPIO17--disabled--")

def EnviarEmailGpios17():
                   ckm=sndemailGpios17.get()                   
                   if (ckm=="1"):
                                 messagebox.showinfo("save",message="Email Send Service GPIO17 --enabled--")                      
                   if (ckm=="0"):                                                             
                                 messagebox.showinfo("save",message="Email Send Service GPIO17 --disabled--")
                                        
                                                                  
# Control CheckBox
global checkGpios17
checkGpios17=StringVar()
c1Gpios17=ttk.Checkbutton(fr1,text="ON/OFF",variable=checkGpios17,command=EvaluarCheckBoxGpios17)
c1Gpios17.place(x=10,y=150)

# Control RadioButton
global radioGpios17
radioGpios17=StringVar()
r1Gpios17=ttk.Radiobutton(fr1,text="ON",variable=radioGpios17,value=1,command=EvaluarRadiobuttonGpios17)
r1Gpios17.place(x=10,y=180)
r2Gpios17=ttk.Radiobutton(fr1,text="OFF",variable=radioGpios17,value=0,command=EvaluarRadiobuttonGpios17)
r2Gpios17.place(x=60,y=180)

# Coontrol Combobox
global comboGpios17
comboGpios17=StringVar()
cGpios17=ttk.Combobox(fr1,textvariable=comboGpios17,values=["ON","OFF"])
cGpios17.place(x=150,y=215)
btn_ejecutarGpios17=Button(fr1,text=">>",command=EvaluarComboGpios17,bg="darkcyan").place(x=330,y=210)

# checkbox-recibir-email
global ckemailGpios17
ckemailGpios17=StringVar()
ck1Gpios17=ttk.Checkbutton(fr1,text="Enable/Disable Receive Email",variable=ckemailGpios17,command=EvaluarEmailGpios17)
ck1Gpios17.place(x=0,y=280)

# checkbox-enviar-email
global sndemailGpios17
sndemailGpios17=StringVar()
ck1Gpios17=ttk.Checkbutton(fr1,text="Enable/Disable Send Email",variable=sndemailGpios17,command=EnviarEmailGpios17)
ck1Gpios17.place(x=150,y=245)

#----------------------------------------------------GPIO22----------------------------------------------------
def encenderGpios22():
               print("Encendido GPIO22")
               os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/on22.sh'))
               VaciarDatos()
               LlenarTabla()
        
def apagarGpios22():
              print("Apagado GPIO22")
              os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/off22.sh'))
              VaciarDatos()
              LlenarTabla()
              


#funcion recursiva
def actualiza1Gpios22():
                    pf=open("/home/msabillon/ProyectoFinal/estado22.txt","r")
                    for linea in pf:
                                    campo=linea.split("\n")
                                    campof=campo[0]
                                    if(campof=="1"):
                                                     label_onGpios22=Label(fr2,text="1",font=text1).place(x=160,y=60)
                                                     fr2.after(1000,actualiza1Gpios22)
                                    if(campof=="0"):
                                                    label_offGpios22=Label(fr2,text="0",font=text1).place(x=160,y=60)
                                                    fr2.after(1000,actualiza1Gpios22)

actualiza1Gpios22()

def actualiza2Gpios22():
                 pf2=open("/home/msabillon/ProyectoFinal/estado22.txt","r")
                 for linea in pf2:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   btn_1Gpios22=Button(fr2,image=img_on).place(x=250,y=60)
                                                   fr2.after(1000,actualiza2Gpios22)

                                  if (campof=="0"):
                                                   btn_0Gpios22=Button(fr2,image=img_off).place(x=250,y=60)
                                                   fr2.after(1000,actualiza2Gpios22)
                                                   
actualiza2Gpios22()

# Titulo
label_t22=Label(fr2,text="CONTROL GPIO 22",font=text2,fg="green",bg="ghostwhite").place(x=120,y=10)
# Zona de Botones
btn_onGpios22=Button(fr2,text="ON",command=encenderGpios22,fg="white",bg="green").place(x=88,y=75)
btn_offGpios22=Button(fr2,text="OFF",command=apagarGpios22,fg="white",bg="green").place(x=85,y=110)

#------------------------------------------------ GUI TIEMPO ------------------------------------------------


def Salvar_TiempoGpios22():
                     print("Registrando Tiempo GPIO22")
                     hi=horai.get()
                     mi=minini.get()
                     hf=horaf.get()
                     mf=minf.get()
                     tab=" "
                     dia="*"
                     mes="*"
                     ism="*"
                     user="root"
                     path1="/home/msabillon/ProyectoFinal/on22.sh"
                     path2="/home/msabillon/ProyectoFinal/off22.sh"

                     cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                     cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
                     
                     # Asignar full acceso escritura
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura4'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura3'))

                     pf1=open("/etc/cron.d/lectura4","w")
                     pf1.write(cadena1)
                     pf1.write("\n")
                     pf1.close()

                     pf2=open("/etc/cron.d/lectura3","w")
                     pf2.write(cadena2)
                     pf2.write("\n")
                     pf2.close()          

                     #Pausa Estratetica
                     time.sleep(0.1)

                     # Revertir Permisos
                     #os.system("sudo chmod 755 /etc/cron.d/tarea1")
                     #os.system("sudo chmod 755 /etc/cron.d/tarea2")
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura4'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura3'))

                     # Reiniciar servicio cron

                     os.system("echo %s|sudo -S %s" % ('123456','sudo /./etc/init.d/cron restart'))
                     #os.system("sudo /./etc/init.d/cron restart")

                     # invocar la funcion privada clean()
                     clean()
                               
def DialogoTiempoGpios22():
                     print("Programando Tiempo GPIO22")
                     v1=Toplevel()
                     v1.title("Temporizador GPIO22")
                     v1.geometry("310x200")
                     # Etiquetas
                     label_t2=Label(v1,text="--- TEMPORIZADOR ---",font=text3).place(x=10,y=5)
                     label_horai=Label(v1,text="Hora Encendido:",font=text3).place(x=10,y=50)
                     label_minini=Label(v1,text="Minuto Encendido:",font=text3).place(x=10,y=90)
                     label_horaf=Label(v1,text="Hora Apagado:",font=text3).place(x=10,y=130)
                     label_minf=Label(v1,text="Minuto Apagado:",font=text3).place(x=10,y=170)

                     # Variables Cajas de texto para el Temporizador
                     global horai,minini,horaf,minf
                     horai=StringVar()
                     minini=StringVar()
                     horaf=StringVar()
                     minf=StringVar()

                     # Cajas de Texto
                     txt_horai=Entry(v1,textvariable=horai,width=10).place(x=150,y=50)
                     txt_minini=Entry(v1,textvariable=minini,width=10).place(x=150,y=90)
                     txt_horaf=Entry(v1,textvariable=horaf,width=10).place(x=150,y=130)
                     txt_minf=Entry(v1,textvariable=minf,width=10).place(x=150,y=170)

                     # botones
                     btn_salvarGpios22=Button(v1,text="SAVE",command=Salvar_TiempoGpios22).place(x=240,y=100)
                     
                     
                     v1.mainloop()
                     
                    
btn_tiempoGpios22=Button(fr2,text="Tiempo",command=DialogoTiempoGpios22,bg="green",fg="beige").place(x=0,y=90)
# Funciones

def EvaluarCheckBoxGpios22():                    
                      ck=checkGpios22.get()
                      if (ck=="1"):
                                   encenderGpios22()
                      if (ck=="0"):
                                   apagarGpios22()

def EvaluarRadiobuttonGpios22():
                         r=radioGpios22.get()
                         if (r=="1"):
                                   encenderGpios22()
                         if (r=="0"):
                                   apagarGpios22()
                                   
def EvaluarComboGpios22():
                    cmb=comboGpios22.get()
                    ckm=sndemailGpios22.get()
                    if (ckm=="1"):                        
                                  if (cmb=="ON"):
                                                 encenderGpios22()
                                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOn22.sh'))
                                  if (cmb=="OFF"):
                                                  apagarGpios22()
                                                  os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOff22.sh'))
                    else:
                         if (cmb=="ON"):
                                        encenderGpios22()
                         if (cmb=="OFF"):
                                         apagarGpios22()
                                  

def EvaluarEmailGpios22():
                   ckm=ckemailGpios22.get()
                   if (ckm=="1"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/lecturaInbox22.sh &'))
                                 messagebox.showinfo("save",message="Email Receive Service GPIO22 --enabled--")
                                 
                                 
                   if (ckm=="0"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo pkill -f lecturaInbox22.sh'))
                                 VaciarDatos()
                                 LlenarTabla()
                                 messagebox.showinfo("save",message="Email Receive Service GPIO22 --disabled--")

def EnviarEmailGpios22():
                   ckm=sndemailGpios22.get()                   
                   if (ckm=="1"):
                                 messagebox.showinfo("save",message="Email Send Service GPIO22 --enabled--")                      
                   if (ckm=="0"):                                                             
                                 messagebox.showinfo("save",message="Email Send Service GPIO22 --disabled--")
                                        
                                                                  
# Control CheckBox
global checkGpios22
checkGpios22=StringVar()
c1Gpios22=ttk.Checkbutton(fr2,text="ON/OFF",variable=checkGpios22,command=EvaluarCheckBoxGpios22)
c1Gpios22.place(x=10,y=150)

# Control RadioButton
global radioGpios22
radioGpios22=StringVar()
r1Gpios22=ttk.Radiobutton(fr2,text="ON",variable=radioGpios22,value=1,command=EvaluarRadiobuttonGpios22)
r1Gpios22.place(x=10,y=180)
r2Gpios22=ttk.Radiobutton(fr2,text="OFF",variable=radioGpios22,value=0,command=EvaluarRadiobuttonGpios22)
r2Gpios22.place(x=60,y=180)

# Coontrol Combobox
global comboGpios22
comboGpios22=StringVar()
cGpios22=ttk.Combobox(fr2,textvariable=comboGpios22,values=["ON","OFF"])
cGpios22.place(x=150,y=215)
btn_ejecutarGpios22=Button(fr2,text=">>",command=EvaluarComboGpios22,bg="darkcyan").place(x=330,y=210)

# checkbox-recibir-email
global ckemailGpios22
ckemailGpios22=StringVar()
ck1Gpios22=ttk.Checkbutton(fr2,text="Enable/Disable Receive Email",variable=ckemailGpios22,command=EvaluarEmailGpios22)
ck1Gpios22.place(x=0,y=280)

# checkbox-enviar-email
global sndemailGpios22
sndemailGpios22=StringVar()
ck1Gpios22=ttk.Checkbutton(fr2,text="Enable/Disable Send Email",variable=sndemailGpios22,command=EnviarEmailGpios22)
ck1Gpios22.place(x=150,y=245)

#----------------------------------------------------GPIO27----------------------------------------------------

def encenderGpios27():
               print("Encendido GPIO27")
               os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/on27.sh'))
               VaciarDatos()
               LlenarTabla()
        
def apagarGpios27():
              print("Apagado GPIO27")
              os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/off27.sh'))
              VaciarDatos()
              LlenarTabla()
              


#funcion recursiva
def actualiza1Gpios27():
                    pf=open("/home/msabillon/ProyectoFinal/estado27.txt","r")
                    for linea in pf:
                                    campo=linea.split("\n")
                                    campof=campo[0]
                                    if(campof=="1"):
                                                     label_onGpios27=Label(fr3,text="1",font=text1).place(x=160,y=60)
                                                     fr3.after(1000,actualiza1Gpios27)
                                    if(campof=="0"):
                                                    label_offGpios27=Label(fr3,text="0",font=text1).place(x=160,y=60)
                                                    fr3.after(1000,actualiza1Gpios27)

actualiza1Gpios27()

def actualiza2Gpios27():
                 pf2=open("/home/msabillon/ProyectoFinal/estado27.txt","r")
                 for linea in pf2:
                                  campo=linea.split("\n")
                                  campof=campo[0]
                                  if (campof=="1"):
                                                   btn_1Gpios27=Button(fr3,image=img_on).place(x=250,y=60)
                                                   fr3.after(1000,actualiza2Gpios27)

                                  if (campof=="0"):
                                                   btn_0Gpios27=Button(fr3,image=img_off).place(x=250,y=60)
                                                   fr3.after(1000,actualiza2Gpios27)
                                                   
actualiza2Gpios27()

# Titulo
label_t27=Label(fr3,text="CONTROL GPIO 27",font=text2,fg="red",bg="ghostwhite").place(x=120,y=10)
# Zona de Botones
btn_onGpios27=Button(fr3,text="ON",command=encenderGpios27,fg="white",bg="green").place(x=88,y=75)
btn_offGpios27=Button(fr3,text="OFF",command=apagarGpios27,fg="white",bg="green").place(x=85,y=110)

#------------------------------------------------ GUI TIEMPO ------------------------------------------------


def Salvar_TiempoGpios27():
                     print("Registrando Tiempo GPIO27")
                     hi=horai.get()
                     mi=minini.get()
                     hf=horaf.get()
                     mf=minf.get()
                     tab=" "
                     dia="*"
                     mes="*"
                     ism="*"
                     user="root"
                     path1="/home/msabillon/ProyectoFinal/on27.sh"
                     path2="/home/msabillon/ProyectoFinal/off27.sh"

                     cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                     cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
                     
                     # Asignar full acceso escritura
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura6'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 777 /etc/cron.d/lectura5'))

                     pf1=open("/etc/cron.d/lectura6","w")
                     pf1.write(cadena1)
                     pf1.write("\n")
                     pf1.close()

                     pf2=open("/etc/cron.d/lectura5","w")
                     pf2.write(cadena2)
                     pf2.write("\n")
                     pf2.close()          

                     #Pausa Estratetica
                     time.sleep(0.1)

                     # Revertir Permisos
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura6'))
                     os.system("echo %s|sudo -S %s" % ('123456','chmod -R 755 /etc/cron.d/lectura5'))

                     # Reiniciar servicio cron

                     os.system("echo %s|sudo -S %s" % ('123456','sudo /./etc/init.d/cron restart'))
                     #os.system("sudo /./etc/init.d/cron restart")

                     # invocar la funcion privada clean()
                     clean()
                               
def DialogoTiempoGpios27():
                     print("Programando Tiempo GPIO27")
                     v1=Toplevel()
                     v1.title("Temporizador GPIO27")
                     v1.geometry("310x200")
                     # Etiquetas
                     label_t2=Label(v1,text="--- TEMPORIZADOR ---",font=text3).place(x=10,y=5)
                     label_horai=Label(v1,text="Hora Encendido:",font=text3).place(x=10,y=50)
                     label_minini=Label(v1,text="Minuto Encendido:",font=text3).place(x=10,y=90)
                     label_horaf=Label(v1,text="Hora Apagado:",font=text3).place(x=10,y=130)
                     label_minf=Label(v1,text="Minuto Apagado:",font=text3).place(x=10,y=170)

                     # Variables Cajas de texto para el Temporizador
                     global horai,minini,horaf,minf
                     horai=StringVar()
                     minini=StringVar()
                     horaf=StringVar()
                     minf=StringVar()

                     # Cajas de Texto
                     txt_horai=Entry(v1,textvariable=horai,width=10).place(x=150,y=50)
                     txt_minini=Entry(v1,textvariable=minini,width=10).place(x=150,y=90)
                     txt_horaf=Entry(v1,textvariable=horaf,width=10).place(x=150,y=130)
                     txt_minf=Entry(v1,textvariable=minf,width=10).place(x=150,y=170)

                     # botones
                     btn_salvarGpios27=Button(v1,text="SAVE",command=Salvar_TiempoGpios27).place(x=240,y=100)
                     
                     
                     v1.mainloop()
                     
                    
btn_tiempoGpios27=Button(fr3,text="Tiempo",command=DialogoTiempoGpios27,bg="green",fg="beige").place(x=0,y=90)
# Funciones

def EvaluarCheckBoxGpios27():                    
                      ck=checkGpios27.get()
                      if (ck=="1"):
                                   encenderGpios27()
                      if (ck=="0"):
                                   apagarGpios27()

def EvaluarRadiobuttonGpios27():
                         r=radioGpios27.get()
                         if (r=="1"):
                                   encenderGpios27()
                         if (r=="0"):
                                   apagarGpios27()
                                   
def EvaluarComboGpios27():
                    cmb=comboGpios27.get()
                    ckm=sndemailGpios27.get()
                    if (ckm=="1"):                        
                                  if (cmb=="ON"):
                                                 encenderGpios27()
                                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOn27.sh'))
                                  if (cmb=="OFF"):
                                                  apagarGpios27()
                                                  os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/sendEmailOff27.sh'))
                    else:
                         if (cmb=="ON"):
                                        encenderGpios27()
                         if (cmb=="OFF"):
                                         apagarGpios27()
                                  

def EvaluarEmailGpios27():
                   ckm=ckemailGpios27.get()
                   if (ckm=="1"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo /./home/msabillon/ProyectoFinal/lecturaInbox27.sh &'))
                                 messagebox.showinfo("save",message="Email Receive Service GPIO27 --enabled--")                                                                 
                                 
                   if (ckm=="0"):
                                 os.system("echo %s|sudo -S %s" % ('123456','sudo pkill -f lecturaInbox27.sh'))
                                 VaciarDatos()
                                 LlenarTabla()
                                 messagebox.showinfo("save",message="Email Receive Service GPIO27 --disabled--")

def EnviarEmailGpios27():
                   ckm=sndemailGpios27.get()                   
                   if (ckm=="1"):
                                 messagebox.showinfo("save",message="Email Send Service GPIO27 --enabled--")                      
                   if (ckm=="0"):                                                             
                                 messagebox.showinfo("save",message="Email Send Service GPIO27 --disabled--")
                                        
                                                                 
# Control CheckBox
global checkGpios27
checkGpios27=StringVar()
c1Gpios27=ttk.Checkbutton(fr3,text="ON/OFF",variable=checkGpios27,command=EvaluarCheckBoxGpios27)
c1Gpios27.place(x=10,y=150)

# Control RadioButton
global radioGpios27
radioGpios27=StringVar()
r1Gpios27=ttk.Radiobutton(fr3,text="ON",variable=radioGpios27,value=1,command=EvaluarRadiobuttonGpios27)
r1Gpios27.place(x=10,y=180)
r2Gpios27=ttk.Radiobutton(fr3,text="OFF",variable=radioGpios27,value=0,command=EvaluarRadiobuttonGpios27)
r2Gpios27.place(x=60,y=180)

# Control Combobox
global comboGpios27
comboGpios27=StringVar()
cGpios27=ttk.Combobox(fr3,textvariable=comboGpios27,values=["ON","OFF"])
cGpios27.place(x=150,y=215)
btn_ejecutarGpios27=Button(fr3,text=">>",command=EvaluarComboGpios27,bg="darkcyan").place(x=330,y=210)

# checkbox-recibir-email
global ckemailGpios27
ckemailGpios27=StringVar()
ck1Gpios27=ttk.Checkbutton(fr3,text="Enable/Disable Receive Email",variable=ckemailGpios27,command=EvaluarEmailGpios27)
ck1Gpios27.place(x=0,y=280)

# checkbox-enviar-email
global sndemailGpios27
sndemailGpios27=StringVar()
ck1Gpios27=ttk.Checkbutton(fr3,text="Enable/Disable Send Email",variable=sndemailGpios27,command=EnviarEmailGpios27)
ck1Gpios27.place(x=150,y=245)


                    
v0.resizable(False,False)
v0.mainloop()

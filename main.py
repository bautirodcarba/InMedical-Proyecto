import tkinter
import os
from os import remove


def registerScreen():
    def backProcess():
        text = tkinter.Label(regScreen)
        text.pack()
        text.after(500)
        regScreen.destroy()
        loginScreen()

    def refreshCredentials():
        userarchive = open("data/credentials/userarchive.txt","w")
        passwordarchive = open("data/credentials/passwordarchive.txt","w")
        userarchive.write(username.get())
        passwordarchive.write(password.get())
        userarchive.close()
        passwordarchive.close()
        text = tkinter.Label(regScreen)
        text.pack()
        text.after(500)
        regScreen.destroy()
        loginScreen()

    def checkPass():
        if password.get() == passwordtwo.get():
            uploadbtn = tkinter.Button(regScreen,text="Subir credenciales",justify="center",bg="green",command=refreshCredentials,font="30")
            uploadbtn.place(x=200,y=325,width=200)
    regScreen = tkinter.Tk()
    regScreen.geometry("600x500")
    regScreen.title("InMedical-Registro de usuario")
    title = tkinter.Label(regScreen,text="Registro de usuario",font="40",justify="center",bg="green")
    title.pack(fill=tkinter.X)
    user = tkinter.Label(regScreen,text="Ingrese un nombre de usuario:",justify="center",font="20")
    user.place(x=200,y=100)
    username = tkinter.Entry(regScreen)
    username.place(x=200,y=125,width=200)
    passtit = tkinter.Label(regScreen,text="Ingrese una contraseña:",justify="center",font="20")
    passtit.place(x=200,y=150)
    password = tkinter.Entry(regScreen)
    password.place(x=200,y=175,width=200)
    passtittwo = tkinter.Label(regScreen,text="Confirme la contraseña:",justify="center",font="20")
    passtittwo.place(x=200,y=200)
    passwordtwo = tkinter.Entry(regScreen)
    passwordtwo.place(x=200,y=225,width=200)
    confirmbtn = tkinter.Button(regScreen,text="Confirmar contraseñas",justify="center",command=checkPass,bg="green",font="30")
    confirmbtn.place(x=200,y=275,width=200)
    backbtn = tkinter.Button(regScreen,text="Regresar",font="30",justify="center",bg="green",command=backProcess)
    backbtn.place(x=200,y=400,width=200)
    regScreen.mainloop()

def loginScreen():
    def checkLogin():
        userarchive = open("data/credentials/userarchive.txt","r")
        passwordarchive = open("data/credentials/passwordarchive.txt","r")
        usercheck = usertext.get()
        passwordcheck = passwordtext.get()
        if usercheck.upper() == userarchive.readline().upper():
            if passwordcheck.upper() == passwordarchive.readline().upper():
                ingreso = tkinter.Label(logScreen,text="Credenciales correctas",justify="center",bg="blue")
                ingreso.pack()
                text = tkinter.Label(logScreen)
                text.pack()
                text.after(500)
                logScreen.destroy()
                mainScreen()
        else: 
            noingreso = tkinter.Label(logScreen,text="Credenciales incorrectas",font="20",justify="center",bg="red")
            noingreso.place(x=200,y=425,width=200,height=58)
        userarchive.close()
        passwordarchive.close()

    def confirmregister():
        text = tkinter.Label(logScreen)
        text.pack()
        text.after(500)
        logScreen.destroy()
        registerScreen()

    logScreen = tkinter.Tk()
    logScreen.geometry("600x500")
    logScreen.title("InMedical-Inicio de sesión")
    login = tkinter.Label(logScreen, text="InMedical",justify="center",bg="lightblue",font="40")
    login.pack(fill=tkinter.X)
    user = tkinter.Label(logScreen, text="Usuario",justify="center",font="30")
    user.place(x=200,y=100,width=200)
    usertext = tkinter.Entry(logScreen)
    usertext.place(x=200,y=130,width=200)
    password = tkinter.Label(logScreen,text="Contraseña",justify="center",font="30")
    password.place(x=200,y=160,width=200)
    passwordtext = tkinter.Entry(logScreen)
    passwordtext.place(x=200,y=190,width=200)
    loginbutton = tkinter.Button(logScreen,text="Ingresar",justify="center",command=checkLogin,bg="lightblue",font="30")
    loginbutton.place(x=200,y=220,width=200)
    register = tkinter.Label(logScreen,text="Si no existe una cuenta:",justify="center",font="30")
    register.place(x=200,y=260,width=200)
    registerbutton = tkinter.Button(logScreen,text="Registarse",justify="center",command=confirmregister,bg="lightblue",font="30")
    registerbutton.place(x=200,y=290,width=200)
    logScreen.mainloop()
    
def mainScreen():
    def gestionar():
        text = tkinter.Label(mScreen)
        text.pack()
        text.after(500)
        mScreen.destroy()
        gestionarScreen()
    def busqueda():
        text = tkinter.Label(mScreen)
        text.pack()
        text.after(500)
        mScreen.destroy()
        busquedaScreen()
    mScreen = tkinter.Tk()
    mScreen.title("InMedical")
    mScreen.geometry("600x500")
    uppertxt = tkinter.Label(mScreen,text="InMedical",justify="center",bg="lightblue",font="40")
    uppertxt.pack(fill=tkinter.X)
    personalbtn = tkinter.Button(mScreen,text="Gestionar personal",justify="center",bg="lightblue",font="20",command=gestionar)
    personalbtn.place(x=200,y=150,width=200,height=58)
    busquedabtn = tkinter.Button(mScreen,text="Busqueda",justify="center",bg="lightblue",font="20",command=busqueda)
    busquedabtn.place(x=200,y=300,width=200,height=58)
    mScreen.mainloop()

def gestionarScreen():
    ##callear endprocess con el lult boton
    def backProcess():
        text = tkinter.Label(gScreen)
        text.pack()
        text.after(500)
        gScreen.destroy()
        mainScreen()

    def altaScreen():
        def infoupload():
            name = nametext.get()
            provincia = provinciatext.get()
            domicilio = domiciliotext.get()
            especialidad = especialidadtext.get()
            ingreso = ingresotext.get()
            dias = daystext.get()
            guardia = guardiastext.get()
            sueldo = (int(dias)*(int(guardia)))*5.75
            archive = open(f"data/employees/{name}.txt","w+")
            archive.write(name+'\n')
            archive.write(provincia+'\n')
            archive.write(domicilio+'\n')
            archive.write(especialidad+'\n')
            archive.write(ingreso+'\n')
            archive.write(dias+'\n')
            archive.write(guardia+'\n')
            archive.write(str(sueldo))
            archive.close()
            listarchive = open("data/samplelist.txt","a")
            listarchive.writelines(f"\n{name}")
            listarchive.close()
            
        def backProcess():
            text = tkinter.Label(aScreen)
            text.pack()
            text.after(500)
            aScreen.destroy()
            gestionarScreen()

        text = tkinter.Label(gScreen)
        text.pack()
        text.after(500)
        gScreen.destroy()
        aScreen= tkinter.Tk()
        aScreen.geometry("600x500")
        aScreen.title("InMedical-Gestion de personal-Altas")
        uppertxt = tkinter.Label(aScreen,text="InMedical",justify="center",bg="lightblue",font="40")
        uppertxt.pack(fill=tkinter.X)
        exitbtn = tkinter.Button(aScreen,text="Regresar",justify="center",font="20",bg="lightblue",command=backProcess)
        exitbtn.place(x=200,y=400,width=200,height=58)
        namelbl = tkinter.Label(aScreen,text="Nombre y apellido:",justify="center",font="10")
        namelbl.pack()
        nametext = tkinter.Entry(aScreen)
        nametext.pack()
        provincialbl = tkinter.Label(aScreen,text="Provincia:",justify="center",font="10")
        provincialbl.pack()
        provinciatext = tkinter.Entry(aScreen)
        provinciatext.pack()
        domiciliolbl = tkinter.Label(aScreen,text="Domicilio:",justify="center",font="10")
        domiciliolbl.pack()
        domiciliotext = tkinter.Entry(aScreen)
        domiciliotext.pack()
        especialidadlbl = tkinter.Label(aScreen,text="Especialidad:",justify="center",font="10")
        especialidadlbl.pack()
        especialidadtext = tkinter.Entry(aScreen)
        especialidadtext.pack()
        ingresolbl = tkinter.Label(aScreen,text="Fecha de ingreso:",justify="center",font="10")
        ingresolbl.pack()
        ingresotext = tkinter.Entry(aScreen)
        ingresotext.pack()
        dayslbl = tkinter.Label(aScreen,text="Dias de trabajo:",justify="center",font="10")
        dayslbl.pack()
        daystext = tkinter.Entry(aScreen)
        daystext.pack()
        guardiaslbl = tkinter.Label(aScreen,text="Horas de guardia:",justify="center",font="10")
        guardiaslbl.pack()
        guardiastext = tkinter.Entry(aScreen)
        guardiastext.pack()
        altabtn = tkinter.Button(aScreen,text="Cargar datos",justify="center",bg="lightblue",font="20",command=infoupload)
        altabtn.place(x=200,y=330,height=58,width=200)
        aScreen.mainloop()

    def bajaScreen():
        def endProcess():
            text = tkinter.Label(bjScreen)
            text.pack()
            text.after(500)
            bjScreen.destroy()
            mainScreen()

        ##DELETEUSER NOT WORKING HELP##
        def deleteuser():
            newchar = []
            directory = 'data/employees'
            for item in deletelist.curselection():
                name=str(deletelist.get(item))
                for i in range(0,len(name)-1,1):
                    newchar += name[i]
                newname =''.join(newchar)
                newchar = []
                for filename in os.listdir(directory):                
                    x = str(filename)
                    for i in range(0,len(x)-4,1):
                        newchar += x[i]
                    newstr =''.join(newchar)
                    if newstr == newname:
                        remove(f"data/employees/{newstr}.txt")
                        ## ACTUALIZAR SAMPLELIST ##
                        filename = "data/samplelist.txt"
                        with open(filename) as fobj:
                            for line in fobj:
                                if line == newstr:
                                    fobj.write("BORRADO")
            
                    newchar = []
                    newstr = ''
            
        text = tkinter.Label(gScreen)
        text.pack()
        text.after(500)
        gScreen.destroy()
        bjScreen = tkinter.Tk()
        bjScreen.geometry("600x500")
        bjScreen.title("InMedical-Gestion de personal-Bajas")
        title = tkinter.Label(bjScreen,text="InMedical",justify="center",font="40",bg="lightblue")
        title.pack(fill=tkinter.X)
        nonsense = tkinter.Label(bjScreen,text="Selecccione empleado a borrar:",justify="center",font="20")
        nonsense.place(x=175,y=125,width=250)
        deletelist = tkinter.Listbox(bjScreen)
        filename = 'data/samplelist.txt'
        with open(filename) as fobj:
            for line in fobj:
                deletelist.insert(tkinter.END,line)
        deletelist.place(x=200,y=150,width=200,height=100)
        deletebtn = tkinter.Button(bjScreen,text="Eliminar",justify="center",font="20",bg="lightblue",command=deleteuser)
        deletebtn.place(x=250,y=275,width=100)
        backbtn = tkinter.Button(bjScreen,text="Regresar",font="20",justify="center",bg="lightblue",command=endProcess)
        backbtn.place(x=200,y=325,width=200,height=58)
        bjScreen.mainloop()

    def inverselist():
            ##even -> 1st apreto; ergo, reverse
        r = []
        userlist.delete(0,1000)
        with open(r"data/samplelist.txt", 'r') as fp:
            lines = len(fp.readlines())
            #print('Total Number of lines:', lines)
        filename = 'data/samplelist.txt'
        with open(filename) as fobj:
            for line in fobj:
                r.append(line)
        rev = list(reversed(r))
        for x in range(0,lines,1):
            userlist.insert(tkinter.END,rev[x])
    def directlist():
        userlist.delete(0,1000)
        filename = 'data/samplelist.txt'
        with open(filename) as fobj:
            for line in fobj:
                userlist.insert(tkinter.END,line)

    gScreen = tkinter.Tk()
    gScreen.title("InMedical-Gestion de personal")
    gScreen.geometry("600x500")
    uppertxt = tkinter.Label(gScreen,text="InMedical",justify="center",bg="lightblue",font="40")
    uppertxt.pack(fill=tkinter.X)
    altabtn = tkinter.Button(gScreen,text="Alta personal",justify="center",bg="lightblue",font="20",command=altaScreen)
    altabtn.place(x=200,y=50,width=200,height=58)
    bajabtn = tkinter.Button(gScreen,text="Baja personal",justify="center",bg="lightblue",font="20",command=bajaScreen)
    bajabtn.place(x=200,y=125,width=200,height=58)
    showuserlbl = tkinter.Label(gScreen,text="Listado de personal:",justify="center",font="20")
    showuserlbl.place(x=200,y=190)
    userlist = tkinter.Listbox(gScreen)
    # # MOSTRAR EMPLEADOS EN LA LISTA # #
    filename = 'data/samplelist.txt'
    with open(filename) as fobj:
        for line in fobj:
            userlist.insert(tkinter.END,line)
    # # SISTEMA DE SORTEO DE EMPLEADOS # # 
    userlist.place(x=200,y=210,width=200)
    greatbtn = tkinter.Button(gScreen,text="Mayor-menor",justify="center",font="10",command=directlist)
    greatbtn.place(x=80,y=220)
    sortbtn = tkinter.Button(gScreen,text="Menor-mayor",justify="center",font="10",command=inverselist)
    sortbtn.place(x=80,y=265)
    backbtn = tkinter.Button(gScreen,text="Regresar",justify="center",font="20",bg="lightblue",command=backProcess)
    backbtn.place(x=200,y=400,width=200,height=58)
    gScreen.mainloop()

def busquedaScreen():
    def endProcess():
        text = tkinter.Label(bScreen)
        text.pack()
        text.after(500)
        bScreen.destroy()
        mainScreen()

    def openFiles(name):
        def endLocalProcess():
            text = tkinter.Label(ofScreen)
            text.pack()
            text.after(500)
            ofScreen.destroy()
            busquedaScreen()
        text = tkinter.Label(bScreen)
        text.pack()
        text.after(500)
        bScreen.destroy()
        ofScreen = tkinter.Tk()
        ofScreen.title("InMedical - Perfiles")
        ofScreen.geometry("600x500")
        uppertxt = tkinter.Label(ofScreen,text="InMedical",justify="center",font="40",bg="lightblue",state="normal")
        uppertxt.pack(fill=tkinter.X)
        backbtn = tkinter.Button(ofScreen,text="Regresar",justify="center",font="20",bg="lightblue",command=endLocalProcess)
        backbtn.place(x=200,y=400,width=200,height=58)
        info = tkinter.Listbox(ofScreen)
        print(name)
        filename = 'data/employees/'+name
        with open(filename) as fobj:
            for line in fobj:
                info.insert(tkinter.END,line)
        info.place(x=50,y=75,width=500,height=250)
        ##lol
        ofScreen.mainloop()

    def addFiles(x):
        openbtn = tkinter.Button(bScreen,text="Abrir perfil",justify="center",font="20",bg="lightblue",command= lambda:openFiles(x))
        openbtn.place(x=350,y=400,height=25,width=100)
        
    def choosefactor():
        n = askedvalue.get()
        name = n + ".txt"
        directory = 'data/employees'
        for filename in os.listdir(directory): 
            if filename == name:
                print(f"concidencia encontrada con: {filename} y {name}")
                namelist.insert(tkinter.END,n)
                addFiles(name)

    bScreen = tkinter.Tk()
    bScreen.title("InMedical - Busqueda de personal")
    bScreen.geometry("600x500")
    uppertxt = tkinter.Label(bScreen,text="InMedical",justify="center",font="40",bg="lightblue",state="normal")
    uppertxt.pack(fill=tkinter.X)
    titlefilter = tkinter.Label(bScreen,text="Busque un empleado:",justify="center",font=30,bg="lightblue",state="normal")
    titlefilter.place(x=25,y=50,width=200,height=50)
    titlelist = tkinter.Label(bScreen,text="Coincidencias:",justify="center",font="30",bg="Lightblue",state="normal")
    titlelist.place(x=300,y=50,width=200,height=50)
    backbtn = tkinter.Button(bScreen,text="Regresar",justify="center",font="20",bg="lightblue",command=endProcess)
    backbtn.place(x=25,y=400,width=200,height=58)
    namelist = tkinter.Listbox(bScreen)
    namelist.place(x=300,y=125,height=250,width=200)
    askedvalue = tkinter.Entry(bScreen,font="20")
    askedvalue.place(x=50,y=125,height=25,width=150)
    valbtn = tkinter.Button(bScreen,text="Buscar",font="20",justify="center",command=choosefactor)
    valbtn.place(x=75,y=160,height=25,width=100)
    bScreen.mainloop()
loginScreen()
#incio loop


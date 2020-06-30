class Persona:
    def __init__(self):
        self.nombre = []
        self.apellido = []
        self.telefono = []
        self.carnet = []

class Usuario(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.email = []
        self.password = []
      
    def registrarUsuario(self):
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        carnet = input("Carnet de Identidad: ")
        email = input("Email: ")
        password = input("Password: ")

        self.guardarUsuario(nombre, apellido, telefono, carnet, email, password)
    
    def guardarUsuario(self, nombre, apellido, telefono, carnet, email, password):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.telefono.append(telefono)
        self.carnet.append(carnet)
        self.email.append(email)
        self.password.append(password)

    def modificarUsuario(self, posicion):
        opcion = """
            **************MODIFICACION DEL USUARIO**************
            1.- Nombre
            2.- Apellido
            3.- Telefono
            4.- Carnet
            5.- Email
            6.- Password
            """
        print(opcion)
        
        nombreNuevo = self.nombre[posicion]
        apellidoNuevo = self.apellido[posicion]
        telefonoNuevo = self.telefono[posicion]
        carnetNuevo = self.carnet[posicion]
        emailNuevo = self.email[posicion]
        passwordNuevo = self.password[posicion]

        opcion = int(input("Elija el Numero de la Opcion Que quiere modificar: "))

        if (opcion == 1):
            nombreNuevo = input("Nuevo Nombre: ")
        elif (opcion == 2):
            apellidoNuevo = input("Nuevo Apellido: ")
        elif (opcion == 3):
            telefonoNuevo = input("Nuevo Telefono: ")
        elif (opcion == 4):
            carnetNuevo = input("Nuevo CI: ")
        elif (opcion == 5):
            emailNuevo = input("Nuevo Email: ")
        elif (opcion == 6):
            passwordNuevo = input("Nuevo Password: ")
        else:
            print("Elija un numero de opcion correcto..!!")
            self.modificarUsuario(posicion)        
        
        self.nombre[posicion] = nombreNuevo
        self.apellido[posicion] = apellidoNuevo
        self.telefono[posicion] = telefonoNuevo
        self.carnet[posicion] = carnetNuevo
        self.email[posicion] = emailNuevo
        self.password[posicion] = passwordNuevo

        print ("Datos Actualizados Correctamente")

class TipoVehiculo:
    def __init__(self):
        self.tipoVehiculo = []

class Marca:
    def __init__(self):
        self.marca = []
        self.procedencia = []

class Vehiculo(TipoVehiculo, Marca):
    def __init__(self):
        TipoVehiculo.__init__(self)
        Marca.__init__(self)
        self.placa = []
        self.cilindrada = []
    
    def registrarVehiculo(self):
        tipoVehiculo = input("Tipo de Vehiculo: ")
        marca = input("Marca del Vehiculo: ")
        procedencia = input("Procedencia: ")
        placa = input("Placa del Vehiculo: ")
        cilindrada = input("Cilindrada: ")

        self.guardarVehiculo(tipoVehiculo, marca, procedencia, placa, cilindrada)
    
    def guardarVehiculo(self, tipoVehiculo, marca, procedencia, placa, cilindrada):
        self.tipoVehiculo.append(tipoVehiculo)
        self.marca.append(marca)
        self.procedencia.append(procedencia)
        self.placa.append(placa)
        self.cilindrada.append(cilindrada)
    
    def modificarVehiculo(self, posicion):
        opcion = """
            **************MODIFICACION DEL VEHICULO**************
            1.- Tipo Vehiculo
            2.- Marca
            3.- Procedencia
            4.- Placa
            5.- Cilindrada
            """
        print(opcion)
        
        tipoVehiculoNuevo = self.tipoVehiculo[posicion]
        marcaNuevo = self.marca[posicion]
        procedenciaNuevo = self.procedencia[posicion]
        placaNuevo = self.placa[posicion]
        cilindradaNuevo = self.cilindrada[posicion]

        opcion = int(input("Elija el Numero de la Opcion Que quiere modificar: "))

        if (opcion == 1):
            tipoVehiculoNuevo = input("Nuevo Tipo de Vehiculo: ")
        elif (opcion == 2):
            marcaNuevo = input("Nueva Marca: ")
        elif (opcion == 3):
            procedenciaNuevo = input("Nueva Procedencia: ")
        elif (opcion == 4):
            placaNuevo = input("Nueva Placa: ")
        elif (opcion == 5):
            cilindradaNuevo = input("Nueva Cilindrada: ")
        else:
            print("Elija un numero de opcion correcto..!!")
            self.modificarVehiculo(posicion)        
        
        self.tipoVehiculo[posicion] = tipoVehiculoNuevo
        self.marca[posicion] = marcaNuevo
        self.procedencia[posicion] = procedenciaNuevo
        self.placa[posicion] = placaNuevo
        self.cilindrada[posicion] = cilindradaNuevo

        print ("Datos Actualizados Correctamente")

class Conductor(Usuario, Vehiculo):
    def __init__(self):
        Usuario.__init__(self)
        Vehiculo.__init__(self)
        self.tipo_licencia = []
        self.vehiculo = []
        self.estado = []
    
    def menu(self):
        print("""
            ************** ****** ***** MENU ***** ****** **************
            1.- REGISTRAR CONDUCTORES
            2.- MOSTRAR CONDUCTORES REGISTRADOS HABILITADOS
            3.- MOSTRAR CONDUCTORES REGISTRADOS NO HABILITADOS
            4.- MODIFICAR DATOS DE CONDUCTOR
            5.- SALIR
        """)

        opcion = int(input("Elija una opcion del Menu: "))

        if opcion == 1:
            self.registrar()
        elif opcion == 2:
            self.listarHabilitados()
            self.volverMenu()
        elif opcion == 3:
            self.listarNoHabilitados()
            self.volverMenu()
        elif opcion == 4:
            self.modificarMenu()
            self.volverMenu()
        elif opcion == 5:
            print("GRACIAS POR UTILIZAR NUESTRO SERVICIO... :)")
        else:
            print("Elija una opcion correcta del Menu..!!")        

    def volverMenu(self):
        opcion = input("Desea volver al MENU? S/N: ")

        if opcion == "S" or opcion == "s":
            self.menu()
        elif opcion == "N" or opcion == "n":
            print("GRACIAS POR UTILIZAR NUESTRO SERVICIO... :)")
        else:
            print("Elija una opcion correcta S/N..!!")
            self.volverMenu()

    def registrar(self):
        print("******COMPLETE LOS DATOS DEL FORMULARIO DE REGISTRO******")
        self.registrarUsuario()
        self.registrarVehiculo()
        tipo_licencia = input("Tipo de Licencia: ")
        vehiculo = input("Vehiculo: ")
        estado = input("Habilitado Si/No: ") 
        
        self.guardarConductor(tipo_licencia, vehiculo, estado)

        print("Usuario Registrado Correctamente..!!")

        self.registrarOtro()
        pass
 
    def guardarConductor(self, tipo_licencia, vehiculo, estado):
        self.tipo_licencia.append(tipo_licencia)
        self.vehiculo.append(vehiculo)
        self.estado.append(estado)

    def registrarOtro(self):
        opcion = input("Desea Registrar otro Usuario? S/N: ")

        if opcion == "S" or opcion == "s":
            self.registrar()
        elif opcion == "N" or opcion == "n":
            self.menu()
        else:
            print("Elija una opcion correcta S/N..!!")
            self.registrarOtro()          

    def mostrar(self, posicion):
        print("********************{} {}********************".format(self.nombre[posicion], self.apellido[posicion]))
        print("Cel. {} - C.I. {}".format(self.telefono[posicion], self.carnet[posicion]))
        print("Email: {} - Password: {}".format(self.email[posicion], self.password[posicion]))
        print("Vehiculo: {}".format(self.vehiculo[posicion]))
        print("Tipo: {} - Marca: {}".format(self.tipoVehiculo[posicion], self.marca[posicion]))
        print("Procedencia: {} - Placa: {}".format(self.procedencia[posicion], self.placa[posicion]))
        print("Cilindrada: {}cc - Tipo de Licencia: {}".format(self.cilindrada[posicion], self.tipo_licencia[posicion]))        
        print("Habilitado Si/No: {}".format(self.estado[posicion]))
        pass

    def listar(self, estado):
        if self.nombre:    
            for posicion in range(len(self.nombre)):
                if self.estado[posicion] == estado or self.estado[posicion] == estado.upper() or self.estado[posicion] == estado.lower():
                    self.mostrar(posicion)
        else:
            return print("No hay Usuarios Registrados en el Sistema..!!")

    def listarHabilitados(self):
        estado = "Si"
        self.listar(estado)
        self.volverMenu()

    def listarNoHabilitados(self):
        estado = "No"
        self.listar(estado)
        self.volverMenu()

    def modificarMenu(self):
        carnetConductor = input("Ingrese el CI del Conductor: ")
        posicion = self.carnet.index(carnetConductor)
        self.mostrar(posicion)

        opcion = """
            **************OPCIONES A MODIFICAR**************
            1.- USUARIO
                (Nombre, Apellido, Telefono, Carnet, Email, Password)

            2.- VEHICULO
                (Tipo Vehiculo, Marca, Procedencia, Placa, Cilindrada)

            3.- CONDUCTOR
                (Tipo de Licencia, Vehiculo, Estado)
            """
        print(opcion)

        opcion = int(input("Elija el Numero de la Opcion a Modificar: "))

        if (opcion == 1):
            self.modificarUsuario(posicion)
            self.modificarOtro()
        elif (opcion == 2):
            self.modificarVehiculo(posicion)
            self.modificarOtro()
        elif (opcion == 3):
            self.modificarConductor(posicion)
            self.modificarOtro()
        else:
            print("Elija un numero de opcion correcto..!!")
            self.modificarMenu()

    def modificarOtro(self):
        opcion = input("Desea Modificar otro Usuario? S/N: ")

        if opcion == "S" or opcion == "s":
            self.modificarMenu()
        elif opcion == "N" or opcion == "n":
            self.menu()
        else:
            print("Elija una opcion correcta S/N..!!")
            self.modificarOtro()    

    def modificarConductor(self, posicion):
        opcion = """
            **************MODIFICACION DEL CONDUCTOR**************
            1.- Tipo de Licencia
            2.- Vehiculo
            3.- Estado
            """
        print(opcion)
        
        tipoLicenciaNuevo = self.tipo_licencia[posicion]
        vehiculoNuevo = self.vehiculo[posicion]
        estadoNuevo = self.estado[posicion]

        opcion = int(input("Elija el Numero de la Opcion Que quiere modificar: "))

        if (opcion == 1):
            tipoLicenciaNuevo = input("Nuevo Tipo de Licencia: ")
        elif (opcion == 2):
            vehiculoNuevo = input("Nuevo Vehiculo: ")
        elif (opcion == 3):
            estadoNuevo = input("Nuevo Estado: ")
        else:
            print("Elija un numero de opcion correcto..!!")
            self.modificarUsuario(posicion)        
        
        self.tipo_licencia[posicion] = tipoLicenciaNuevo
        self.vehiculo[posicion] = vehiculoNuevo
        self.estado[posicion] = estadoNuevo

        print ("Datos Actualizados Correctamente")

conductor = Conductor()

conductor.guardarUsuario("Alejandro", "Gonzales","78138077","11325913","alejandrog280211@gmail.com","**********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "AXN-678", "125")
conductor.guardarConductor("M", "Motocicleta", "Si")

conductor.guardarUsuario("Alejandro", "Gonzales","78138077","11325913","alejandrog280211@gmail.com","**********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "AXN-678", "125") 
conductor.guardarConductor("M", "Motocicleta", "Si")

conductor.guardarUsuario("Vanessa", "Florez","76645292","8989990","vanessaf1@gmail.com","**********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "VAN-678", "150")
conductor.guardarConductor("M", "Motocicleta", "Si")

conductor.guardarUsuario("Jose", "Mercado","73256984","5659854","josemercado@gmail.com","**********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "VAN-678", "150")
conductor.guardarConductor("M", "Motocicleta", "Si")

conductor.guardarUsuario("Maria", "Cuellar","7598654","4654879","mariacuellar@gmail.com","**********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "VAN-678", "150")
conductor.guardarConductor("M", "Motocicleta", "Si")

conductor.guardarUsuario("Marco", "Peredo","75421563","3216546","marcoperedo@gmail.com","*********")
conductor.guardarVehiculo("Motocicleta","Honda", "Japon", "VAN-678", "150")
conductor.guardarConductor("M", "Motocicleta", "Si")


conductor.menu()
print("Bienvenido al programa")
#Crear datos
#Humanos (países y gentilicios), Animales (especie y tipo)
#Cada dato debe ser almacenado de manera individual
#Definición datos humanos: países y gentilicios
paGen1 = "Francia, francés"       #paGen1 es de tipo str
paGen2 = "Argentina, argentino"   #paGen2 es de tipo str
paGen3 = "Croacia, croata"        #paGen3 es de tipo str
paGen4 = "Italia, italiano"       #paGen4 es de tipo str
paGen5 = "Brasil, brasileño"      #paGen5 es de tipo str
paGen6 = "México, mexicano"       #paGen6 es de tipo str
paGen7 = "España, español"        #paGen7 es de tipo str
paGen8 = "Marruecos, marroquí"    #paGen8 es de tipo str
paGen9 = "Colombia, colombiano"   #paGen9 es de tipo str
paGen10 = "Alemania, alemán"      #paGen10 es de tipo str

#Definición datos animales: especie y tipo
anim1 = "Perro, Caninos"            #anim1 es de tipo str
anim2 = "Mosquito, Insectos"        #anim2 es de tipo str
anim3 = "Lince, Felinos"            #anim3 es de tipo str
anim4 = "Caimán, Reptiles"          #anim4 es de tipo str
anim5 = "Rana, Anfibios"            #anim5 es de tipo str
anim6 = "Lobo, Caninos"             #anim6 es de tipo str
anim7 = "Araña, Insectos"           #anim7 es de tipo str
anim8 = "Puma, Felinos"             #anim8 es de tipo str
anim9 = "Cocodrilo, Reptiles"       #anim9 es de tipo str
anim10 = "Salamandra, Anfibios"     #anim10 es de tipo str

#Captura de datos desde el teclado
#Pedir nombre al usuario
nombreUs = input("\nIngrese su nombre: ")
#País o especie según la opción en la que se encuentre
#Se creará un menú de opciones
#Las opciones son: Humanos y Animales
opción1 = input('''
              \tMenú de opciones:
              A- Humanos
              B- Animales
              
              Seleccione una opción del menú: ''').upper()

#Si la opción escogida es 'A', mostrar las opciones de países para conocer su gentilicio
if opción1 == "A":
    opción2 = input('''
                  \tOpciones de países:
                  1- FRANCIA
                  2- ARGENTINA
                  3- CROACIA
                  4- ITALIA
                  5- BRASIL
                  6- MÉXICO
                  7- ESPAÑA
                  8- MARRUECOS
                  9- COLOMBIA
                  10- ALEMANIA
                  
                  Ingrese una de las opciones mostradas: ''')
    
    #Comparar los datos almacenados con los datos ingresados por el usuario
    if opción2 == '1':
        print ("\n"f"{nombreUs} usted es de Francia, su gentilicio es 'francés'")

    elif opción2 == '2':
        print ("\n"f"{nombreUs} usted es de Argentina, su gentilicio es 'argentino'")
    
    elif opción2 == '3':
        print ("\n"f"{nombreUs} usted es de Croacia, su gentilicio es 'croata'")
    
    elif opción2 == '4':
        print ("\n"f"{nombreUs} usted es de Italia, su gentilicio es 'italiano'")
        
    elif opción2 == '5':
        print ("\n"f"{nombreUs} usted es de Brasil, su gentilicio es 'brasileño'")

    elif opción2 == '6':
        print ("\n"f"{nombreUs} usted es de México, su gentilicio es 'mexicano'")

    elif opción2 == '7':
        print ("\n"f"{nombreUs} usted es de España, su gentilicio es 'español'")

    elif opción2 == '8':
        print ("\n"f"{nombreUs} usted es de Marruecos, su gentilicio es 'marroquí'")
 
    elif opción2 == '9':
        print ("\n"f"{nombreUs} usted es de Colombia, su gentilicio es 'colombiano'")

    elif opción2 == '10':
        print ("\n"f"{nombreUs} usted es de Alemania, su gentilicio es 'alemán'")

    else:
        print("\nLa opción ingresada no está disponible")
        
#Si la opción escogida es 'B', mostrar las opciones de especies para conocer los tipos de animales
elif opción1 == "B":
    opción2 = input('''
                    \tOpciones de especies:
                    A- CANINA
                    B- INSECTOS
                    C- FELINOS
                    D- REPTILES
                    E- ANFIBIOS
                    
                    Ingrese una de las opciones mostradas: ''').upper()
    
    #Comparar los datos almacenados con los datos ingresados por el usuario
    if opción2 == 'A':
        print("\n"f"{nombreUs} usted ha escogido la especie 'Canina' los animales que se encuentran en dicha especie son: Perro y Lobo")
        
    elif opción2 == 'B':
        print("\n"f"{nombreUs} usted ha escogido la especie 'Insectos' los animales que se encuentran en dicha especie son: Mosquito y Araña")
        
    elif opción2 == 'C':
        print("\n"f"{nombreUs} usted ha escogido la especie 'Felinos' los animales que se encuentran en dicha especie son: Lince y Puma")
    
    elif opción2 == 'D':
        print("\n"f"{nombreUs} usted ha escogido la especie 'Reptiles' los animales que se encuentran en dicha especie son: Caimán y Cocodrilo")
        
    elif opción2 == 'E':
        print("\n"f"{nombreUs} usted ha escogido la especie 'Anfibios' los animales que se encuentran en dicha especie son: Rana y Salamandra")
        
    else:
        print("\nLa opción ingresada no está disponible")

#Si el usuario no escoge ninguna de las opciones disponibles (A o B), mostrar un mensaje indicando que la opción no está disponible
else:
    print("\nLa opción ingresada no se encuentra disponible")
    
print("\nFIN DEL PROGRAMA")

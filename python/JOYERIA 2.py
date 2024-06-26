#Productos personal
import os
os.system("cls")

folio = 10000

#           ID     Producto       Marca      Modelo Unidad Stock Precio  
productos = [
    ["A001", "anillos", "talla 4", 100, 1000],
    ["A002", "anillos", "talla 5", 90, 2000],
    ["A003", "anillos", "talla 6", 120, 2500],
    ["B001", "anillos", "talla 7", 40, 3200],
    ["B002", "anillos", "talla 8", 30, 4500],
    ["B003", "cadena", "40 cm", 50, 2000],
    ["C001", "cadena", "42 cm", 25, 5000],
    ["C002", "pulsera", "15 cm", 30, 1000],
    ["D001", "pulsera", "16 cm", 25, 2000],
    ["D002", "pulseras", "17 cm", 25, 6000],
]

ventas = [
    [100, "12-06-2024", "A001"],
    [90, "12-06-2024", "A002"],
    [120, "12-06-2024", "A003"],
    [40, "12-06-2024", "B001"],
    [30, "12-06-2024", "B002"],
    [50, "12-06-2024", "B003"],
    [25, "12-06-2024", "C001"],
    [30, "12-06-2024", "C002"],
    [25, "12-06-2024", "D001"],
    [25, "12-06-2024", "D002"],
]
# Función para agregar un nuevo producto
def agregar_producto():
    print("AGREGAR PRODUCTO")
    try:
        id = input("Ingrese la id: ")
        Producto = input("Ingrese el producto: ")
        Marca = input("Ingresar marca: ")
        Modelo = input("Ingrese el modelo: ")
        Unidad = int(input("Ingresar unidades: "))
        Stock = int(input("Ingresar el stock: "))
        Precio = int(input("Ingresar precio: "))
        
        productos.append([id, Producto, Marca, Modelo, Unidad, Stock, Precio])
        print("Producto agregado correctamente.")
    except ValueError:
        print("Error: Por favor, asegúrese de ingresar un número válido para unidades, stock y precio.")

# Función para buscar un producto por su id
def buscar_producto():
    print("BUSCAR PRODUCTO")
    try:
        id_buscar = input("Ingrese la id del producto a buscar: ")
        encontrado = False
        for producto in productos:
            if producto[0] == id_buscar:
                print_producto(producto)
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, asegúrese de ingresar una id válida para buscar.")

# Función para eliminar un producto por su id
def eliminar_producto():
    print("ELIMINAR PRODUCTO")
    try:
        id_eliminar = input("Ingrese la id del producto a eliminar: ")
        encontrado = False
        for producto in productos:
            if producto[0] == id_eliminar:
                productos.remove(producto)
                print("Producto eliminado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, asegúrese de ingresar una id válida para eliminar.")

# Función para modificar un producto por su id
def modificar_producto():
    print("MODIFICAR PRODUCTO")
    try:
        id_modificar = input("Ingrese la id del producto a modificar: ")
        encontrado = False
        for producto in productos:
            if producto[0] == id_modificar:
                print_producto(producto)
                print("Ingrese los nuevos datos:")
                producto[1] = input("Ingrese el nombre del producto: ")
                producto[2] = input("Ingrese la marca: ")
                producto[3] = input("Ingrese el modelo: ")
                producto[4] = int(input("Ingrese las unidades: "))
                producto[5] = int(input("Ingrese el stock: "))
                producto[6] = float(input("Ingrese el precio: "))
                print("Producto modificado correctamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    except ValueError:
        print("Error: Por favor, asegúrese de ingresar valores numéricos válidos para unidades, stock y precio")

# Función para listar todos los productos
def listar_productos():
    print("LISTA DE PRODUCTOS")
    for producto in productos:
        print_producto(producto)
        print()

# Función para imprimir un producto
def print_producto(producto):
    print(f"ID: {producto[0]}, Producto: {producto[1]}, Marca: {producto[2]}, Modelo: {producto[3]}, Unidades: {producto[4]}, Stock: {producto[5]}, Precio: {producto[6]}")

# Función principal
def main():
    opcion = 0
    while opcion != 3:
         
        print("""
              MENÚ DE JOYAS
              ----------------------------------
              1. Reportes de ventas
              2. Mantenedor de productos
              3. Salir
              """)
        try:
            opcion = int(input("Ingrese una opción 1-3: "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido")

def total_ventas():
    total = sum(venta[0] for venta in ventas)
    print(f"Total de ventas: {total}")

def ventas_por_fecha(fecha):
    total_fecha = sum(venta[0] for venta in ventas if venta[1] == fecha)
    print(f"Total de ventas para la fecha {fecha}: {total_fecha}")

def ventas_rango_fechas(fecha_inicio, fecha_fin):
    total_rango = sum(venta[0] for venta in ventas if fecha_inicio <= venta[1] <= fecha_fin)
    print(f"Total de ventas para el rango de fechas {fecha_inicio} - {fecha_fin}: {total_rango}")

opcion = 0
while opcion <= 4:
    os.system("cls")
    print("""
          REPORTES
          ----------------------------------
          1. General de ventas (con total)
          2. Ventas por fecha especifica (con total)
          3. Ventas por rango de fecha (con total)
          4. Salir al menu principal 
          """)

    opcion = int(input("Ingrese una opción 1-4: "))

    if opcion == 1:
        total_ventas()

    elif opcion == 2:
        fecha = input("Ingrese la fecha en formato dd-mm-aaaa: ")
        ventas_por_fecha(fecha)

    elif opcion == 3:
        fecha_inicio = input("Ingrese la fecha de inicio en formato dd-mm-aaaa: ")
        fecha_fin = input("Ingrese la fecha de fin en formato dd-mm-aaaa: ")
        ventas_rango_fechas(fecha_inicio,fecha_fin)

    elif opcion == 4:
        print("Volviendo al menú principal...")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 4.")

    input("\nPresione Enter para continuar...") 

    os.system("cls")
    op=0
    while op<=6:
                print("""
                        Mantenedor de productos
                      ---------------------------------
                      1. Agregar
                      2. Buscar
                      3. Eliminar
                      4. Modificar
                      5. Listar
                      6. Salir al menú principal
                      
                      """)
                op=int(input("Ingrese una opcion 1-6 "))
                
                match op:
                    case 1:
                        print("\nAgregar\n")
                        id = input("Ingrese la id:  ")
                        Producto=input("Ingrese el producto:  ")
                        Marca=input("Ingresar marca:  ")
                        Modelo=input("Ingrese el modelo:  ")
                        Unidad=int(input("Ingresar unidades:  "))
                        Stock=int(input("Ingresar el stock:  "))
                        Precio=int(input("Ingresar precio:  "))
                                
                        productos.append([id, Producto, Marca, Modelo, Unidad, Stock, Precio])

                    case 2:
                        print("Buscar con funcion")
                        id=input("Ingrese la id del producto al buscar:  ")
                        lista= (id)
                        if lista != -1:
                            print(lista)
                        else:
                            print("Error, id no existe")

                        
                    case 3:
                        id = int(input("Ingrese id producto a eliminar:  "))

                        i = 0
                        sw = 0 
                        while i <= (len(productos) - 1):
                            if productos[i][0] == id:
                                sw = 1  
                                productos.pop(i) 
                                break 
                            else:
                                    i += 1 
                        if sw == 0: print("id no existe...")


                    case 4: 
                        print("\n Modificar\n")
                        
                        id=int(input("Ingrese id producto a modificar: "))

                        i = 0
                        sw = 0 
                        while i <= (len(productos) - 1):
                                if productos[i][0] == id:
                                    sw = 1  
                                    print("id encontrado en el indice ", i)
                                    print(productos[i])
                                    id = input("Ingrese el id del producto: ")
                                    Producto = input("Ingrese nombre del producto:  ")
                                    Marca = input("Ingrese la marca:  ")
                                    Modelo = input("Ingrese el modelo:  ")
                                    Unidad = int(input("Ingrese la unidad:  "))
                                    Stock = int(input("Ingrese el stock:  "))
                                    Precio = int(input("Ingrese el precio:  "))
                                    
                                    productos[i][0] = id
                                    productos[i][1] = Producto
                                    productos[i][2] = Marca
                                    productos[i][3] = Modelo
                                    productos[i][4] = Unidad
                                    productos[i][5] = Stock
                                    productos[i][6] = Precio
                                    print("\n Listo! datos modificados")
                                    break 
                                else:
                                    i += 1 
                                if sw == 0: print("id no existe...")

                    case 5:
                        print("Enter para continuar")
                        os.system("pause")
                        sw=0
                        for a in  productos:
                            if a[0] == id:
                                sw=1
                            print ("ID    Producto         Marca     Modelo    Unidad    Stock     Precio")  
                            print (a[0],"  ",a[1],"  ",a[2],"  ",a[3],"   ",a[4],"  ",a[5],"       ",a[6])
                
print("Fin del menú")       
def leer_opcion():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

def elegir_opcion():
    try:
        opcion = int(input("Eliga una opcion: "))
        return 1 <= opcion <= 6
    except ValueError:
        return -1
    
def validar_codigo(cod_f):
    return len(cod_f.strip()) > 0

def validar_nombre(nom_f):
    return len(nom_f.strip()) > 0
def validar_categoria(catg_f):
    return len(catg_f.strip()) > 0
def validar_marca(marc_f):
    return len(marc_f.strip()) > 0
def validar_peso_kg(peso_f):
    try:
        valor = float(peso_f)
        return valor > 0
    except ValueError:
        return False
def validar_importado(imp_f):
    try:
        imp = imp_f.strip().lower()
        return imp
    except ValueError:
        return False
def validar_para_cachorro(chr_f):
    try:
        chr = chr_f.strip().lower()
        return chr
    except ValueError:
        return False
def validar_precio(prc_f):
    try:
        valor = int(prc_f)
        return valor > 0
    except ValueError:
        return False
def validar_unidades(und_f):
    try:
        valor = int(und_f)
        return valor >= 0
    except ValueError:
        return False

def agregar_producto(lista_productos,lista_stock):
    codigo = input("Ingrese el codigo del producto")
    nombre = input("Ingrese Nombre del producto")
    categoria = input("Ingrese la categoria del producto")
    marca = input("Ingrese la marca del producto")
    peso_kg = input("Ingrese el peso del producto")
    es_importado = input("¿el producto es importadp?(s/n)")
    es_para_cachorro = input("¿el producto es para cachorros?(s/n)")
    precio = input("Ingrese el precio del producto")
    unidades = input("Ingrese la cantidad de unidades del producto")
    if not validar_codigo(codigo):
        print("[ERROR]: El codigo no puede estar vacío o existente ya en los diccionarios")
    
    if not validar_nombre(nombre):
        print("[ERROR]:El nombre no puede estar vacío o con espacios en blanco")
        return
    if not validar_categoria(categoria):
        print("[ERROR]:La categoria no puede estar vacía o con espacios en blanco")
        return
    if not validar_marca(marca):
        print("[ERROR]:La marca no puede estar vacía o con espacios en blanco")
        return    
    if not validar_peso_kg(peso_kg):
        print("[ERROR]: EL peso debe ser un número mayor que cero")
        return
    if not validar_importado(es_importado):
        print("[ERROR]:Ingresa solo 's' o 'n'")
        return
    if not validar_para_cachorro(es_para_cachorro):
        print("[ERROR]:Ingresa solo 's' o 'n'")
        return
    if not validar_precio(precio):
        print("[ERROR]:El precio debe serun numero mayor a cero sin decimales")
        return
    if not validar_unidades(unidades):
        print("[ERROR]:Las unidades deben ser un numero mayor o igual a cero")
        return
    
    nuevo_producto = {codigo : [nombre, categoria,marca,peso_kg,es_importado,es_para_cachorro]}
    nuevo_stock = {codigo : [precio,unidades]}

    lista_productos.append(nuevo_producto)
    lista_stock.append(nuevo_stock)
    print("El Producto fue correctamente Ingresado en productos y stock")

def unidades_categoria(categoria,lista_productos,lista_stock):
    for i in range(len(lista_productos)):
        if lista_productos[i][2].lower() == categoria.strip().lower():
            print("")
        


def buscar_codigo(codigo):
    print("")

def actualizar_precio(codigo, nuevo_precio):
    print("")
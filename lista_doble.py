# Lista doblemente enlazada sin clases
# Cada nodo es un diccionario con referencias anterior y siguiente.

cabeza = None
cola = None


def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo


def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" " if actual["siguiente"] else "\n")
        actual = actual["siguiente"]


def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" " if actual["anterior"] else "\n")
        actual = actual["anterior"]


def agregar_inicio(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = nuevo
        cola = nuevo
    else:
        nuevo["siguiente"] = cabeza
        cabeza["anterior"] = nuevo
        cabeza = nuevo


def eliminar(dato):
    global cabeza, cola
    actual = cabeza

    while actual is not None and actual["dato"] != dato:
        actual = actual["siguiente"]

    if actual is None:
        return False

    anterior = actual["anterior"]
    siguiente = actual["siguiente"]

    if anterior is None:
        cabeza = siguiente
    else:
        anterior["siguiente"] = siguiente

    if siguiente is None:
        cola = anterior
    else:
        siguiente["anterior"] = anterior

    return True


# Reflexión: Lo más difícil fue mantener sincronizados los enlaces "anterior"
# y "siguiente", especialmente al modificar el primer o el último nodo.
# Para evitar enlaces rotos, actualicé las referencias de ambos nodos vecinos
# y, cuando correspondía, también "cabeza" o "cola". Comprobé la lista
# recorriéndola hacia adelante y hacia atrás.


if __name__ == "__main__":
    # Paso 1
    cabeza = None
    cola = None
    agregar_final("Inicio")
    agregar_final("Catálogo")
    agregar_final("Contacto")
    print("Paso 1 - adelante:")
    mostrar_adelante()

    # Paso 2
    print("Paso 2 - adelante y atrás:")
    mostrar_adelante()
    mostrar_atras()

    # Paso 3
    print("Paso 3 - agregar al inicio:")
    agregar_inicio("Bienvenida")
    mostrar_adelante()
    mostrar_atras()

    # Paso 4
    print("Paso 4 - eliminar por valor:")
    print("Eliminado:", eliminar("Catálogo"))
    mostrar_adelante()
    mostrar_atras()

    # Casos especiales
    print("Casos especiales:")
    cabeza = None
    cola = None
    print("Eliminar de lista vacía:", eliminar("x"))
    agregar_final("A")
    print("Eliminar único nodo:", eliminar("A"))
    print("Lista vacía después de eliminar único nodo:", cabeza, cola)

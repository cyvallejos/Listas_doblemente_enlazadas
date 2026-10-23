# Reto 2: Insertar después de un valor
# Lista doblemente enlazada sin clases.

cabeza = None
cola = None


def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}


def agregar_final(dato):
    global cabeza, cola
    nuevo = crear_nodo(dato)

    if cabeza is None:
        cabeza = cola = nuevo
    else:
        nuevo["anterior"] = cola
        cola["siguiente"] = nuevo
        cola = nuevo


def insertar_despues(referencia, dato):
    global cabeza, cola
    actual = cabeza

    while actual is not None and actual["dato"] != referencia:
        actual = actual["siguiente"]

    if actual is None:
        return False

    nuevo = crear_nodo(dato)
    siguiente = actual["siguiente"]
    nuevo["anterior"] = actual
    nuevo["siguiente"] = siguiente
    actual["siguiente"] = nuevo

    if siguiente is None:
        cola = nuevo
    else:
        siguiente["anterior"] = nuevo

    return True


def mostrar_adelante():
    actual = cabeza
    while actual is not None:
        print(actual["dato"], end=" -> " if actual["siguiente"] is not None else "\n")
        actual = actual["siguiente"]


def mostrar_atras():
    actual = cola
    while actual is not None:
        print(actual["dato"], end=" <- " if actual["anterior"] is not None else "\n")
        actual = actual["anterior"]


if __name__ == "__main__":
    print("Lista vacía:")
    print("insertar_despues('A', 'X') ->", insertar_despues("A", "X"))

    agregar_final("A")
    print("\nUn solo nodo:")
    print("insertar_despues('A', 'B') ->", insertar_despues("A", "B"))
    mostrar_adelante()
    mostrar_atras()

    agregar_final("C")
    print("\nVarios nodos:")
    print("insertar_despues('A', 'X') ->", insertar_despues("A", "X"))
    print("insertar_despues('Z', 'Y') ->", insertar_despues("Z", "Y"))
    mostrar_adelante()
    mostrar_atras()

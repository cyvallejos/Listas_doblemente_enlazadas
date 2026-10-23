# Reto 1: Buscador bidireccional
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


def buscar(dato):
    desde_cabeza = cabeza
    desde_cola = cola

    while desde_cabeza is not None and desde_cola is not None:
        if desde_cabeza["dato"] == dato or desde_cola["dato"] == dato:
            return True

        if desde_cabeza is desde_cola:
            break

        desde_cabeza = desde_cabeza["siguiente"]
        desde_cola = desde_cola["anterior"]

    return False


if __name__ == "__main__":
    print("Lista vacía:")
    print("buscar('A') ->", buscar("A"))

    agregar_final("A")
    print("\nUn solo nodo:")
    print("buscar('A') ->", buscar("A"))
    print("buscar('Z') ->", buscar("Z"))

    agregar_final("B")
    agregar_final("C")
    agregar_final("D")
    print("\nVarios nodos:")
    print("buscar('A') ->", buscar("A"))
    print("buscar('C') ->", buscar("C"))
    print("buscar('D') ->", buscar("D"))
    print("buscar('Z') ->", buscar("Z"))

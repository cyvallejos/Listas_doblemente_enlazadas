# Reto 3: Historial del navegador
# Usa una lista doblemente enlazada sin clases.

cabeza = None
cola = None
actual = None


def crear_nodo(pagina):
    return {"pagina": pagina, "anterior": None, "siguiente": None}


def visitar(pagina):
    global cabeza, cola, actual
    nuevo = crear_nodo(pagina)

    if actual is None:
        cabeza = nuevo
        cola = nuevo
    else:
        # Elimina el historial futuro antes de crear una nueva rama.
        futuro = actual["siguiente"]
        actual["siguiente"] = None
        while futuro is not None:
            siguiente = futuro["siguiente"]
            futuro["anterior"] = None
            futuro["siguiente"] = None
            futuro = siguiente
        cola = actual
        nuevo["anterior"] = actual
        actual["siguiente"] = nuevo
        cola = nuevo

    actual = nuevo


def retroceder():
    global actual
    if actual is not None and actual["anterior"] is not None:
        actual = actual["anterior"]
        return True
    return False


def avanzar():
    global actual
    if actual is not None and actual["siguiente"] is not None:
        actual = actual["siguiente"]
        return True
    return False


def mostrar_pagina_actual():
    if actual is None:
        print("No hay una página en el historial.")
    else:
        print("Página actual:", actual["pagina"])


def mostrar_historial():
    pagina = cabeza
    paginas = []
    while pagina is not None:
        etiqueta = f"[{pagina['pagina']}]" if pagina is actual else pagina["pagina"]
        paginas.append(etiqueta)
        pagina = pagina["siguiente"]

    if paginas:
        print("Historial:", " <-> ".join(paginas))
    else:
        print("El historial está vacío.")


def menu():
    while True:
        print("\n--- Historial del navegador ---")
        print("1. Visitar página")
        print("2. Retroceder")
        print("3. Avanzar")
        print("4. Mostrar página actual")
        print("5. Mostrar historial")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            pagina = input("Nombre o dirección de la página: ").strip()
            if pagina:
                visitar(pagina)
                mostrar_pagina_actual()
            else:
                print("La página no puede estar vacía.")
        elif opcion == "2":
            if not retroceder():
                print("No hay una página anterior.")
            mostrar_pagina_actual()
        elif opcion == "3":
            if not avanzar():
                print("No hay una página siguiente.")
            mostrar_pagina_actual()
        elif opcion == "4":
            mostrar_pagina_actual()
        elif opcion == "5":
            mostrar_historial()
        elif opcion == "0":
            print("Fin del historial.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()

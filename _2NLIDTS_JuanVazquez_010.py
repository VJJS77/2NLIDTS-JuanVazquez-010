class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
def imprimir_lista(cabeza):
    actual = cabeza
    while actual is not None:
        print(
            f"Dato: {actual.dato} "
            f"| Direccion: {hex(id(actual))} "
            f"| Anterior: {hex(id(actual.anterior)) if actual.anterior else '0'} "
            f"| Siguiente: {hex(id(actual.siguiente)) if actual.siguiente else '0'}"
        )
        actual = actual.siguiente
    print()
def imprimir_lista_reversa(cola):
    actual = cola
    while actual is not None:
        print(
            f"Dato: {actual.dato} "
            f"| Direccion: {hex(id(actual))} "
            f"| Anterior: {hex(id(actual.anterior)) if actual.anterior else '0'} "
            f"| Siguiente: {hex(id(actual.siguiente)) if actual.siguiente else '0'}"
        )
        actual = actual.anterior
    print()
def borrar_lista(cabeza, cola):
    contador = 0
    actual = cabeza
    while actual is not None:
        siguiente = actual.siguiente
        contador += 1
        print(f"Elemento borrado {contador} | Dato: {actual.dato} | Direccion: {hex(id(actual))}")
        actual = siguiente
    print(f"Total de elementos borrados: {contador}")
    return None, None
def agregar_nodo(cabeza, cola, valor):
    nuevo_nodo = Nodo(valor)
    if cabeza is None:
        cabeza = nuevo_nodo
        cola = nuevo_nodo
    else:
        cola.siguiente = nuevo_nodo
        nuevo_nodo.anterior = cola
        cola = nuevo_nodo
    return cabeza, cola
def main():
    print("Actividad 08 - Lista Doblemente Enlazada\n")
    cabeza = None
    cola = None
    try:
        tamanolista = int(input("Ingrese la cantidad de elementos de la lista enlazada: "))
    except ValueError:
        print("Cantidad de elementos no valida")
        return
    if tamanolista <= 0:
        print("Cantidad de elementos no valida")
        return
    for i in range(tamanolista):
        valor = int(input(f"Ingrese el dato {i + 1}: "))
        cabeza, cola = agregar_nodo(cabeza, cola, valor)
    print("\nImprimiendo lista (de inicio a fin):")
    imprimir_lista(cabeza)
    print("Imprimiendo lista (de fin a inicio):")
    imprimir_lista_reversa(cola)
    print("\nBorrando lista de numeros")
    cabeza, cola = borrar_lista(cabeza, cola)
if __name__ == "__main__":
    main()
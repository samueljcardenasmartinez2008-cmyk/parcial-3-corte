import random


def generar_lista(n=10):
    """Crea una lista aleatoria de n elementos entre 1 y 100."""
    return [random.randint(1, 100) for _ in range(n)]


def leer_lista():
    """Lee una lista desde el teclado (equivalente a Scanner en Java)."""
    while True:
        texto = input("Ingresa los números separados por espacios: ").strip()
        try:
            lista = [int(x) for x in texto.split()]
            if len(lista) < 2:
                print("Ingresa al menos 2 números.")
                continue
            return lista
        except ValueError:
            print("Solo se permiten números enteros. Intenta de nuevo.")


def ordenar_burbuja(lista):
    """Ordena con Burbuja. Devuelve (lista_ordenada, iteraciones)."""
    datos = lista.copy()
    iteraciones = 0
    n = len(datos)

    for i in range(n - 1):
        hubo_intercambio = False
        for j in range(n - 1 - i):
            iteraciones += 1
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
                hubo_intercambio = True
        if not hubo_intercambio:
            break

    return datos, iteraciones


def ordenar_seleccion(lista):
    """Ordena con Selección. Devuelve (lista_ordenada, iteraciones)."""
    datos = lista.copy()
    iteraciones = 0
    n = len(datos)

    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            iteraciones += 1
            if datos[j] < datos[indice_minimo]:
                indice_minimo = j
        datos[i], datos[indice_minimo] = datos[indice_minimo], datos[i]

    return datos, iteraciones


def comparar(lista):
    """Ejecuta ambos métodos y dice cuál usó menos iteraciones."""
    _, iter_burbuja = ordenar_burbuja(lista)
    _, iter_seleccion = ordenar_seleccion(lista)

    print("\n--- Comparación ---")
    print(f"Burbuja:   {iter_burbuja} iteraciones")
    print(f"Selección: {iter_seleccion} iteraciones")

    if iter_burbuja < iter_seleccion:
        print("Burbuja usó menos iteraciones.")
    elif iter_seleccion < iter_burbuja:
        print("Selección usó menos iteraciones.")
    else:
        print("Ambos usaron la misma cantidad de iteraciones.")


def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Generar lista aleatoria de 10 elementos")
    print("2. Ingresar lista manualmente (teclado)")
    print("3. Ordenar con Burbuja")
    print("4. Ordenar con Selección")
    print("5. Comparar ambos algoritmos")
    print("6. Salir")


def main():
    lista = generar_lista()
    print("Lista original:", lista)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            lista = generar_lista()
            print("Nueva lista:", lista)
        elif opcion == "2":
            lista = leer_lista()
            print("Lista ingresada:", lista)
        elif opcion == "3":
            ordenada, iteraciones = ordenar_burbuja(lista)
            print("Original: ", lista)
            print("Ordenada: ", ordenada)
            print("Iteraciones (Burbuja):", iteraciones)
        elif opcion == "4":
            ordenada, iteraciones = ordenar_seleccion(lista)
            print("Original: ", lista)
            print("Ordenada: ", ordenada)
            print("Iteraciones (Selección):", iteraciones)
        elif opcion == "5":
            print("Lista:", lista)
            comparar(lista)
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()

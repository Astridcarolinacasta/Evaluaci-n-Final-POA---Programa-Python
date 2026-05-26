print("Información del estudiante")
print("Astrid Carolina Castañeda Rincon")
print("Grupo: 213022_236")
print("Programa: Ingeniería de sistemas")
print("Código Fuente: Autoría propia\n")

def cantidad_a_pedir(stock_actual: int, stock_minimo: int) -> int:
    
    #Retorna la cantidad exacta a pedir según la lógica de negocio:
    # Si stock_actual < stock_minimo: pedir (stock_minimo - stock_actual)
    # En caso contrario: pedir 0
    
    return max(0, stock_minimo - stock_actual)


def main() -> None:
    # Matriz (inventario): [Código, Nombre, Stock Actual, Stock Mínimo Requerido]
    inventario = [
        ["A001", "Arroz", 10, 15],
        ["A002", "Frijol", 25, 20],
        ["A003", "Aceite", 3, 10],
        ["A004", "Azúcar", 18, 18],
        ["A005", "Café", 7, 12],
    ]

    #Solicitar el nombre y cantidad por articulo
    pedidos = []
    for codigo, nombre, stock_actual, stock_minimo in inventario:
        pedir = cantidad_a_pedir(int(stock_actual), int(stock_minimo))
        if pedir > 0:
            pedidos.append((nombre, pedir))

    print("LISTA DE PEDIDOS (Reabastecimiento)")

    #Si no hay articulos que reabastecer
    if not pedidos:
        print("No hay artículos por reabastecer.")
        return

    #Imprimir de una manera mas ordenada
    for nombre, cantidad in pedidos:
        print(f"{nombre:<10} {cantidad}")

if __name__ == "__main__":
    main()



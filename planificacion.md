# Planificación del proyecto

## Características del sistema

## Algoritmo

## Clases a utilizar

### Maquina:

  - Atributos:
    - inventario: Instancia de la clase inventario
    - selección: Código del producto que le pidieron
    - charola: Guarda el producto que entrega
    - dinero: Guarda el producto que entrega
    - historial: Lista de productos en el inventario

    - password: Guarda el producto que entrega

  - Métodos:
    - recibirPago: Explicación
    - darCambio: Explicación
    - darProducto: Explicación
    - imprimirTicket: Explicación
    - guardarEnHistorial: Explicación

    - acceder: Explicación
    - cambiarContra: Explicación
    - desatascar

### Inventario:

  - Atributos:
    - tamano: cantidad de objetos en el inventario
    - catalogo: Lista de productos en el inventario
    - historial: Lista de productos en el inventario

  - Métodos:
    - agregarProductos: Lee un archivo csv y guarda los productos
    - listarProductos
    - buscarProducto
    - buscarCantidadProductos: Ver cuántos productos hay de un tipo
    - guardarEnHistorial: Explicación

### Producto:

  - Atributos:
    - nombre: Explicación
    - precio: Explicación
    - codigo: Explicación
    - marca: Explicación
    - fechaCaducidad: Explicación

  - Métodos:
    - cambiarCódigo: Explicación
    - cambiarPrecio: Explicación

### Bebida (hereda de Producto)

  - Atributos:
    - volumen: Explicación

  - Métodos:

### Botana (hereda de Producto)

  - Atributos:
    - peso: Explicación

  - Métodos:

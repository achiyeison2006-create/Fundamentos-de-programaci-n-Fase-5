
# Curso: Fundamentos de Programación
# Estudiante: Yeison Yovanny Achicanoy Rodríguez
# Problema 2: Gestión de Precios de Menú de Restaurante

def calcular_precio_final(producto, categoria_objetivo, umbral_precio):
    """
    Módulo (función) para calcular el precio final de un producto.
    Aplica 15% de descuento si cumple la categoría y supera el umbral.
    """
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Lógica de negocio: Verificar condiciones para el descuento
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        # Se mantiene el precio base si no cumple las condiciones
        precio_final = precio_base
        
    return precio_final


def main():
    # REQ-01: Matriz con 6 productos [Nombre, Categoría, Precio Base]
    menu = [
        ["Hamburguesa Premium", "Plato Fuerte", 25000],
        ["Papas Supremas", "Entradas", 12000],
        ["Filete de Mero", "Plato Fuerte", 32000],
        ["Jugo Natural", "Bebidas", 6000],
        ["Limonada Cerezada", "Bebidas", 8500],
        ["Tres Leches", "Postres", 11000]
    ]
    
    # REQ-02: Definición de variables para la promoción (Categoría objetivo y Umbral)
    # Ejemplo: Aplicar descuento a "Plato Fuerte" que cuesten más de 20,000 pesos
    categoria_promo = "Plato Fuerte"
    umbral_promo = 20000
    
    print("=" * 65)
    print(f"   SISTEMA DE GESTIÓN DE MENÚ - APLICANDO PROMOCIÓN")
    print(f"   Categoría Objetivo: {categoria_promo} | Umbral: ${umbral_promo:,}")
    print("=" * 65)
    print(f"{'Producto':<25} | {'Categoría':<15} | {'P. Base':<10} | {'P. Final':<10}")
    print("-" * 65)
    
    # Procesar la matriz y mostrar resultados (REQ-03 y REQ-04)
    for producto in menu:
        precio_base = producto[2]
        # Llamada al módulo de cálculo
        precio_final = calcular_precio_final(producto, categoria_promo, umbral_promo)
        
        # Formatear la salida para que sea clara y ordenada
        print(f"{producto[0]:<25} | {producto[1]:<15} | ${precio_base:<8,} | ${precio_final:<8,.0f}")
        
    print("=" * 65)


if __name__ == "__main__":
    main()

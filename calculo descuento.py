def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando un porcentaje al monto total de la compra.

    Parámetros:
    - monto_total (float): El monto total de la compra.
    - porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar.
      Por defecto, es del 10%.

    Retorna:
    - float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Compras de diferentes productos
monto_viveres = 200  # Monto total de compra de viveres en dólares
descuento_viveres = calcular_descuento(monto_viveres)  # Descuento aplicado al monto total de compra de viveres
monto_final_viveres = monto_viveres - descuento_viveres  # Monto final a pagar por los viveres después del descuento

monto_ropa = 150  # Monto total de compra de ropa en dólares
porcentaje_descuento_ropa = 20  # Porcentaje de descuento para la compra de ropa
descuento_ropa = calcular_descuento(monto_ropa, porcentaje_descuento_ropa)  # Descuento aplicado al monto total de compra de ropa
monto_final_ropa = monto_ropa - descuento_ropa  # Monto final a pagar por la ropa después del descuento

monto_zapatos = 100  # Monto total de compra de zapatos en dólares
descuento_zapatos = calcular_descuento(monto_zapatos)  # Descuento aplicado al monto total de compra de zapatos
monto_final_zapatos = monto_zapatos - descuento_zapatos  # Monto final a pagar por los zapatos después del descuento

monto_utiles_escolares = 50  # Monto total de compra de útiles escolares en dólares
descuento_utiles_escolares = calcular_descuento(monto_utiles_escolares)  # Descuento aplicado al monto total de compra de útiles escolares
monto_final_utiles_escolares = monto_utiles_escolares - descuento_utiles_escolares  # Monto final a pagar por los útiles escolares después del descuento

monto_limpieza = 80  # Monto total de compra de artículos de limpieza en dólares
descuento_limpieza = calcular_descuento(monto_limpieza)  # Descuento aplicado al monto total de compra de artículos de limpieza
monto_final_limpieza = monto_limpieza - descuento_limpieza  # Monto final a pagar por los artículos de limpieza después del descuento

monto_higiene_personal = 120  # Monto total de compra de elementos de higiene personal en dólares
descuento_higiene_personal = calcular_descuento(monto_higiene_personal)  # Descuento aplicado al monto total de compra de elementos de higiene personal
monto_final_higiene_personal = monto_higiene_personal - descuento_higiene_personal  # Monto final a pagar por los elementos de higiene personal después del descuento

# Mostrar los resultados
print(f"Descuento para la compra de viveres: ${descuento_viveres}, Monto final a pagar: ${monto_final_viveres}")
print(f"Descuento para la compra de ropa: ${descuento_ropa}, Monto final a pagar: ${monto_final_ropa}")
print(f"Descuento para la compra de zapatos: ${descuento_zapatos}, Monto final a pagar: ${monto_final_zapatos}")
print(f"Descuento para la compra de útiles escolares: ${descuento_utiles_escolares}, Monto final a pagar: ${monto_final_utiles_escolares}")
print(f"Descuento para la compra de artículos de limpieza: ${descuento_limpieza}, Monto final a pagar: ${monto_final_limpieza}")
print(f"Descuento para la compra de elementos de higiene personal: ${descuento_higiene_personal}, Monto final a pagar: ${monto_final_higiene_personal}")


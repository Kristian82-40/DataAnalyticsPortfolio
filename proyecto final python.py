import pandas as pd


df = pd.read_csv('/Users/juliafenton/Desktop/Kris/kris_data_analitycs/proyecto_final_python.ipynb/datos_ventas_centros_comerciales (1).csv')
# # ejercicio 1
# es el total de ingresos generados por todas las ventas registradas
total_ingresos = df['price'].sum()
print("El total de ingresos generados es:", total_ingresos)


# # ejercicio 2
# te da el shopping que mas a vendido
centro_comercial_mas_ventas = df['shopping_mall'].max()
precio_maximo = df['price'].max()
print("El shopping que mas a vendido es:", centro_comercial_mas_ventas,"El precio máximo es:",precio_maximo)

# # ejercicio 3
# sacamos la categoria mas vendida
ventas_por_categoria = df.groupby("category")["price"].sum()
categoria_mas_vendida = ventas_por_categoria.idxmax()
print("La categoria mas vendida es:",categoria_mas_vendida)

# # ejercicio 4
# Encontrar el índice del producto con el precio máximo
indice_producto_mas_caro = df['price'].idxmax()
# Obtener el nombre del producto más caro
producto_mas_caro = df.loc[indice_producto_mas_caro, 'category']
print("El producto más caro es:", producto_mas_caro)

# # ejercicio 5
#factura_mas_antigua 
factura_mas_antigua = df.sort_values(by='invoice_date')
df.iloc[[6479]]

# # ejercicio 6
# cantidad promedio de productos vendidos por transacción
cantidad_promedio_por_transaccion = df.loc[:,["quantity"]].mean()
print("La cantidad promedio por transaccion es:",cantidad_promedio_por_transaccion)

# # ejercicio 7
# agrupo y saco los valores para ventas registradas
dia_con_mas_ventas = df.groupby('invoice_date')['price'].sum()
dia_con_mas_ventas = dia_con_mas_ventas.idxmax()
print("El dia con mas ventas fue el:",dia_con_mas_ventas)

# # ejercicio 8
# aqui sacamos el cliente que mas gasto
cliente_que_mas_gasto = df.groupby('customer_id')['price'].sum()
cliente_que_mas_gasto = cliente_que_mas_gasto.idxmax()
print("El Cliente que mas a gastado fue el:",cliente_que_mas_gasto)

# # ejercicio 9
# aqui agrupo las columnas y cogo el mas alto
factura_max_valor = df.groupby('invoice_no')['price'].sum()
factura_max_valor = factura_max_valor.idxmax()
print("La factura con el precio total mas alto fue:",factura_max_valor)

# # ejercicio 10
# Calcular el porcentaje de ventas por categoría
distribucion_porcentual_ventas_por_categoria = ventas_por_categoria / ventas_por_categoria.sum() * 100
ventas_por_categoria = df.groupby('category')[['price']].sum()
distribucion_porcentual_ventas_por_categoria

# # ejercicio 11
# ventas_por_categoria = df.groupby('category')['price'].sum()
dia_semana_mas_ventas_por_centro = df.groupby('invoice_date')[['shopping_mall','price']].max()
dia_semana_mas_ventas_por_centro
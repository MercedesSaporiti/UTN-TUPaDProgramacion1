
import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear carpeta resultados si no existe
os.makedirs("resultados", exist_ok=True)

# Leer dataset
df = pd.read_csv("datos/ventas.csv")

# Calcular total de cada venta
df["total_venta"] = df["cantidad"] * df["precio"]

# Ventas totales
ventas_totales = df["total_venta"].sum()

# Producto más vendido
producto_mas_vendido = (
    df.groupby("producto")["cantidad"]
    .sum()
    .idxmax()
)

# Ventas por mes
df["fecha"] = pd.to_datetime(df["fecha"])

ventas_por_mes = (
    df.groupby(df["fecha"].dt.to_period("M"))["total_venta"]
    .sum()
)

# Guardar resumen
with open("resultados/resumen.txt", "w") as archivo:
    archivo.write(f"Ventas totales: ${ventas_totales}\n")
    archivo.write(f"Producto más vendido: {producto_mas_vendido}\n")
    archivo.write("\nVentas por mes:\n")
    archivo.write(str(ventas_por_mes))

# Crear gráfico
ventas_por_mes.plot(kind="bar")

plt.title("Ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")

plt.tight_layout()

plt.savefig("resultados/grafico_ventas.png")

print("Análisis finalizado correctamente")

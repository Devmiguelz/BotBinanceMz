import time
from binance.client import Client
from config import API_KEY, API_SECRET

# Configuración de la API de Binance
api_key = API_KEY
api_secret = API_SECRET
par = 'BTCBUSD'
client = Client(api_key, api_secret)

# Configuración del grid bot
cantidad_inicial = 1.0  # Cantidad inicial de activos para operar
grid_size = 0.01  # Tamaño de cada cuadrícula
spread = 0.005  # Porcentaje de spread para cada lado de la cuadrícula

# Función para obtener el precio actual de un par de trading
def obtener_precio(par):
    return float(client.get_symbol_ticker(symbol=par)['price'])

# Función para colocar una orden de compra en el grid
def realizar_compra(par, cantidad, precio):
    print(f"Realizando una compra: {cantidad} {par} a {precio}")
    # Aquí debes implementar la llamada a la API de Binance para colocar la orden de compra

# Función para colocar una orden de venta en el grid
def realizar_venta(par, cantidad, precio):
    print(f"Realizando una venta: {cantidad} {par} a {precio}")
    # Aquí debes implementar la llamada a la API de Binance para colocar la orden de venta

# Loop principal del grid bot
while True:
    # Obtener el precio actual del par de trading
    precio_actual = obtener_precio(par)

    # Calcular el precio de la cuadrícula superior e inferior
    precio_superior = precio_actual * (1 + spread)
    precio_inferior = precio_actual * (1 - spread)

    # Calcular la cantidad de cuadrículas a comprar y vender
    cuadriculas_comprar = int(cantidad_inicial / precio_inferior / grid_size)
    cuadriculas_vender = int(cantidad_inicial / precio_superior / grid_size)

    # Realizar las operaciones de compra
    for i in range(cuadriculas_comprar):
        precio_compra = precio_inferior * (1 - grid_size) ** i
        realizar_compra('BTCUSDT', grid_size, precio_compra)

    # Realizar las operaciones de venta
    for i in range(cuadriculas_vender):
        precio_venta = precio_superior * (1 + grid_size) ** i
        realizar_venta('BTCUSDT', grid_size, precio_venta)

    # Esperar un tiempo antes de volver a ejecutar el ciclo
    time.sleep(60)  # Esperar 1 minuto

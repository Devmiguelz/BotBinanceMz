import time
from binance import Client
from config import API_KEY, API_SECRET

class Binance:
    def __init__(self, public_key = '', secret_key = '', sync = False):
        self.time_offset = 0
        self.b = Client(public_key, secret_key)

        if sync:
            self.time_offset = self._get_time_offset()

    def _get_time_offset(self):
        res = self.b.get_server_time()
        return res['serverTime'] - int(time.time() * 1000)

    def synced(self, fn_name, **args):
        args['timestamp'] = int(time.time() - self.time_offset)
        return getattr(self.b, fn_name)(**args)


public_key = API_KEY
secret_key = API_SECRET

binance = Binance(public_key = public_key, secret_key = secret_key , sync=True)
account_info = binance.synced('get_account')

# Encuentra el balance del activo específico que deseas obtener
asset = 'BUSC'  # Cambia 'BTC' por el símbolo del activo que deseas obtener

for balance in account_info['balances']:
    if balance['asset'] == asset:
        available_balance = float(balance['free'])
        print(f"La cantidad disponible de {asset} es: {available_balance}")
        break
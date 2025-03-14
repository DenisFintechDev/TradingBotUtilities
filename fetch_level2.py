from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time

class IBKRClient(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def tickPrice(self, reqId, tickType, price, attrib):
        print(f"Tick Price: {price}")

def main():
    app = IBKRClient()
    app.connect("127.0.0.1", 7497, 123)  # Подключись к TWS или IB Gateway
    threading.Thread(target=app.run).start()
    time.sleep(1)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"

    app.reqMktData(1, contract, "", False, False, [])
    time.sleep(3)
    app.disconnect()

if __name__ == "__main__":
    main()

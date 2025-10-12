from ib_insync import *
import time
import logging

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(
    filename='ib_gateway_bot.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# -----------------------------
# Connect to IB Gateway
# -----------------------------
ib = IB()

while True:
    try:
        if not ib.isConnected():
            ib.connect('127.0.0.1', 7497, clientId=1)  # 7497 = Paper Gateway
            logging.info("✅ Connected to IB Gateway")

        # -----------------------------
        # Define contract & order
        # -----------------------------
        stock = Stock('AAPL', 'SMART', 'USD')
        ib.qualifyContracts(stock)  # ensures the contract is valid

        order = MarketOrder('BUY', 1)

        # -----------------------------
        # Place order
        # -----------------------------
        trade = ib.placeOrder(stock, order)
        ib.sleep(2)  # brief pause to ensure transmission

        msg = f"✅ Placed BUY order for 1 AAPL at {ib.reqCurrentTime()}"
        print(msg)
        logging.info(msg)

        # -----------------------------
        # Wait for 5 minutes
        # -----------------------------
        time.sleep(5 * 60)

    except Exception as e:
        err = f"❌ Error: {e}"
        print(err)
        logging.error(err)
        time.sleep(60)

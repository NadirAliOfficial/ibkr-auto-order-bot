
# 💹 IBKR Python Trading Bot

A simple automated trading bot built using **Python** and **IB Gateway** via the `ib_insync` library.  
The bot connects to your Interactive Brokers Paper Account and places a sample **market order every 5 minutes**.

---

## ⚙️ Features
- Connects automatically to **IB Gateway**
- Places sample **BUY orders** every few minutes
- Reconnects automatically if disconnected
- Logs all activity in `ib_gateway_bot.log`
- Safe exception handling and clean shutdown

---

## 🧩 Requirements

**1. Install Dependencies**
```bash
pip install ib_insync
````

**2. Install IB Gateway**

* Download: [https://www.interactivebrokers.com/en/trading/ibgateway-stable.php](https://www.interactivebrokers.com/en/trading/ibgateway-stable.php)
* Log in to **Paper Trading** account
* Enable API Access:

  * ⚙️ `Configure → API → Settings`
  * ✅ Enable ActiveX and Socket Clients
  * 🔢 Port: `7497`
  * 💻 Trusted IPs: `127.0.0.1`

---

## 🚀 How to Run

1. Start **IB Gateway (Paper)**
2. Run the bot:

   ```bash
   python ib_gateway_bot.py
   ```
3. The bot will:

   * Connect to your gateway
   * Place a **BUY 1 AAPL** order every 5 minutes
   * Save all logs to `ib_gateway_bot.log`

---

## 📜 Log Example

```
2025-10-12 10:15:03 [INFO] ✅ Connected to IB Gateway
2025-10-12 10:15:05 [INFO] ✅ Placed BUY order for 1 AAPL at 2025-10-12 10:15:05
```

---

## 🧠 Code Overview

### `ib_gateway_bot.py`

| Section          | Description                              |
| ---------------- | ---------------------------------------- |
| Logging Setup    | Saves logs to file                       |
| Connection Logic | Connects or reconnects to IB Gateway     |
| Order Execution  | Places market order (BUY 1 AAPL)         |
| Error Handling   | Logs and retries if any exception occurs |

---

## 📈 Future Enhancements

Students can extend this project by adding:

* 🔁 Alternate between BUY and SELL
* 💰 Trade only if AAPL < certain price
* 📊 Save all trades to a CSV
* 🧮 Add simple moving average logic
* 📢 Send Telegram alerts on each trade

---

## 🧾 Author

**Nadir Ali Khan**
Founder & Instructor — *Team NAK / Al-Mehdi Foundation*
📍 Sukkur, Pakistan
<!-- updated: 2025-03-15-r01 -->

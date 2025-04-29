# 📈 Real-Time Market Price Alert App

  A Python-based tool that fetches real-time market (stocks,crypto) data and 
  triggers alerts when prices break your defined upper/lower thresholds.

---

## 🚀 Features

- 📉 Real-time price tracking with custom upper and lower thresholds
- 🔔 Terminal Alerts when a threshold is breached
- 📊 Interactive candlestick charts using mplfinance
- 🕒 Automatically fetches price every 10 seconds using `schedule`
- 💡 Designed to be extendable (GUI coming soon!)

---
## ⚙️ Tech Stack

- Python 🐍
- Pandas, NumPy
- yFinance 📈
- mplfinance 🕹️
- schedule ⏰
- Matplotlib 📊

---

## 🎥 Demo Video

[![Watch the demo](https://img.youtube.com/vi/MiWyNGftaPs/0.jpg)](https://www.youtube.com/watch?v=MiWyNGftaPs)

---

## 📌 How to Use

1. Clone this repo:
    ```bash
    git clone https://github.com/YuvBhatt-YB/market-price-tracker.git
    cd market-price-tracker
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python tracker.py
    ```

4. Customize thresholds and add the assets (stock or crypto) you want to monitor in `config` dictionary inside the script:
    ```python
    config = {
        "symbol-name-1": {"upper": 85700, "lower": 85600},
        "symbol-name-2": {"upper": 1627, "lower": 1630}
    }
    ```

---
## 🔮 Future Improvements

- Full GUI using Tkinter or web interface using Flask + React
- Email or Telegram alerts
- Add more assets
- Logging and export to CSV
- Responsive dashboard

---
## 🙋‍♂️ Author

Made with 💙 by Yuv Bhatt (https://github.com/YuvBhatt-YB)

## 📌 License

This project is for educational and portfolio purposes only.

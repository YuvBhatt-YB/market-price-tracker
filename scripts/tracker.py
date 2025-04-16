import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import mplfinance as mpl
import schedule
import time
import numpy as np

# ---------- CONFIG ----------

config ={
    "BTC-USD":{"upper":83500,"lower":83100},
    "ETH-USD":{"upper":1620,"lower":1580}
}

#Market Data

market_data = {}

#Whether the alert is triggered or not

alert_triggered = {f"{x}":False for x in config.keys()}

#---------- FETCH STOCK DATA ----------

def fetch_stock_data(config):
    for k,v in config.items():
        symbol = yf.Ticker(k)
        data = symbol.history(period="2d", interval="15m")
        market_data[k] = data


#---------- DISPLAY CHART ----------

def display_chart(k):
    mc = mpl.make_marketcolors(up='#d0D4dc', down='#678797',
                               edge='#5c606b',
                               wick={'up': '#022f31', 'down': '#022f31'},
                               volume='in',
                               ohlc='black')
    style = mpl.make_mpf_style(marketcolors=mc,base_mpf_style='classic',rc={
    'figure.figsize': (16, 9),
    'axes.titleweight': 'bold',
    'axes.titlesize': 22,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
})
    upper = config[k]["upper"]
    lower = config[k]["lower"]

    add_plots = [
        mpl.make_addplot(np.full(len(market_data[k]), upper), color='#4DAA57', linestyle='--', width=2),
        mpl.make_addplot(np.full(len(market_data[k]), lower), color='#C1292E', linestyle='--', width=2),
    ]

    width = dict(candle_linewidth=0.7, candle_width=0.6, volume_width=0.5)
    mpl.plot(market_data[k], type='candle', title=k, volume=True,style=style,figratio=(18,10),ylabel="Price",
             ylabel_lower="Volume",volume_panel=1,panel_ratios=(5,1.2),figscale=1.5,update_width_config=width,addplot=add_plots)
    plt.show()

#---------- CHECK FOR THRESHOLDS ----------

def check_threshold():
    for k,v in market_data.items():
        latest_price = v.iloc[-1]
        close_price = latest_price["Close"]
        high_price = latest_price["High"]
        low_price = latest_price["Low"]

        if close_price > config[k]["upper"] and not alert_triggered[k]:
            print(f"{k} broke your upper threshold of {config[k]["upper"]},\nCurrent High : ${high_price},\nCurrent Low : ${low_price},\nCurrent Close: ${close_price}")
            display_chart(k)
            alert_triggered[k] = True
        elif close_price < config[k]["lower"] and not alert_triggered[k]:
            print(f"{k} broke your lower threshold of {config[k]["lower"]},\nCurrent High : ${high_price},\nCurrent Low : ${low_price},\nCurrent Close: ${close_price}")
            display_chart(k)
            alert_triggered[k] = True

        if config[k]["lower"] <=close_price <= config[k]["upper"]:
            alert_triggered[k] = False


def main():
    pd.set_option('display.float_format', '{:.2f}'.format)
    schedule.every(10).seconds.do(lambda: fetch_stock_data(config))
    schedule.every(10).seconds.do(check_threshold)
    while True:
        schedule.run_pending()
        time.sleep(1)


while __name__ == "__main__":
    main()



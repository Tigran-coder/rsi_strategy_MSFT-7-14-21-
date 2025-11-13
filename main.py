import pandas as pd
import vectorbt as vbt
import pandas_ta as ta



df = pd.read_csv("MSFT_1hour.csv")
df['Positions'] = 0.0
df = df.set_index('Time')
df.index = pd.to_datetime(df.index)
df['RSI_7'] = ta.rsi(df['Close'], length=7)
df['RSI_14'] = ta.rsi(df['Close'], length=14)
df['RSI_21'] = ta.rsi(df['Close'], length=21)
entries_14 = df['RSI_14'] < 30
exits_14   = df['RSI_14'] > 70
exits_14
pf_14 = vbt.Portfolio.from_signals(
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    entries=entries_14,
    exits=exits_14,
    size=1,
    size_type="percent",
    fees=0.001,
    slippage=0.0002,
    init_cash=1000,
    freq="1h"
)
entries_7 = df['RSI_7'] < 30
exits_7   = df['RSI_7'] > 70
exits_7
pf_7 = vbt.Portfolio.from_signals(
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    entries=entries_7,
    exits=exits_7,
    size=1,
    size_type="percent",
    fees=0.001,
    slippage=0.0002,
    init_cash=1000,
    freq="1h"
)
entries_21 = df['RSI_21'] < 30
exits_21   = df['RSI_21'] > 70
exits_21
pf_21 = vbt.Portfolio.from_signals(
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    entries=entries_21,
    exits=exits_21,
    size=1,
    size_type="percent",
    fees=0.001,
    slippage=0.0002,
    init_cash=1000,
    freq="1h"
)
pf_14.stats()
pf_21.stats()
pf_7.stats()

print(pf_14.plot().show(renderer="browser"))    
print(pf_7.plot().show(renderer="browser"))
print(pf_21.plot().show(renderer="browser"))
import requests


class AdvancedMarketAnalyzer:
    PAIRS = {
        "EUR/USD": "EURUSD=X",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "JPY=X",
        "USD/CHF": "CHF=X",
        "AUD/USD": "AUDUSD=X",
        "USD/CAD": "CAD=X",
        "NZD/USD": "NZDUSD=X",
        "EUR/GBP": "EURGBP=X",
        "EUR/JPY": "EURJPY=X",
        "GBP/JPY": "GBPJPY=X",
        "EUR/CHF": "EURCHF=X",
        "AUD/JPY": "AUDJPY=X",
        "GBP/CHF": "GBPCHF=X",
        "AUD/CAD": "AUDCAD=X",
        "AUD/NZD": "AUDNZD=X",
        "CAD/JPY": "CADJPY=X",
        "CHF/JPY": "CHFJPY=X",
        "EUR/AUD": "EURAUD=X",
        "EUR/CAD": "EURCAD=X",
        "GBP/AUD": "GBPAUD=X",
        "GBP/CAD": "GBPCAD=X",
        "NZD/JPY": "NZDJPY=X",
        "NZD/CAD": "NZDCAD=X",
        "USD/SGD": "SGD=X",
        "USD/HKD": "HKD=X",
    }

    def __init__(self, pair="EUR/USD", data=None):
        self.pair = pair
        self.symbol = self.PAIRS.get(pair)
        if not self.symbol:
            raise ValueError(f"Unsupported pair: {pair}")
        self.data = data

    def _fetch_market_data(self):
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{self.symbol}"
        params = {"range": "1d", "interval": "1m"}
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        payload = response.json()

        result = payload["chart"]["result"][0]
        quote = result["indicators"]["quote"][0]
        closes = quote["close"]
        highs = quote["high"]
        lows = quote["low"]
        volumes = quote.get("volume") or [0] * len(closes)

        rows = []
        for i, close in enumerate(closes):
            if close is None:
                continue
            rows.append(
                {
                    "close": float(close),
                    "high": float(highs[i] if highs[i] is not None else close),
                    "low": float(lows[i] if lows[i] is not None else close),
                    "volume": float(volumes[i] or 0),
                }
            )

        if len(rows) < 30:
            raise RuntimeError("Not enough candle data received.")
        return rows

    @staticmethod
    def _ema(values, span):
        alpha = 2.0 / (span + 1.0)
        ema = values[0]
        result = [ema]
        for value in values[1:]:
            ema = alpha * value + (1 - alpha) * ema
            result.append(ema)
        return result

    @staticmethod
    def _rsi(values, period=14):
        if len(values) <= period:
            return 50.0
        gains, losses = [], []
        for i in range(1, len(values)):
            change = values[i] - values[i - 1]
            gains.append(max(change, 0))
            losses.append(max(-change, 0))
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        if avg_loss == 0:
            return 100.0 if avg_gain > 0 else 50.0
        rs = avg_gain / avg_loss
        return 100.0 - (100.0 / (1.0 + rs))

    @staticmethod
    def _vwap(rows):
        total_pv = 0.0
        total_volume = 0.0
        for row in rows:
            typical = (row["high"] + row["low"] + row["close"]) / 3.0
            volume = row["volume"]
            total_pv += typical * volume
            total_volume += volume
        if total_volume <= 0:
            return rows[-1]["close"]
        return total_pv / total_volume

    def evaluate_signal(self):
        rows = self.data if self.data is not None else self._fetch_market_data()
        closes = [r["close"] for r in rows]

        ema9 = self._ema(closes, 9)[-1]
        ema21 = self._ema(closes, 21)[-1]
        ema200 = self._ema(closes, 200)[-1]
        ema12 = self._ema(closes, 12)
        ema26 = self._ema(closes, 26)
        macd_series = [a - b for a, b in zip(ema12, ema26)]
        macd = macd_series[-1]
        macd_signal = self._ema(macd_series, 9)[-1]
        rsi = self._rsi(closes, 14)
        vwap = self._vwap(rows)
        last = closes[-1]

        bullish = 0
        bearish = 0

        if last > ema200:
            bullish += 25
        else:
            bearish += 25

        if rsi > 50 and macd > macd_signal:
            bullish += 25
        elif rsi < 50 and macd < macd_signal:
            bearish += 25

        if last > vwap:
            bullish += 25
        else:
            bearish += 25

        if ema9 > ema21:
            bullish += 25
        else:
            bearish += 25

        direction = "CALL" if bullish >= bearish else "PUT"
        confidence = float(max(bullish, bearish))

        return {
            "direction": direction,
            "confidence": round(confidence, 1),
            "rsi": round(rsi, 2),
            "macd": round(macd, 6),
            "ema_gap": round(ema9 - ema21, 6),
            "price_vs_vwap": round(last - vwap, 6),
            "price": round(last, 6),
            "explanation": (
                f"{self.pair} {last:.5f} | RSI {rsi:.1f} | "
                f"EMA9/21 {'bullish' if ema9 > ema21 else 'bearish'} | "
                f"MACD {'bullish' if macd > macd_signal else 'bearish'} | "
                f"VWAP {'above' if last > vwap else 'below'}"
            ),
        }

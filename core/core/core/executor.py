class TradeExecutor:
    def __init__(self, auto_trade_enabled=False):
        self.auto_trade_enabled = bool(auto_trade_enabled)

    def process_signal(self, asset, signal_data, amount, min_confidence):
        confidence = float(signal_data.get("confidence", 0))

        if confidence < float(min_confidence):
            return {
                "execution_mode": "SIGNAL_ONLY",
                "status": "SKIPPED",
                "message": (
                    f"{asset}: confidence {confidence:.1f}% is below "
                    f"the {float(min_confidence):.1f}% threshold."
                ),
            }

        return {
            "execution_mode": "SIGNAL_ONLY",
            "status": "SIGNAL_READY",
            "message": (
                f"{asset}: {signal_data.get('direction')} signal ready "
                f"at {confidence:.1f}% confidence."
            ),
        }

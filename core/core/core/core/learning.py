import json
import os


class LearningEngine:
    def __init__(self, history_path="storage/trade_history.json"):
        self.history_path = history_path
        self._ensure_storage()

    def _ensure_storage(self):
        folder = os.path.dirname(self.history_path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        if not os.path.exists(self.history_path):
            with open(self.history_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def record_prediction(self, features, prediction, win):
        with open(self.history_path, "r", encoding="utf-8") as f:
            history = json.load(f)
        history.append(
            {
                "features": features,
                "prediction": prediction,
                "outcome": int(bool(win)),
            }
        )
        with open(self.history_path, "w", encoding="utf-8") as f:
            json.dump(history[-500:], f, indent=2)

    def refine_confidence(self, base_confidence, features):
        try:
            with open(self.history_path, "r", encoding="utf-8") as f:
                history = json.load(f)
        except (OSError, ValueError):
            return round(float(base_confidence), 1)

        if len(history) < 20:
            return round(float(base_confidence), 1)

        wins = sum(int(item.get("outcome", 0)) for item in history)
        rate = wins / len(history) * 100.0

        adjusted = float(base_confidence) * 0.8 + rate * 0.2
        return round(max(0.0, min(100.0, adjusted)), 1)

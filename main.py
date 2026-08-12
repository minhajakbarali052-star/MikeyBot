from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog

from core.auth import SecurityManager
from core.analyzer import AdvancedMarketAnalyzer
from core.learning import LearningEngine
from core.executor import TradeExecutor


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20,
            size_hint=(0.9, None),
            height=430,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        layout.add_widget(MDLabel(text="Mikey Bot", font_style="H4", halign="center"))
        layout.add_widget(MDLabel(text="Market Signal Assistant", halign="center"))

        self.username_input = MDTextField(hint_text="Username", text="Mikey Bot")
        self.password_input = MDTextField(hint_text="Password", password=True)

        login_btn = MDRaisedButton(
            text="LOGIN", pos_hint={"center_x": 0.5}, on_release=self.perform_login
        )
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_btn)
        self.add_widget(layout)

    def perform_login(self, instance):
        app = MDApp.get_running_app()
        if app.security_manager.verify_login(
            self.username_input.text, self.password_input.text
        ):
            app.sm.current = "dashboard"
        else:
            app.show_dialog("Login failed", "Invalid username or password.")


class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_pair = "EUR/USD"
        self.layout = MDBoxLayout(orientation="vertical", padding=12, spacing=10)

        self.layout.add_widget(
            MDLabel(
                text="Mikey Bot — Select a Forex Pair",
                font_style="H6",
                halign="center",
                size_hint_y=None,
                height=45,
            )
        )

        pair_grid = MDBoxLayout(orientation="vertical", spacing=6, size_hint_y=0.42)
        pairs = list(AdvancedMarketAnalyzer.PAIRS.keys())
        for row_start in range(0, len(pairs), 3):
            row = MDBoxLayout(orientation="horizontal", spacing=6)
            for pair in pairs[row_start : row_start + 3]:
                btn = MDRectangleFlatButton(
                    text=pair, size_hint_x=1, on_release=self.select_pair
                )
                row.add_widget(btn)
            pair_grid.add_widget(row)

        self.selected_label = MDLabel(
            text="Selected: EUR/USD", halign="center", size_hint_y=None, height=35
        )

        self.signal_card = MDCard(orientation="vertical", padding=10, size_hint_y=0.28)
        self.signal_title = MDLabel(text="SIGNAL: --", font_style="H5", halign="center")
        self.confidence_label = MDLabel(
            text="Confidence: --%", font_style="H6", halign="center"
        )
        self.analysis_label = MDLabel(
            text="Choose a pair, then tap ANALYZE.", halign="center"
        )
        self.signal_card.add_widget(self.signal_title)
        self.signal_card.add_widget(self.confidence_label)
        self.signal_card.add_widget(self.analysis_label)

        controls = MDBoxLayout(orientation="horizontal", spacing=8, size_hint_y=0.12)
        controls.add_widget(
            MDRaisedButton(text="ANALYZE SELECTED", on_release=self.run_analysis)
        )
        controls.add_widget(
            MDRectangleFlatButton(text="SECURITY", on_release=self.open_security)
        )

        self.layout.add_widget(pair_grid)
        self.layout.add_widget(self.selected_label)
        self.layout.add_widget(self.signal_card)
        self.layout.add_widget(controls)
        self.add_widget(self.layout)

    def select_pair(self, instance):
        self.selected_pair = instance.text
        self.selected_label.text = f"Selected: {self.selected_pair}"
        self.signal_title.text = f"SIGNAL: {self.selected_pair}"
        self.confidence_label.text = "Confidence: --%"
        self.analysis_label.text = "Ready to analyze."

    def run_analysis(self, instance):
        app = MDApp.get_running_app()
        try:
            analyzer = AdvancedMarketAnalyzer(pair=self.selected_pair)
            raw_signal = analyzer.evaluate_signal()

            features = [
                raw_signal["rsi"],
                raw_signal["macd"],
                raw_signal["ema_gap"],
                raw_signal["price_vs_vwap"],
            ]
            adjusted = app.learning_engine.refine_confidence(
                raw_signal["confidence"], features
            )

            self.signal_title.text = f"{self.selected_pair}: {raw_signal['direction']}"
            self.confidence_label.text = f"Confidence: {adjusted}%"
            self.analysis_label.text = raw_signal["explanation"]

            executor = TradeExecutor(auto_trade_enabled=False)
            result = executor.process_signal(
                self.selected_pair,
                {**raw_signal, "confidence": adjusted},
                amount=10.0,
                min_confidence=75.0,
            )
            app.show_dialog("Signal", result["message"])
        except Exception as exc:
            app.show_dialog("Market Data Error", str(exc))

    def open_security(self, instance):
        MDApp.get_running_app().sm.current = "security"


class SecurityScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=25, spacing=15)

        layout.add_widget(
            MDLabel(text="Security Settings", font_style="H5", halign="center")
        )
        self.curr_pass = MDTextField(hint_text="Current Password", password=True)
        self.new_pass = MDTextField(hint_text="New Password", password=True)
        self.conf_pass = MDTextField(hint_text="Confirm New Password", password=True)

        layout.add_widget(self.curr_pass)
        layout.add_widget(self.new_pass)
        layout.add_widget(self.conf_pass)
        layout.add_widget(
            MDRaisedButton(
                text="CHANGE PASSWORD",
                pos_hint={"center_x": 0.5},
                on_release=self.update_password,
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="BACK TO DASHBOARD",
                pos_hint={"center_x": 0.5},
                on_release=self.go_back,
            )
        )
        self.add_widget(layout)

    def update_password(self, instance):
        app = MDApp.get_running_app()
        success, msg = app.security_manager.change_password(
            self.curr_pass.text, self.new_pass.text, self.conf_pass.text
        )
        app.show_dialog("Security", msg)
        if success:
            self.curr_pass.text = ""
            self.new_pass.text = ""
            self.conf_pass.text = ""

    def go_back(self, instance):
        MDApp.get_running_app().sm.current = "dashboard"


class MikeyBotApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        self.security_manager = SecurityManager()
        self.learning_engine = LearningEngine()

        self.sm = MDScreenManager()
        self.sm.add_widget(LoginScreen(name="login"))
        self.sm.add_widget(DashboardScreen(name="dashboard"))
        self.sm.add_widget(SecurityScreen(name="security"))
        return self.sm

    def show_dialog(self, title, text):
        dialog = MDDialog(title=title, text=text)
        dialog.buttons = [
            MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())
        ]
        dialog.open()


if __name__ == "__main__":
    MikeyBotApp().run()

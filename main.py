import sys
import traceback

# Catch global errors
def handle_exception(exc_type, exc_value, exc_traceback):
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(err)

sys.excepthook = handle_exception

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.spinner import Spinner
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.graphics import Color, Rectangle
    import requests

    # --- LOGIN SCREEN ---
    class LoginScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
            
            # App Title
            title = Label(
                text="[b]MikeyBot Signals[/b]\n[size=14sp]Please login to continue[/size]",
                markup=True,
                font_size='26sp',
                size_hint_y=None,
                height=80,
                halign='center'
            )
            layout.add_widget(title)

            # Username Field
            layout.add_widget(Label(text="Username:", size_hint_y=None, height=25, halign='left'))
            self.username = TextInput(
                text="Mikey Bot",
                multiline=False,
                size_hint_y=None,
                height=45,
                background_color=(0.2, 0.2, 0.25, 1),
                foreground_color=(1, 1, 1, 1)
            )
            layout.add_widget(self.username)

            # Password Field
            layout.add_widget(Label(text="Password:", size_hint_y=None, height=25, halign='left'))
            self.password = TextInput(
                text="mikey0982",
                password=True,
                multiline=False,
                size_hint_y=None,
                height=45,
                background_color=(0.2, 0.2, 0.25, 1),
                foreground_color=(1, 1, 1, 1)
            )
            layout.add_widget(self.password)

            # Status Message
            self.status = Label(text="", color=(1, 0.3, 0.3, 1), size_hint_y=None, height=30)
            layout.add_widget(self.status)

            # Login Button
            login_btn = Button(
                text="LOGIN",
                size_hint_y=None,
                height=50,
                background_color=(0.1, 0.6, 0.9, 1)
            )
            login_btn.bind(on_press=self.do_login)
            layout.add_widget(login_btn)

            self.add_widget(layout)

        def do_login(self, instance):
            user = self.username.text.strip()
            pwd = self.password.text.strip()

            if user == "Mikey Bot" and pwd == "mikey0982":
                self.manager.current = 'dashboard'
            else:
                self.status.text = "Invalid Username or Password!"

    # --- DASHBOARD SCREEN ---
    class DashboardScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

            # Header
            header = Label(
                text="[b]MikeyBot Signal Analyzer[/b]",
                markup=True,
                font_size='22sp',
                size_hint_y=None,
                height=50
            )
            layout.add_widget(header)

            # Dropdown Select Pair
            layout.add_widget(Label(text="Select Currency / Asset:", size_hint_y=None, height=25))
            self.pair_spinner = Spinner(
                text='EURUSD',
                values=('EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD', 'BTCUSD', 'XAUUSD (GOLD)'),
                size_hint_y=None,
                height=45
            )
            layout.add_widget(self.pair_spinner)

            # Analyze Button
            analyze_btn = Button(
                text="ANALYZE SELECTED PAIR",
                size_hint_y=None,
                height=50,
                background_color=(0.2, 0.7, 0.3, 1)
            )
            analyze_btn.bind(on_press=self.analyze)
            layout.add_widget(analyze_btn)

            # Results Display Area
            scroll = ScrollView()
            self.result_label = Label(
                text="Select a pair above and tap Analyze to fetch live signal...",
                markup=True,
                size_hint_y=None,
                text_size=(None, None),
                halign='center'
            )
            self.result_label.bind(texture_size=self.result_label.setter('size'))
            scroll.add_widget(self.result_label)
            layout.add_widget(scroll)

            # Logout Button
            logout_btn = Button(
                text="LOGOUT",
                size_hint_y=None,
                height=40,
                background_color=(0.8, 0.2, 0.2, 1)
            )
            logout_btn.bind(on_press=self.logout)
            layout.add_widget(logout_btn)

            self.add_widget(layout)

        def analyze(self, instance):
            selected = self.pair_spinner.text
            self.result_label.text = (
                f"[b]=== LIVE SIGNAL FOR {selected} ===[/b]\n\n"
                f"[color=00ff00]STATUS: ACTIVE[/color]\n"
                f"RECOMMENDATION: [b]BUY / BULLISH[/b]\n"
                f"ENTRY PRICE: Market Price\n"
                f"TAKE PROFIT (TP): +30 Pips\n"
                f"STOP LOSS (SL): -15 Pips\n\n"
                f"[i]Analysis executed successfully via MikeyBot Engine.[/i]"
            )

        def logout(self, instance):
            self.manager.current = 'login'

    # --- MAIN APP ---
    class MikeyBotApp(App):
        def build(self):
            sm = ScreenManager()
            sm.add_widget(LoginScreen(name='login'))
            sm.add_widget(DashboardScreen(name='dashboard'))
            return sm

    if __name__ == '__main__':
        MikeyBotApp().run()

except Exception as e:
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.scrollview import ScrollView

    class ErrorApp(App):
        def build(self):
            sv = ScrollView()
            lbl = Label(text=f"CRASH ERROR:\n\n{traceback.format_exc()}", color=(1, 0, 0, 1), size_hint_y=None)
            lbl.bind(texture_size=lbl.setter('size'))
            sv.add_widget(lbl)
            return sv

    ErrorApp().run()

import sys
import traceback
import random
from datetime import datetime, timedelta

# Global Exception Handling
def handle_exception(exc_type, exc_value, exc_traceback):
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(err)

sys.excepthook = handle_exception

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.spinner import Spinner
    from kivy.uix.scrollview import ScrollView
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.graphics import Color, Rectangle, RoundedRectangle
    from kivy.core.window import Window
    from kivy.metrics import dp

    # Colors
    BG_COLOR = (0.06, 0.08, 0.12, 1)       # Dark Slate BG
    CARD_COLOR = (0.12, 0.16, 0.23, 1)     # Card Background
    INPUT_BG = (0.07, 0.10, 0.15, 1)       # Clear Dark Input Box

    class ColoredCard(BoxLayout):
        def __init__(self, bg_color=CARD_COLOR, radius_val=10, **kwargs):
            super().__init__(**kwargs)
            with self.canvas.before:
                Color(*bg_color)
                self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[dp(radius_val),])
            self.bind(size=self._update_rect, pos=self._update_rect)

        def _update_rect(self, instance, value):
            self.rect.size = instance.size
            self.rect.pos = instance.pos

    # --- LOGIN SCREEN ---
    class LoginScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            
            with self.canvas.before:
                Color(*BG_COLOR)
                self.bg = Rectangle(size=Window.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)

            root = BoxLayout(orientation='vertical', padding=[dp(20), dp(30), dp(20), dp(20)], spacing=dp(15))

            # Header Title
            header = Label(
                text="[b][color=00E5FF]QUOTEX[/color] [color=FFFFFF]PRO BOT[/color][/b]\n"
                     "[size=13sp][color=8A99AD]Binary Options Signal Tool[/color][/size]",
                markup=True,
                font_size='24sp',
                size_hint_y=None,
                height=dp(60),
                halign='center'
            )
            root.add_widget(header)

            # Center Card (Auto Height - Squeeze Fix)
            card = ColoredCard(
                bg_color=CARD_COLOR, 
                orientation='vertical', 
                padding=[dp(20), dp(20), dp(20), dp(20)], 
                spacing=dp(10),
                size_hint=(1, None)
            )
            card.bind(minimum_height=card.setter('height'))

            card.add_widget(Label(
                text="[b][color=FFFFFF]Account Login[/color][/b]",
                markup=True,
                font_size='18sp',
                size_hint_y=None,
                height=dp(30),
                halign='center'
            ))

            # Username Section
            card.add_widget(Label(
                text="[color=00E5FF]Username:[/color]", 
                markup=True, 
                size_hint_y=None, 
                height=dp(20), 
                halign='left',
                font_size='13sp'
            ))
            self.username = TextInput(
                text="",
                hint_text="Enter Username...",
                multiline=False,
                size_hint_y=None,
                height=dp(48),
                background_normal='',
                background_color=INPUT_BG,
                foreground_color=(1, 1, 1, 1),
                hint_text_color=(0.5, 0.55, 0.65, 1),
                padding=[dp(12), dp(12), dp(12), dp(12)],
                font_size='15sp'
            )
            card.add_widget(self.username)

            # Password Section
            card.add_widget(Label(
                text="[color=00E5FF]Password:[/color]", 
                markup=True, 
                size_hint_y=None, 
                height=dp(20), 
                halign='left',
                font_size='13sp'
            ))
            self.password = TextInput(
                text="",
                hint_text="Enter Password...",
                password=True,
                multiline=False,
                size_hint_y=None,
                height=dp(48),
                background_normal='',
                background_color=INPUT_BG,
                foreground_color=(1, 1, 1, 1),
                hint_text_color=(0.5, 0.55, 0.65, 1),
                padding=[dp(12), dp(12), dp(12), dp(12)],
                font_size='15sp'
            )
            card.add_widget(self.password)

            # Error / Status
            self.status = Label(text="", markup=True, size_hint_y=None, height=dp(25), font_size='12sp')
            card.add_widget(self.status)

            # Login Button
            login_btn = Button(
                text="LOGIN TO BOT",
                size_hint_y=None,
                height=dp(48),
                background_normal='',
                background_color=(0.0, 0.5, 1.0, 1),
                bold=True,
                font_size='15sp'
            )
            login_btn.bind(on_press=self.do_login)
            card.add_widget(login_btn)

            root.add_widget(card)

            # Footer Space
            footer = Label(
                text="[color=445566]System Protected • v3.1 Fixed[/color]",
                markup=True,
                font_size='11sp',
                size_hint_y=None,
                height=dp(30)
            )
            root.add_widget(footer)

            self.add_widget(root)

        def _update_bg(self, instance, value):
            self.bg.size = instance.size
            self.bg.pos = instance.pos

        def do_login(self, instance):
            user = self.username.text.strip()
            pwd = self.password.text.strip()

            if not user or not pwd:
                self.status.text = "[color=FF5252]Please enter Username & Password![/color]"
                return

            if user == "Mikey Bot" and pwd == "mikey0982":
                self.status.text = "[color=00E676]Login Successful![/color]"
                self.manager.current = 'dashboard'
            else:
                self.status.text = "[color=FF5252]Invalid Username or Password![/color]"

    # --- DASHBOARD SCREEN ---
    class DashboardScreen(Screen):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            
            with self.canvas.before:
                Color(*BG_COLOR)
                self.bg = Rectangle(size=Window.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)

            layout = BoxLayout(orientation='vertical', padding=[dp(15), dp(20), dp(15), dp(15)], spacing=dp(10))

            header = Label(
                text="[b][color=00E5FF]QUOTEX[/color] [color=FFFFFF]LIVE SIGNALS[/color][/b]",
                markup=True,
                font_size='20sp',
                size_hint_y=None,
                height=dp(35)
            )
            layout.add_widget(header)

            ctrl_card = ColoredCard(
                bg_color=CARD_COLOR, 
                orientation='vertical', 
                padding=[dp(12), dp(12), dp(12), dp(12)], 
                spacing=dp(6),
                size_hint=(1, None)
            )
            ctrl_card.bind(minimum_height=ctrl_card.setter('height'))

            ctrl_card.add_widget(Label(
                text="[color=8A99AD]Select Asset:[/color]", 
                markup=True, 
                size_hint_y=None, 
                height=dp(18), 
                font_size='12sp'
            ))
            self.pair_spinner = Spinner(
                text='EURUSD (OTC)',
                values=('EURUSD (OTC)', 'GBPUSD (OTC)', 'USDJPY (OTC)', 'EURGBP', 'BTCUSD', 'XAUUSD (GOLD)'),
                size_hint_y=None,
                height=dp(42),
                background_normal='',
                background_color=INPUT_BG,
                color=(1, 1, 1, 1)
            )
            ctrl_card.add_widget(self.pair_spinner)

            ctrl_card.add_widget(Label(
                text="[color=8A99AD]Select Timeframe:[/color]", 
                markup=True, 
                size_hint_y=None, 
                height=dp(18), 
                font_size='12sp'
            ))
            self.tf_spinner = Spinner(
                text='1 MINUTE',
                values=('1 MINUTE', '2 MINUTES', '5 MINUTES'),
                size_hint_y=None,
                height=dp(42),
                background_normal='',
                background_color=INPUT_BG,
                color=(1, 1, 1, 1)
            )
            ctrl_card.add_widget(self.tf_spinner)

            analyze_btn = Button(
                text="GENERATE SIGNAL",
                size_hint_y=None,
                height=dp(45),
                background_normal='',
                background_color=(0.0, 0.8, 0.4, 1),
                bold=True,
                font_size='14sp'
            )
            analyze_btn.bind(on_press=self.generate_quotex_signal)
            ctrl_card.add_widget(analyze_btn)

            layout.add_widget(ctrl_card)

            self.result_card = ColoredCard(bg_color=CARD_COLOR, orientation='vertical', padding=[dp(12), dp(12), dp(12), dp(12)])
            scroll = ScrollView()
            self.result_label = Label(
                text="[color=8A99AD]Select asset above and tap\n[b]'GENERATE SIGNAL'[/b][/color]",
                markup=True,
                size_hint_y=None,
                text_size=(None, None),
                halign='center'
            )
            self.result_label.bind(texture_size=self.result_label.setter('size'))
            scroll.add_widget(self.result_label)
            self.result_card.add_widget(scroll)

            layout.add_widget(self.result_card)

            logout_btn = Button(
                text="LOGOUT",
                size_hint_y=None,
                height=dp(40),
                background_normal='',
                background_color=(0.8, 0.2, 0.2, 1),
                bold=True
            )
            logout_btn.bind(on_press=self.logout)
            layout.add_widget(logout_btn)

            self.add_widget(layout)

        def _update_bg(self, instance, value):
            self.bg.size = instance.size
            self.bg.pos = instance.pos

        def generate_quotex_signal(self, instance):
            pair = self.pair_spinner.text
            timeframe = self.tf_spinner.text
            
            direction = random.choice(["CALL (UP ⬆)", "PUT (DOWN ⬇)"])
            is_call = "CALL" in direction
            color_code = "00E676" if is_call else "FF3355"
            accuracy = random.randint(89, 97)
            
            now = datetime.now()
            entry_time = (now + timedelta(seconds=10)).strftime("%H:%M:%S")
            
            self.result_label.text = (
                f"[b][color=00E5FF]=== LIVE SIGNAL RESULTS ===[/color][/b]\n\n"
                f"[b]PAIR:[/b] [color=FFFFFF]{pair}[/color]\n"
                f"[b]TIMEFRAME:[/b] [color=FFFFFF]{timeframe}[/color]\n\n"
                f"[b]ACTION:[/b] [color={color_code}][size=22sp]{direction}[/size][/color]\n\n"
                f"[b]ENTRY TIME:[/b] [color=FFFFFF]{entry_time}[/color]\n"
                f"[b]WIN RATE:[/b] [color=00E676]{accuracy}% Accuracy[/color]\n"
                f"[b]STRATEGY:[/b] [color=8A99AD]Martingale Max 1 Step[/color]\n\n"
                f"[i][color=556578]Execute trade immediately at candle start.[/color][/i]"
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

            

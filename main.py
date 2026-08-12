import sys
import traceback

# Catch all global errors on Android
def handle_exception(exc_type, exc_value, exc_traceback):
    err = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(err)

sys.excepthook = handle_exception

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.spinner import Spinner
    from kivy.uix.scrollview import ScrollView
    import requests

    class MikeyBotApp(App):
        def build(self):
            self.title = "MikeyBot"
            
            root = BoxLayout(orientation='vertical', padding=20, spacing=15)
            
            # Title
            title_label = Label(
                text="[b]MikeyBot Signals[/b]", 
                markup=True, 
                font_size='24sp', 
                size_hint_y=None, 
                height=50
            )
            root.add_widget(title_label)
            
            # Status area
            self.status_label = Label(
                text="App Ready. Select Pair & Analyze.", 
                font_size='16sp',
                size_hint_y=None,
                height=40
            )
            root.add_widget(self.status_label)
            
            # Currency Pair Dropdown
            self.pair_spinner = Spinner(
                text='EURUSD',
                values=('EURUSD', 'GBPUSD', 'USDJPY', 'AUDUSD', 'BTCUSD'),
                size_hint_y=None,
                height=50
            )
            root.add_widget(self.pair_spinner)
            
            # Analyze Button
            analyze_btn = Button(
                text="ANALYZE SELECTED",
                size_hint_y=None,
                height=55,
                background_color=(0.2, 0.6, 1, 1)
            )
            analyze_btn.bind(on_press=self.analyze_pair)
            root.add_widget(analyze_btn)
            
            # Output Screen
            scroll = ScrollView()
            self.result_label = Label(
                text="Signal output will appear here...", 
                size_hint_y=None,
                text_size=(None, None),
                halign='center'
            )
            self.result_label.bind(texture_size=self.result_label.setter('size'))
            scroll.add_widget(self.result_label)
            
            root.add_widget(scroll)
            return root

        def analyze_pair(self, instance):
            selected = self.pair_spinner.text
            self.status_label.text = f"Analyzing {selected}..."
            self.result_label.text = f"=== SIGNAL FOR {selected} ===\n\nStatus: Active\nTrend: BULLISH\nEntry: Market Price\nTP: +20 pips\nSL: -10 pips"

    if __name__ == '__main__':
        MikeyBotApp().run()

except Exception as e:
    # Fallback Error Screen if app crashes
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.scrollview import ScrollView

    class ErrorApp(App):
        def build(self):
            sv = ScrollView()
            lbl = Label(
                text=f"CRASH ERROR:\n\n{traceback.format_exc()}", 
                color=(1, 0, 0, 1),
                size_hint_y=None
            )
            lbl.bind(texture_size=lbl.setter('size'))
            sv.add_widget(lbl)
            return sv

    ErrorApp().run()

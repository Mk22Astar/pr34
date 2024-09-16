from kivy.config import Config
Config.set('graphics', 'width', '500')  # Устанавливаем ширину окна в 500 пикселей

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

class RainbowApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Метка для отображения названия цвета
        self.color_label = Label(text="Выберите цвет", size_hint=(1, 0.2), font_size='24sp')
        # Убираем фоновый цвет метки
        self.color_label.canvas.before.clear()
        self.layout.add_widget(self.color_label)

        # Текстовое поле для отображения кода цвета
        self.color_code_input = TextInput(text="", readonly=True, size_hint=(1, 0.3), font_size='24sp', multiline=False)
        self.layout.add_widget(self.color_code_input)

        # Список цветов
        self.colors = [
            ("Красный", "#ff0000"),
            ("Оранжевый", "#ff8800"),
            ("Желтый", "#ffff00"),
            ("Зеленый", "#00ff00"),
            ("Голубой", "#00ffff"),
            ("Синий", "#0000ff"),
            ("Фиолетовый", "#ff00ff")
        ]

        # Создаем кнопки для каждого цвета
        for color_name, color_hex in self.colors:
            color_value = [int(color_hex[i:i+2], 16) / 255.0 for i in (1, 3, 5)]
            color_value += [1]  # Прозрачность
            btn = Button(text=color_name, background_normal='', background_color=color_value, on_press=self.on_button_press, size_hint_y=None, height=50)
            self.layout.add_widget(btn)

        return self.layout

    def on_button_press(self, instance):
        color_name = instance.text
        color_hex = instance.background_color
        color_hex_code = f"#{int(color_hex[0] * 255):02X}{int(color_hex[1] * 255):02X}{int(color_hex[2] * 255):02X}"

        # Обновляем название цвета в метке
        self.color_label.text = color_name

        # Обновляем код цвета в текстовом поле
        self.color_code_input.text = color_hex_code

        # Обновляем цвет фона метки
        with self.color_label.canvas.before:
            self.color_label.canvas.before.clear()
            Color(*color_hex)
            Rectangle(size=self.color_label.size, pos=self.color_label.pos)

        # Обновляем цвет текста метки для лучшей видимости
        avg_color = sum(color_hex[:3]) / 3
        self.color_label.color = (1, 1, 1, 1) if avg_color < 0.5 else (0, 0, 0, 1)

if __name__ == "__main__":
    RainbowApp().run()

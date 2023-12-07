import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    days_input = ObjectProperty()

    hours_output = ObjectProperty()
    minutes_output = ObjectProperty()
    seconds_output = ObjectProperty()
    milliseconds_output = ObjectProperty()
    weeks_output = ObjectProperty()

    def convert(self):
        days = int(self.days_input.text)
        hours = days * 24
        minutes = days * 1440
        seconds = minutes * 60
        milliseconds = seconds * 1000
        weeks = days/7
        self.ids.hours_output.text = str(hours)
        self.ids.minutes_output.text = str(minutes)
        self.ids.seconds_output.text = str(seconds)
        self.ids.milliseconds_output.text = str(milliseconds)
        self.ids.weeks_output.text = str(round(weeks, 2))


class MyWin(App):
    Window.size = (1056, 628)

    def build(self):
        return Container()


if __name__ == '__main__':
    MyWin().run()
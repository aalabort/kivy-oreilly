from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.uix.listview import ListItemButton
from kivy.network.urlrequest import UrlRequest
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label

import random
from kivy.graphics import Color, Ellipse
from kivy.clock import Clock



class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    def show_current_weather(self, location):
        self.clear_widgets()

        if location is None and self.current_weather is None:
            location = ('New York','US')
        if location is not None:
            self.current_weather=CurrentWeather()
            self.current_weather.location = location
        self.current_weather.update_weather()
        self.add_widget(self.current_weather)


    def show_add_location_form(self):
        self.clear_widgets()
        location_form = AddLocationForm()
        self.add_widget(location_form)

class WeatherarnauApp(App):
    pass

class CurrentWeather(BoxLayout):
    location = ListProperty(['New York', 'US'])
    conditions = ObjectProperty()
    conditions_image = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()

    def update_weather(self):
        print '1'
        weather_template = 'http://api.openweathermap.org/data/2.5/weather?APPID=ef4f6b76310abad083b96a45a6f547be&q={},{}&units=metric'
        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data,dict) else data
        self.render_conditions(data['weather'][0]['description'])
        self.conditions_image = 'http://openweathermap.org/img/w/{}.png'.format(data['weather'][0]['icon'])
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']

    def render_conditions(self,conditions_description):
        # if 'few clouds' in conditions_description.lower():
        #     conditions_widget = Factory.ClearConditions()
        # if 'snow' in conditions_description.lower():
        #     conditions_widget = SnowConditions()
        # elif 'clear' in conditions_description.lower():
        #     conditions_widget = SnowConditions()
        # else:
        #     conditions_widget = Factory.UnknownConditions()

        # conditions_widget = Conditions()
        # conditions_widget.conditions = conditions_description
        self.conditions = conditions_description
        self.conditions_image = self.conditions_image
        # self.conditions.clear_widgets()
        # self.conditions.add_widget(conditions_widget)




class Conditions(BoxLayout):
    conditions = StringProperty()
    conditions_image = StringProperty()

class SnowConditions(Conditions):
    FLAKE_SIZE = 5
    NUM_FLAKES = 60
    FLAKE_AREA = FLAKE_SIZE * NUM_FLAKES
    FLAKE_INTERVAL = 1.0 / 3.0

    def __init__(self, **kwargs):
        super(SnowConditions, self).__init__(**kwargs)
        self.flakes = [[x * self.FLAKE_SIZE, 0] for x in range(self.NUM_FLAKES)]
        Clock.schedule_interval(self.update_flakes, self.FLAKE_INTERVAL)
        #self.update_flakes(self.FLAKE_INTERVAL)

    def update_flakes(self, time):
        for f in self.flakes:
            f[0] += random.choice([-1, 1])
            f[1] -= random.randint(0, self.FLAKE_SIZE)
            if f[1] <= 0:
                f[1] = random.randint(0, int(self.height))
        self.canvas.before.clear()
        with self.canvas.before:
            widget_x = self.center_x - self. FLAKE_AREA / 2
            widget_y = self.pos[1]
            for x_flake, y_flake in self.flakes:
                x = widget_x + x_flake
                y = widget_y + y_flake
                Color(0.9, 0.9, 1.0)
                Ellipse(pos=(x, y), size=(self.FLAKE_SIZE, self.FLAKE_SIZE))



class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()


    def search_location(self):
        #del self.search_results.adapter.data[:]
        popup = Popup(title='Test popup', content=Label(text='Hello world'), size_hint=(None, None), size=(400, 400))
        popup.open()
        self.search_results.adapter.data = []
        self.search_results._trigger_reset_populate()
        url_template = 'http://api.openweathermap.org/data/2.5/find?APPID=ef4f6b76310abad083b96a45a6f547be&q={}&type=like'
        url_search = url_template.format(self.search_input.text)
        request = UrlRequest(url_search,self.found_location)

    def search_location_coord(self):
        url_template = 'http://api.openweathermap.org/data/2.5/find?APPID=ef4f6b76310abad083b96a45a6f547be&lat={}&lon={}&type=like'
        url_search = url_template.format(self.search_input.text.split()[0],self.search_input.text.split()[1])
        request = UrlRequest(url_search,self.found_location)

    def found_location(self, request, data):
        cities = [(d['name'], d['sys']['country']) for d in data['list']]
        #cities = [d['name'] for d in data['list']]
        self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    def args_converter(self, index, data_item):
        city, country = data_item
        return {'location': (city, country)}

class LocationButton(ListItemButton):
    location = ListProperty()
    pass




if __name__ == '__main__':
    WeatherarnauApp().run()

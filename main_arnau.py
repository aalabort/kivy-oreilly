from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.uix.listview import ListItemButton
from kivy.network.urlrequest import UrlRequest
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.label import Label

def locations_args_converter(self, index, data_item):
    city, country = data_item
    return {'location': (city, country)}




class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()
    locations = ObjectProperty()

    def show_locations(self):
        self.clear_widgets()
        self.add_widget(self.locations)

    def show_current_weather(self, location):
        self.clear_widgets()

        if self.current_weather is None:
            self.current_weather = CurrentWeather()
        if self.location is None:
            self.location = Factory.Locations()

        if location is not None:
            self.current_weather.location = location
            if location not in self.locations.locations_list.adapter.data:
                self.locations.locations_list.adapter.data.append(location)
                self.locations.location_list._trigger_reset_populate()

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
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()
    conditions_image = StringProperty()

    def update_weather(self):
        print '1'
        weather_template = 'http://api.openweathermap.org/data/2.5/weather?APPID=ef4f6b76310abad083b96a45a6f547be&q={},{}&units=metric'
        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data,dict) else data
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.conditions_image = "http://openweathermap.org/img/w/{}.png".format(
data['weather'][0]['icon'])







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


class LocationButton(ListItemButton):
    location = ListProperty()
    pass



if __name__ == '__main__':
    WeatherarnauApp().run()

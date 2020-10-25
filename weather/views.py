from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.
def weather_view(request):
    city_name = 'Colombo'
    if request.method == 'POST':
        form = CityForm(request.POST)
        print("Request: ", request.POST)
        form.save()

    
    cities = City.objects.all()
    for city in cities:
        print("City: ", city.name)
        city_name = city.name
    City.objects.all().delete()

    form = CityForm()

    # city = "Colombo"
    

    url = "https://rapidapi.p.rapidapi.com/weather"
    querystring = {"q": city_name ,"lat":"0","lon":"0","lang":"null","units":"\"metric\"","mode":""}
    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "0d36633e52mshe8328021f36464fp14f3ccjsnffd5f7e98c06"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    # print(response.text)
    # response = {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"10d"}],"base":"stations","main":{"temp":285.2,"feels_like":283.71,"temp_min":284.82,"temp_max":285.37,"pressure":1023,"humidity":66},"visibility":10000,"wind":{"speed":0.78,"deg":45},"clouds":{"all":90},"dt":1603037324,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1603002599,"sunset":1603040453},"timezone":3600,"id":2643743,"name":"London","cod":200}
    response = response.json()
    city_weather = {
        'city': response['name'],
        'temperature': int(response['main']['temp'] - 273),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'wind_speed': '{0:.3g}'.format((response['wind']['speed']*1.852)),
        'humidity': int(response['main']['humidity'])
    }
    print(city_weather)
    context = {
        'city_weather': city_weather,
        'form' : form
    }
    return render(request, 'weather/weather.html', context)

def contact_view(request):
    return render(request, 'weather/contact.html', {})

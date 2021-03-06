import requests,json
api_key= "1f331ac62d1c9a127458b0c3042745e9"
city_name=input("ingresa tu ciudad:")
complete_url="http://api.openweathermap.org/data/2.5/weather?q=London&appid=165ac5562bde3bd0f3f2dad3e3f3fd5c"
response=requests.get(complete_url)
x=response.json()
if x["cod"] != "404":
    print(x)
    y=x["main"]
    current_temperature=y["temp"]
    current_pressure=y["pressure"]
    current_humidity=y["humidity"]
    z=x["weather"]
    weather_description=z[0]["description"]
    print("tem. en grados kelvin")
    str(current_temperature)
    "\n presion atmosferica ="+str(current_pressure)
    "\n humedad en porcentaje ="+str(current_humidity)
    "\n descripcion ="+str(weather_description)
else:
    print("ciudad no encontrada")

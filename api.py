import requests
import subprocess

class Clima:
    ciudad = ""
    api_key = "006a838a6d03c00a993d8b556cd9237a"
    
    def __init__(self):
        self.ciudad = input("ingrese el nombre:")
        self.apiKey = "006a838a6d03c00a993d8b556cd9237a"

    def obtenerClima(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.ciudad}&appid={self.apiKey}"
        response = requests.get(url)
        datosClima = response.json()
        temperatura = datosClima["main"]["temp"]
        humedad = datosClima["main"]["humidity"]
        descripcion = datosClima["weather"][0]["description"]
          
        return temperatura, humedad, descripcion

climaActual = Clima()

temperatura, humedad, descripcion = climaActual.obtenerClima()


print("Datos del clima en:", climaActual.ciudad.upper())
a= temperatura-273
b= a//1
print("Temperatura:", b,"º", "Grados Celsius")
print("Humedad:",humedad, "%")
print("Descripcion:",descripcion.capitalize())

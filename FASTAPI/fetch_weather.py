from urllib import response
import requests
#import openmeteo-requests

def get_weather(lat=21.15,lon=79.08):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return {
     "temperature" : data["current_weather"]["temperature"],
     "wind_speed" : data["current_weather"]["temperature"],
     "timestamps" :  data["current_weather"]["temperature"]     
    }
    
if __name__ == "_main_":
    print(get_weather())    
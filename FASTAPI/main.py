from fastapi import FastAPI
from Projects.FASTAPI.fetch_weather import get_weather
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World",
            "message": "Weather API is working"}
    
@app.get("/weather")
def get_current_weather():
    return get_weather()

from requests import *
class DataManager:
    URL = "https://api.sheety.co/46cb9f32f29918b1f0b9cbf10acd2970/copyOfFlightDeals/prices"
    #This class is responsible for talking to the Google Sheet.
    def sheet(self):
        data = get()

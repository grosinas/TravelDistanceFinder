import requests
from Constants import OPEN_ROUTING_API_KEY

class DistanceCalculator:
    def __init__(self, destination, transport_mode):
        self.destination = destination
        self.transport_mode = transport_mode
        self.coordinates = self.get_address_coordinates(self.destination)
         
    def calculate_travel(self, start):
        url = f"https://api.openrouteservice.org/v2/directions/{self.transport_mode}?api_key={OPEN_ROUTING_API_KEY}&start={start[0]},{start[1]}&end={self.coordinates[0]},{self.coordinates[1]}"
        response = requests.get(url)
        data = response.json()
        distance_in_km = data['features'][0]['properties']['summary']['distance']/1000
        time_in_minutes = data['features'][0]['properties']['summary']['duration']/60
        return (distance_in_km, time_in_minutes)
    
    def get_address_coordinates(self, address):
        url = f"https://api.openrouteservice.org/geocode/search?text={address}&api_key={OPEN_ROUTING_API_KEY}"
        response = requests.get(url)
        data = response.json()
        return data['features'][0]['geometry']['coordinates']
    
    def update_transport_mode(self, transport_mode):
        self.transport_mode = transport_mode
        
    def update_destination(self, destination):
        self.destination = destination
        self.coordinates = self.get_address_coordinates(self.destination)

from itemScraper import ItemScraper
from distanceCalculator import DistanceCalculator
import sys

if len(sys.argv) != 4:
    print("Usage: python app.py <webpage> <output_filename> <label>")
    sys.exit(1)
    
address = sys.argv[1]
address_filename = sys.argv[2]
label = sys.argv[3]

scraper = ItemScraper(address, address_filename, label)
scraper.save_items()

print("Enter the address you want to calculate the distance to:")
address = input()
print("Enter the transport mode you want to use:")
transport_mode = input()
print("Enter the output filename:")
output_filename = input()

with open(address_filename, 'r') as f:
    addresses = f.readlines()

distance_calculator = DistanceCalculator(address, transport_mode)

with open(output_filename, 'w') as f:
    f.write("Transport mode: " + transport_mode + "\n")
    f.write("Address: " + address + "\n ")
    f.write("----------------------------------\n")
    for address in addresses:
        start = distance_calculator.get_address_coordinates(address)
        distance, time = distance_calculator.calculate_travel(start)
        f.write(f"{address.strip()}: {distance} km, {time} minutes\n")



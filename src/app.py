from itemScraper import ItemScraper
import sys

if len(sys.argv) != 4:
    print("Usage: python app.py <webpage> <output_filename> <label>")
    
address = sys.argv[1]
output_filename = sys.argv[2]
label = sys.argv[3]

scraper = ItemScraper(address, output_filename, label)
scraper.save_items()

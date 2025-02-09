import requests
from bs4 import BeautifulSoup

class ItemScraper:
    def __init__(self, webpage, output_filename, label):
        self.webpage = webpage
        self.output_filename = output_filename
        self.label = label

    def scrape_items(self):
        response = requests.get(self.webpage)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', self.label)
        return items

    def save_items(self):
        items = self.scrape_items()
        with open(self.output_filename, 'w') as f:
            for item in items:
                clean_item = ' '.join(item.text.replace('\r', '').replace('\n', '').split())
                f.write(clean_item + '\n')
